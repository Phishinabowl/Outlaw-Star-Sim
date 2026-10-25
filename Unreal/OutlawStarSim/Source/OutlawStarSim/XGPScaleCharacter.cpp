#include "XGPScaleCharacter.h"

#include "Camera/CameraComponent.h"
#include "Components/CapsuleComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/Engine.h"
#include "Engine/LocalPlayer.h"
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/SpringArmComponent.h"
#include "InputAction.h"
#include "InputActionValue.h"
#include "InputMappingContext.h"
#include "InputModifiers.h"
#include "UObject/ConstructorHelpers.h"

DEFINE_LOG_CATEGORY_STATIC(LogXGPScale, Log, All);

AXGPScaleCharacter::AXGPScaleCharacter()
{
	PrimaryActorTick.bCanEverTick = true;
	GetCapsuleComponent()->InitCapsuleSize(30.f, 90.f);
	bUseControllerRotationYaw = true;
	GetCharacterMovement()->bOrientRotationToMovement = false;
	GetCharacterMovement()->MaxWalkSpeed = 300.f;
	GetCharacterMovement()->MaxStepHeight = 35.f;
	GetCharacterMovement()->SetWalkableFloorAngle(45.f);

	FirstPersonCamera = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
	FirstPersonCamera->SetupAttachment(GetRootComponent());
	FirstPersonCamera->SetRelativeLocation(FVector(0.f, 0.f, 70.f));
	FirstPersonCamera->bUsePawnControlRotation = true;
	FirstPersonCamera->FieldOfView = 90.f;

	ThirdPersonArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("ThirdPersonArm"));
	ThirdPersonArm->SetupAttachment(GetRootComponent());
	ThirdPersonArm->TargetArmLength = 300.f;
	ThirdPersonArm->TargetOffset = FVector(0.f, 0.f, 55.f);
	ThirdPersonArm->bUsePawnControlRotation = true;
	ThirdPersonArm->bDoCollisionTest = true;
	ThirdPersonArm->ProbeSize = 12.f;
	ThirdPersonCamera = CreateDefaultSubobject<UCameraComponent>(TEXT("ThirdPersonCamera"));
	ThirdPersonCamera->SetupAttachment(ThirdPersonArm, USpringArmComponent::SocketName);
	ThirdPersonCamera->FieldOfView = 90.f;
	ThirdPersonCamera->SetAutoActivate(false);

	static ConstructorHelpers::FObjectFinder<UStaticMesh> Cube(TEXT("/Engine/BasicShapes/Cube.Cube"));
	static ConstructorHelpers::FObjectFinder<UStaticMesh> Sphere(TEXT("/Engine/BasicShapes/Sphere.Sphere"));
	BodyProxy = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("BodyProxy"));
	BodyProxy->SetupAttachment(GetRootComponent());
	BodyProxy->SetStaticMesh(Cube.Object);
	BodyProxy->SetRelativeLocation(FVector(0.f, 0.f, -10.f));
	BodyProxy->SetRelativeScale3D(FVector(.44f, .32f, 1.5f));
	BodyProxy->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	HeadProxy = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("HeadProxy"));
	HeadProxy->SetupAttachment(GetRootComponent());
	HeadProxy->SetStaticMesh(Sphere.Object);
	HeadProxy->SetRelativeLocation(FVector(0.f, 0.f, 77.5f));
	HeadProxy->SetRelativeScale3D(FVector(.25f));
	HeadProxy->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	ApplyPerspective();
}

void AXGPScaleCharacter::BeginPlay()
{
	Super::BeginPlay();
	ApplyPerspective();
	UE_LOG(LogXGPScale, Display, TEXT("Begin actor=%s id=%u capsuleRadius=%.1f halfHeight=%.1f eyeAboveFeet=160 walkSpeed=300"),
		*GetName(), GetUniqueID(), GetCapsuleComponent()->GetUnscaledCapsuleRadius(),
		GetCapsuleComponent()->GetUnscaledCapsuleHalfHeight());
}

void AXGPScaleCharacter::EnsureInputObjects()
{
	if (FixtureInputContext) return;
	FixtureInputContext = NewObject<UInputMappingContext>(this);
	auto MakeAxis = [this]()
	{
		UInputAction* Action = NewObject<UInputAction>(this);
		Action->ValueType = EInputActionValueType::Axis1D;
		return Action;
	};
	ForwardAction = MakeAxis();
	RightAction = MakeAxis();
	YawAction = MakeAxis();
	PitchAction = MakeAxis();
	PerspectiveAction = NewObject<UInputAction>(this);
	PerspectiveAction->ValueType = EInputActionValueType::Boolean;
	FixtureInputContext->MapKey(ForwardAction, EKeys::W);
	FixtureInputContext->MapKey(ForwardAction, EKeys::S).Modifiers.Add(NewObject<UInputModifierNegate>(FixtureInputContext));
	FixtureInputContext->MapKey(RightAction, EKeys::D);
	FixtureInputContext->MapKey(RightAction, EKeys::A).Modifiers.Add(NewObject<UInputModifierNegate>(FixtureInputContext));
	FixtureInputContext->MapKey(YawAction, EKeys::MouseX);
	FixtureInputContext->MapKey(PitchAction, EKeys::MouseY);
	FixtureInputContext->MapKey(PerspectiveAction, EKeys::V);
}

