#include "XGPScaleFixture.h"

#include "Components/SceneComponent.h"
#include "Components/StaticMeshComponent.h"
#include "Components/TextRenderComponent.h"
#include "UObject/ConstructorHelpers.h"

AXGPScaleFixture::AXGPScaleFixture()
{
	PrimaryActorTick.bCanEverTick = false;
	USceneComponent* Root = CreateDefaultSubobject<USceneComponent>(TEXT("FixtureRoot"));
	Root->SetMobility(EComponentMobility::Static);
	SetRootComponent(Root);
	static ConstructorHelpers::FObjectFinder<UStaticMesh> Cube(TEXT("/Engine/BasicShapes/Cube.Cube"));
	auto Block = [this, Root](const TCHAR* Name, FVector Centre, FVector Size)
	{
		UStaticMeshComponent* Part = CreateDefaultSubobject<UStaticMeshComponent>(Name);
		Part->SetupAttachment(Root);
		Part->SetStaticMesh(Cube.Object);
		Part->SetRelativeLocation(Centre);
		Part->SetRelativeScale3D(Size / 100.f);
		Part->SetCollisionProfileName(TEXT("BlockAll"));
		Part->SetMobility(EComponentMobility::Static);
	};
	auto Label = [this, Root](const TCHAR* Name, FVector Location, const TCHAR* Text)
	{
		UTextRenderComponent* Part = CreateDefaultSubobject<UTextRenderComponent>(Name);
		Part->SetupAttachment(Root);
		Part->SetRelativeLocation(Location);
		Part->SetRelativeRotation(FRotator(0.f, 180.f, 0.f));
		Part->SetText(FText::FromString(Text));
		Part->SetWorldSize(18.f);
		Part->SetHorizontalAlignment(EHTA_Center);
		Part->SetTextRenderColor(FColor::Black);
	};

	Block(TEXT("MeasuredFloor"), FVector(0, 0, -10), FVector(2000, 1600, 20));
	// Clear dimensions exclude posts/header. Both openings have 20 cm nominal head margin.
	Block(TEXT("WideLeftPost"), FVector(250, -290, 100), FVector(30, 40, 200));
	Block(TEXT("WideRightPost"), FVector(250, -150, 100), FVector(30, 40, 200));
	Block(TEXT("WideHeader"), FVector(250, -220, 215), FVector(30, 180, 30));
	Label(TEXT("WideLabel"), FVector(230, -220, 255), TEXT("100 x 200 cm clear"));
	Block(TEXT("NarrowLeftPost"), FVector(250, 160, 100), FVector(30, 40, 200));
	Block(TEXT("NarrowRightPost"), FVector(250, 280, 100), FVector(30, 40, 200));
	Block(TEXT("NarrowHeader"), FVector(250, 220, 215), FVector(30, 160, 30));
	Label(TEXT("NarrowLabel"), FVector(230, 220, 255), TEXT("80 x 200 cm clear"));
	Block(TEXT("CameraTestWall"), FVector(800, 0, 150), FVector(20, 1000, 300));
	Label(TEXT("WallLabel"), FVector(785, 0, 250), TEXT("Wall / third-person camera check"));
	Block(TEXT("MetreReference"), FVector(-150, -500, 50), FVector(100, 100, 100));
	Label(TEXT("MetreLabel"), FVector(-210, -500, 135), TEXT("1 metre cube"));
	Block(TEXT("ReachReference"), FVector(520, -220, 100), FVector(10, 10, 10));
	Label(TEXT("ReachLabel"), FVector(510, -220, 140), TEXT("Reference only - no interaction yet"));
	Label(TEXT("FixtureTitle"), FVector(-400, 0, 250), TEXT("3.1 PLAYER / SCALE LAB\nProvisional fit dimensions - not ship geometry"));
}
