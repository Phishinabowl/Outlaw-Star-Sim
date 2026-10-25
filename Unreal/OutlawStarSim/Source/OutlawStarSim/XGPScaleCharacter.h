#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "XGPScaleCharacter.generated.h"

class UCameraComponent;
class USpringArmComponent;
class UStaticMeshComponent;
class UInputAction;
class UInputMappingContext;
struct FInputActionValue;

/** Phase 3.1 fit proxy. Dimensions are provisional, not character measurements. */
UCLASS()
class OUTLAWSTARSIM_API AXGPScaleCharacter : public ACharacter
{
	GENERATED_BODY()

public:
	AXGPScaleCharacter();
	virtual void Tick(float DeltaSeconds) override;
	virtual void PawnClientRestart() override;
	virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;
	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

protected:
	virtual void BeginPlay() override;

private:
	void EnsureInputObjects();
	void MoveForward(const FInputActionValue& Value);
	void MoveRight(const FInputActionValue& Value);
	void LookYaw(const FInputActionValue& Value);
	void LookPitch(const FInputActionValue& Value);
	void TogglePerspective();
	void ApplyPerspective();

	UPROPERTY(VisibleAnywhere, Category="Scale Fixture")
	TObjectPtr<UCameraComponent> FirstPersonCamera;
	UPROPERTY(VisibleAnywhere, Category="Scale Fixture")
	TObjectPtr<USpringArmComponent> ThirdPersonArm;
	UPROPERTY(VisibleAnywhere, Category="Scale Fixture")
	TObjectPtr<UCameraComponent> ThirdPersonCamera;
	UPROPERTY(VisibleAnywhere, Category="Scale Fixture")
	TObjectPtr<UStaticMeshComponent> BodyProxy;
	UPROPERTY(VisibleAnywhere, Category="Scale Fixture")
	TObjectPtr<UStaticMeshComponent> HeadProxy;
	UPROPERTY(Transient)
	TObjectPtr<UInputMappingContext> FixtureInputContext;
	UPROPERTY(Transient)
	TObjectPtr<UInputAction> ForwardAction;
	UPROPERTY(Transient)
	TObjectPtr<UInputAction> RightAction;
	UPROPERTY(Transient)
	TObjectPtr<UInputAction> YawAction;
	UPROPERTY(Transient)
	TObjectPtr<UInputAction> PitchAction;
	UPROPERTY(Transient)
	TObjectPtr<UInputAction> PerspectiveAction;

	bool bThirdPerson = false;
};