void AXGPScaleCharacter::PawnClientRestart()
{
	Super::PawnClientRestart();
	EnsureInputObjects();
	if (APlayerController* PC = Cast<APlayerController>(GetController()))
	{
		if (ULocalPlayer* LP = PC->GetLocalPlayer())
		{
			if (UEnhancedInputLocalPlayerSubsystem* Input = LP->GetSubsystem<UEnhancedInputLocalPlayerSubsystem>())
			{
				Input->RemoveMappingContext(FixtureInputContext);
				Input->AddMappingContext(FixtureInputContext, 0);
			}
		}
	}
}

void AXGPScaleCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);
	EnsureInputObjects();
	UEnhancedInputComponent* Input = CastChecked<UEnhancedInputComponent>(PlayerInputComponent);
	Input->BindAction(ForwardAction, ETriggerEvent::Triggered, this, &AXGPScaleCharacter::MoveForward);
	Input->BindAction(RightAction, ETriggerEvent::Triggered, this, &AXGPScaleCharacter::MoveRight);
	Input->BindAction(YawAction, ETriggerEvent::Triggered, this, &AXGPScaleCharacter::LookYaw);
	Input->BindAction(PitchAction, ETriggerEvent::Triggered, this, &AXGPScaleCharacter::LookPitch);
	Input->BindAction(PerspectiveAction, ETriggerEvent::Started, this, &AXGPScaleCharacter::TogglePerspective);
}

void AXGPScaleCharacter::MoveForward(const FInputActionValue& Value)
{
	AddMovementInput(GetActorForwardVector(), Value.Get<float>());
}

void AXGPScaleCharacter::MoveRight(const FInputActionValue& Value)
{
	AddMovementInput(GetActorRightVector(), Value.Get<float>());
}

void AXGPScaleCharacter::LookYaw(const FInputActionValue& Value)
{
	AddControllerYawInput(Value.Get<float>() * .2f);
}

void AXGPScaleCharacter::LookPitch(const FInputActionValue& Value)
{
	AddControllerPitchInput(-Value.Get<float>() * .2f);
}

void AXGPScaleCharacter::ApplyPerspective()
{
	FirstPersonCamera->SetActive(!bThirdPerson);
	ThirdPersonCamera->SetActive(bThirdPerson);
	BodyProxy->SetOwnerNoSee(!bThirdPerson);
	HeadProxy->SetOwnerNoSee(!bThirdPerson);
}

void AXGPScaleCharacter::TogglePerspective()
{
	const FTransform Before = GetActorTransform();
	const FVector VelocityBefore = GetVelocity();
	const uint32 IdentityBefore = GetUniqueID();
	bThirdPerson = !bThirdPerson;
	ApplyPerspective();
	const bool bStable = Before.Equals(GetActorTransform()) && IdentityBefore == GetUniqueID()
		&& VelocityBefore.Equals(GetVelocity());
	ensureAlwaysMsgf(bStable, TEXT("Perspective toggle changed the physical player"));
	UE_LOG(LogXGPScale, Display, TEXT("Perspective=%s actor=%s id=%u position=%s velocity=%s stable=%s capsule=%.1f/%.1f"),
		bThirdPerson ? TEXT("third") : TEXT("first"), *GetName(), GetUniqueID(),
		*GetActorLocation().ToCompactString(), *GetVelocity().ToCompactString(), bStable ? TEXT("true") : TEXT("false"),
		GetCapsuleComponent()->GetUnscaledCapsuleRadius(), GetCapsuleComponent()->GetUnscaledCapsuleHalfHeight());
}

void AXGPScaleCharacter::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);
	if (GEngine && IsLocallyControlled())
	{
		GEngine->AddOnScreenDebugMessage(3101, 0.f, FColor::Cyan,
			FString::Printf(TEXT("3.1 FIT PROXY | WASD walk | Mouse look | V view | %s | body id %u | capsule 180h x 60w cm"),
				bThirdPerson ? TEXT("THIRD PERSON") : TEXT("FIRST PERSON"), GetUniqueID()));
	}
}

void AXGPScaleCharacter::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	if (APlayerController* PC = Cast<APlayerController>(GetController()))
	{
		if (ULocalPlayer* LP = PC->GetLocalPlayer())
		{
			if (UEnhancedInputLocalPlayerSubsystem* Input = LP->GetSubsystem<UEnhancedInputLocalPlayerSubsystem>())
			{
				if (FixtureInputContext) Input->RemoveMappingContext(FixtureInputContext);
			}
		}
	}
	Super::EndPlay(EndPlayReason);
}
