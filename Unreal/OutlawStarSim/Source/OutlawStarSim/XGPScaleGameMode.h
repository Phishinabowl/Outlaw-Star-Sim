#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "XGPScaleGameMode.generated.h"

/** Assigned only to the development scale map; preserves the neutral proof baseline. */
UCLASS()
class OUTLAWSTARSIM_API AXGPScaleGameMode : public AGameModeBase
{
	GENERATED_BODY()

public:
	AXGPScaleGameMode();
};
