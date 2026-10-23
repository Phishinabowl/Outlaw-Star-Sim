# Game Development Glossary

Plain-language reference for terms introduced during this project. Started 2026-10-11; expand it as
new concepts come up. You do not need to memorize this before continuing.

Definitions explain concepts; they do not select settings or authorize implementation. The
[Phase 1.4 plan](../implementation/phase-1-4-architecture-asset-validation-draft.md) owns our choices
and learning experiments. Version-specific support must be checked before use.

## Find A Topic

- [How the graphics pieces fit together](#how-the-graphics-pieces-fit-together)
- [Rendering, APIs and tracing](#rendering-apis-and-tracing)
- [Lighting and reflections](#lighting-and-reflections)
- [Shadows](#shadows)
- [Materials and PBR](#materials-and-pbr)
- [Textures, detail and distance](#textures-detail-and-distance)
- [Anti-aliasing and reconstruction](#anti-aliasing-and-reconstruction)
- [Camera and image effects](#camera-and-image-effects)
- [Performance and measurement](#performance-and-measurement)
- [Shaders, pipelines and caches](#shaders-pipelines-and-caches)
- [Blender, geometry and asset handoff](#blender-geometry-and-asset-handoff)
- [Unreal, gameplay and input](#unreal-gameplay-and-input)
- [Files, builds and version control](#files-builds-and-version-control)
- [MCP and development automation](#mcp-and-development-automation)
- [Common mix-ups](#common-mix-ups)
- [Adding to this glossary](#adding-to-this-glossary)

Use your Markdown viewer's search for abbreviations such as GI, TSR, PBR or RHI.

## How The Graphics Pieces Fit Together

Think about a ceiling light shining onto an engineering cylinder:

| Piece | Question it answers | Ship example |
| --- | --- | --- |
| Geometry | What shape is there? | Cylinder, handle and surrounding walls. |
| Material | How does its surface respond to light? | Painted casing, exposed metal and rubber grip. |
| Lighting | Where does illumination come from? | Ceiling light, screen glow and light bouncing off walls. |
| Shadows | What blocks that light? | Cylinder casts a changing shadow as it extends. |
| Renderer | How are those calculations organized? | Deferred rendering gathers surface information before lighting it. |
| Graphics API | How does the engine send work to the GPU? | DirectX 12 or Vulkan. |
| Anti-aliasing / reconstruction | How are pixels made stable and smooth? | Reduce jagged handle edges and shimmer during movement. |
| Image effects | How is the camera image presented? | Exposure, bloom, depth of field and motion blur. |

This is a conceptual map, not an exact rendering-pass order. Several techniques cooperate or overlap.

Our starting candidate is **DX12 + deferred + Lumen + Virtual Shadow Maps + native-resolution TSR**.
See the [accepted rendering direction](../implementation/phase-1-4-architecture-asset-validation-draft.md#initial-rendering-and-anti-aliasing-direction--accepted-2026-10-11)
for the current contract rather than treating this glossary as another settings registry.

## Rendering, APIs And Tracing

| Term | Plain-language meaning |
| --- | --- |
| Rendering | Turning a scene, its materials, lights and camera into an image. |
| Real-time rendering | Producing images fast enough to respond continuously while you play. |
| Offline rendering | Spending more time per image for reference pictures or cinematics. |
| Rasterization | Projecting geometry onto the pixel grid to determine visible surfaces. Can cooperate with ray tracing. |
| Forward renderer | Calculates surface shading as objects are drawn. Unreal desktop MSAA is available here. |
| Deferred renderer | Records surface information in buffers, then uses it to calculate lighting. Our planned Lumen path. |
| G-buffer | The deferred renderer's collection of surface information, such as normals and material properties. |
| Graphics API / backend | Interface used to submit graphics work to the GPU. DirectX 12 and Vulkan are alternatives. |
| RHI — Rendering Hardware Interface | Unreal's abstraction over graphics backends, helping engine code work across APIs. |
| Shader | A program used for rendering work, including material appearance and image processing. |
| Shader compilation | Preparing shader code for a platform/configuration. Related to, but distinct from, GPU/driver pipeline preparation; see [shaders and caches](#shaders-pipelines-and-caches). |

In Unreal's desktop paths, forward/MSAA and deferred/Lumen are different supported combinations.
Changing DX12 to Vulkan does not inherently change forward to deferred or vice versa.
[Epic's rendering-path comparison](https://dev.epicgames.com/documentation/en-us/unreal-engine/supported-features-by-rendering-path-for-desktop-with-unreal-engine).

| Term | Plain-language meaning |
| --- | --- |
| Ray tracing | Following rays through a scene to find intersections; useful for reflections, shadows and lighting. |
| Hardware ray tracing | Accelerates ray-intersection work using supported GPU hardware. |
| Software ray tracing | Computes tracing without relying on dedicated ray-tracing hardware; may use approximate scene representations. |
| Path tracing | Samples chains of light interactions to estimate the finished image. Our planned use is reference rendering. |
| Samples / noise / denoising | Limited ray samples produce noise; more samples or a denoiser improve the image, with their own costs/artifacts. |
| Hybrid rendering | Combines approaches—for example, rasterized surfaces with ray-traced reflections. |
| RTX | NVIDIA's technology branding; not one universal rendering switch. |
| RTX Remix | NVIDIA's remastering toolkit for compatible existing games. Context for learning, not a required tool for our new Unreal game. |

Vulkan hardware ray tracing is marked experimental in Epic's current documentation. A powerful GPU
does not establish that a particular engine/plugin/backend combination works.
[Epic hardware ray tracing](https://dev.epicgames.com/documentation/unreal-engine/hardware-ray-tracing-in-unreal-engine),
[path tracer](https://dev.epicgames.com/documentation/unreal-engine/path-tracer-in-unreal-engine),
[NVIDIA RTX Remix overview](https://docs.omniverse.nvidia.com/kit/docs/rtx_remix/latest/docs/introduction/intro-overview.html).

## Lighting And Reflections

| Term | Plain-language meaning / example |
| --- | --- |
| Direct lighting | Light reaching a surface directly from a source: ceiling light illuminating the floor. |
| Indirect / bounced lighting | Light reaching a surface after reflecting elsewhere: a lit red panel tinting nearby surfaces. |
| GI — Global Illumination | A system for estimating indirect illumination across the scene. |
| Dynamic lighting | Lighting that can respond during play, such as lights switching on and machinery moving. |
| Baked / precomputed lighting | Lighting calculated beforehand and stored for use later. Changes have limitations. |
| Lightmass / lightmap | Unreal's baking system / texture containing precomputed lighting information. |
| Lumen | Unreal's dynamic GI and reflection system. It is not the entire renderer or the shadow method. |
| Diffuse reflection | Light scattered by a surface; contributes to its broadly visible appearance. |
| Specular reflection | More directional reflection, including shiny highlights and mirror-like views. |
| Screen-space technique | Uses information available in the current camera view; missing off-screen information can limit results. |
| SSR — Screen Space Reflections | Reflections reconstructed from visible scene information. |
| AO — Ambient Occlusion | Estimates local obstruction of ambient light, helping creases/corners feel grounded. Not a complete GI solution. |
| SSAO / GTAO / RTAO | Screen-space AO / Ground Truth Ambient Occlusion / ray-traced AO: different ways to estimate that obstruction. |
| Point / spot / rect / directional light | Light radiating outward / in a cone / from an area / in a common direction, like distant sunlight. |

For our learning fixture, compare direct light alone against bounced light and reflections with the
same camera. This makes the individual contributions easier to recognize.
[Epic Lumen overview](https://dev.epicgames.com/documentation/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine),
[post-process effects, including AO/reflections](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine).

## Shadows

| Term | Plain-language meaning |
| --- | --- |
| Shadow map | Depth information rendered from a light's viewpoint, used to decide whether a surface is blocked. |
| Conventional shadow maps | Traditional shadow maps whose resolution/settings need balancing against cost. |
| CSM — Cascaded Shadow Maps | Multiple shadow-map regions for a directional light, allocating detail across viewing distances. |
| VSM — Virtual Shadow Maps | Unreal allocates shadow-map detail in small pages where needed. Our initial candidate. |
| Hardware ray-traced shadows | Trace toward a light to determine blockage and area-light softness. Separate from enabling Lumen hardware tracing. |
| Distance-field shadows | Use approximate distance-to-surface volumes to estimate soft shadows; geometry support matters. |
| Contact shadows | Supplement nearby small shadow details, commonly using screen-space information. |
| Baked shadows | Stored results for precomputed lighting situations; not a complete solution for our moving mechanisms. |
| Penumbra / contact hardening | Partially shadowed soft edge / tendency for a shadow to be sharper near contact and softer farther away. |
| Shadow bias | Offset used to avoid erroneous self-shadowing; too much can detach a shadow from its object. |
| Shadow acne / peter-panning | Erroneous self-shadow speckles / shadows appearing detached from their caster. |

Compare the extending cylinder beneath a small light and a broad ceiling light. Keep light placement
consistent when comparing algorithms, then deliberately vary source size as a separate exercise.
[Epic shadowing overview](https://dev.epicgames.com/documentation/unreal-engine/shadowing-in-unreal-engine),
[Virtual Shadow Maps](https://dev.epicgames.com/documentation/unreal-engine/virtual-shadow-maps-in-unreal-engine).

## Materials And PBR

| Term | Plain-language meaning |
| --- | --- |
| Material | Rules and data describing a surface's appearance and light response. |
| PBR — Physically Based Rendering | Surface shading based on approximations of real light behavior; also useful for stylized art. |
| Base color / albedo | Surface color information before the final scene lighting is applied; treatment differs for metals. |
| Roughness | Microscopic surface irregularity: lower values give tighter reflections; higher values spread them out. |
| Metallic | Whether a surface behaves as metal. Painted metal usually has nonmetal paint over metal underneath. |
| Specular | Directional reflected light. In Unreal's common PBR workflow, roughness is usually the main control for changing highlight sharpness. |
| Normal / normal map | Surface direction / texture that changes the shading direction to suggest detail without adding its full geometry. |
| Emissive | Makes a surface appear to emit light. Visible glow and reliable illumination of neighbors are separate considerations. |
| Opacity / translucency | How opaque a surface is / rendering that allows light or a background to show through. |
| Refraction / IOR | Bending of light through a material / index of refraction controlling that bending. |
| Material instance | A reusable variation of a material, such as changing paint color or roughness. |

For the ship, bare metal, paint, glass and rubber should respond differently even under identical
lighting. A normal-map screw does not automatically become a real protrusion you can collide with.
[Epic PBR materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine).

## Textures, Detail And Distance

| Term | Plain-language meaning |
| --- | --- |
| Texture | Image/data sampled by a material: color, roughness, normals or other information. |
| Texture resolution / texel | Size of a texture image / one texture element, distinct from a final screen pixel. |
| UV mapping | Coordinates that tell the mesh which parts of a texture go where. |
| Mipmaps / mip chain | Progressively smaller versions of a texture, used when full detail is unnecessary. Help reduce shimmer and sampling cost. |
| Texture filtering | How samples are combined when a texture does not line up exactly with screen pixels. |
| Bilinear / trilinear filtering | Blend neighboring texels / also blend between mip levels. |
| Anisotropic filtering | Improves sampling of textures viewed at oblique angles, such as corridor floors. |
| Texture streaming / pool | Loading needed texture detail over time / memory budget used for streamed textures. |
| LOD — Level Of Detail | Uses a different detail level when appropriate; often a simpler mesh at distance. |
| Nanite | Unreal's virtualized geometry system, selecting fine geometry detail efficiently. Not a substitute for materials, lighting or collision. |
| Culling / view distance | Avoiding rendering unnecessary objects / controlling how far particular content is displayed. |

Higher-resolution textures can improve close-up detail but consume memory. Good mipmaps help the
same panel remain stable farther away. Graphics quality must not remove required controls or change
our simulation/collision behavior.
[Epic texture properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-properties?application_version=4.27)
(older reference for general concepts), [Nanite](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine).

## Anti-Aliasing And Reconstruction

| Term | Plain-language meaning |
| --- | --- |
| Aliasing / shimmer | Stair-stepped edges / unstable fine detail while moving. |
| AA — Anti-Aliasing | Reduces those sampling artifacts. |
| Spatial / temporal | Uses current-frame information / also uses information from earlier frames. |
| FXAA — Fast Approximate AA | Smooths detected edges in the finished frame; inexpensive but can soften detail. |
| MSAA — Multisample AA | Samples geometry coverage multiple times; does not fix every material/texture artifact. Unreal desktop forward only. |
| TAA — Temporal AA | Accumulates frame history to stabilize detail; can blur or ghost. |
| TAAU — Temporal AA Upsampling | TAA-based reconstruction to a larger output image. |
| TSR — Temporal Super Resolution | Unreal temporal reconstruction; can run at native input resolution or upscale. |
| Ghosting / disocclusion | Trails from inappropriate history / surfaces newly revealed by motion. |

[Epic anti-aliasing overview](https://dev.epicgames.com/documentation/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine),
[TSR](https://dev.epicgames.com/documentation/unreal-engine/temporal-super-resolution-in-unreal-engine).

| Term | Plain-language meaning |
| --- | --- |
| Native / internal / output resolution | Native uses matching input/output dimensions; internal is the rendered input, output is the delivered image. |
| Screen percentage | Rendering scale relative to output dimensions; record it instead of assuming a 1440p display means native rendering. |
| Upscaling | Constructing a higher-resolution output from a lower-resolution input. |
| Dynamic resolution | Changes internal resolution during play to manage rendering cost. |
| DLSS Super Resolution | NVIDIA AI reconstruction from lower-resolution input on supported hardware/integration. |
| DLAA — Deep Learning AA | NVIDIA AI anti-aliasing using native-resolution input. |
| Frame generation | Creates additional displayed frames; does not mean the simulation rendered that many fresh frames. |
| Ray reconstruction | NVIDIA AI reconstruction replacing certain ray-tracing denoisers in supported integrations. |

Native 1440p with TSR still uses AA. Our performance baseline disables resolution scaling and frame
generation; optional modes get their own results. Look at moving handles and cockpit text as well as
still images. [NVIDIA DLSS technologies](https://developer.nvidia.com/rtx/dlss).

## Camera And Image Effects

| Term | Plain-language meaning |
| --- | --- |
| Post-processing | Image treatments applied within the rendering pipeline. |
| DoF — Depth Of Field | Focus-related blur: sharp at the chosen focus distance, blur elsewhere. Not view distance. |
| Motion blur | Blur representing motion during an exposure; separate from AA ghosting. |
| Bloom | Glow spreading around bright image regions; does not itself light nearby objects. |
| Exposure / auto-exposure | Brightness adjustment / automatic adaptation between bright and dark scenes. |
| Tone mapping | Converts a wide range of rendered brightness into displayable values. |
| Color grading | Adjusts color and contrast for a visual look. |
| FOV — Field Of View | How wide an angle the camera sees; affects perceived scale and perspective. |

DoF and motion blur start OFF for gameplay. Exposure deserves attention during our dark-to-lit hangar
reveal so adaptation does not accidentally undermine it.
[Epic post-process effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine).

## Performance And Measurement

| Term | Plain-language meaning |
| --- | --- |
| FPS — Frames Per Second | Rate at which frames are produced or displayed; specify which when frame generation is active. |
| Frame time / budget | Time per frame / available time: 60 FPS is about 16.67 ms; 120 FPS about 8.33 ms. |
| Average / p95 / p99 | Overall average / frame-time thresholds containing 95% or 99% of sampled frames. Lower measured times at the same percentile are better. |
| Hitch / frame pacing | An unusually slow frame / consistency of delivery, which averages can hide. |
| CPU-bound / GPU-bound | CPU work / GPU work is limiting performance; lowering graphics settings may not fix a CPU bottleneck. |
| VRAM / RAM | GPU memory / system memory; both matter, and neither is disk space. |
| VSync / FPS cap | Synchronizing presentation to display refresh / limiting frame rate. Can obscure uncapped rendering capacity. |
| Input latency | Delay between input and its visible result. High displayed FPS alone does not establish low latency. |
| Profiling / trace | Measuring where time/resources go / recorded events used for analysis. |
| Unreal Insights / GPU profiler | Unreal tools for examining timing and resource use / investigating rendering pass costs. |
| Warm-up / cold run | Letting startup work and operating conditions settle / measuring a fresh start separately. A fresh process launch does not imply empty caches. |
| Scalability / quality preset | Grouped settings controlling visual cost and quality. Must preserve gameplay rules and usability. |

A five-minute cylinder/cockpit route with recorded settings tells us more than a single FPS screenshot.
The plan owns acceptance thresholds; this glossary does not set new ones.
[Epic profiling introduction](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine).

## Shaders, Pipelines And Caches

| Term | Plain-language meaning / example |
| --- | --- |
| Shader compilation | Converts shader programs into a platform-ready form. Unreal prepares required shader code during cooking for a packaged game. |
| Shader permutation | A shader variation for a particular set of features/settings; changing those can require different compiled code. |
| Graphics pipeline / PSO — Pipeline State Object | A prepared combination of shaders and rendering state, such as how a surface is drawn and blended. Both DX12 and Vulkan use pipeline concepts. |
| Pipeline compilation / creation | GPU/driver preparation of that combination. Can still cost time in a packaged game with cooked shaders. |
| PSO precaching | Predicts needed pipelines and prepares them ahead of use, instead of waiting for the first draw. |
| Bundled PSO cache | Shipped descriptions of needed pipeline combinations, used to prepare them early; not universal ready-made machine code for every GPU. |
| Cache hit / miss | Needed work is already available / must be created or retrieved. |
| Cache invalidation | Previously cached work is no longer usable—for example, after some code, settings or driver changes. |
| Shader/pipeline compilation stutter | Visible stall when preparation delays a needed frame. Not every hitch has this cause. |

Imagine full ignition first showing a new cockpit-screen effect: a missing pipeline can cause a hitch,
while the next ignition appears smooth. That is why we capture first-use and warm performance separately.
[Epic shader development](https://dev.epicgames.com/documentation/unreal-engine/shader-development-in-unreal-engine),
[PSO caching](https://dev.epicgames.com/documentation/unreal-engine/optimizing-rendering-with-pso-caches-in-unreal-engine),
[PSO precaching](https://dev.epicgames.com/documentation/unreal-engine/pso-precaching-for-unreal-engine).

| Cache / test term | What it means |
| --- | --- |
| DDC — Derived Data Cache | Unreal development cache for rebuildable processed asset data, including compiled shaders. Cooked games do not use the editor DDC. |
| GPU/driver pipeline cache | Retains hardware/driver-specific preparation results. Different role from an editor DDC or bundled PSO descriptions. |
| Warm cache | Relevant preparation has already happened; repeat runs may reuse it. |
| Cold cache | Relevant cached preparation is absent or unusable. State which cache is cold. |
| Cold launch | New game process; caches from an earlier run may still exist. |
| First-use test | Exercise content before that test route has prepared it through use; record existing cache conditions. |
| Startup preparation | Work before player control, timed separately from active play. |

Caches save repeated work but do not all serve the same purpose. We will use project-scoped test
recipes, not delete broad system or unrelated game caches. No cache has been changed by this glossary.
[Epic DDC documentation](https://dev.epicgames.com/documentation/unreal-engine/using-derived-data-cache-in-unreal-engine),
[project performance contract](../implementation/phase-1-4-architecture-asset-validation-draft.md#accepted-performance-measurement-contract--execution-pending).

## Blender, Geometry And Asset Handoff

| Term | Plain-language meaning / project use |
| --- | --- |
| Blender | Authoring tool for geometry, materials, animation and related content. Unreal runs the playable experience. |
| Mesh / vertex / edge / face | Surface geometry / point / connecting line / surface patch. |
| Transform / local space / world space | Position, rotation and scale / relative to an object or parent / relative to the scene. |
| Origin / pivot | Reference point for an object's transform. Place a hatch's rotation pivot at its hinge. |
| Applied transforms | Incorporating object transforms into its data; effects on export must be verified, not applied blindly. |
| Collision mesh | Shape used for physical blocking/interactions; can differ from the visible mesh. |
| Graybox / proxy | Simple geometry used to prove scale, traversal and mechanics before detailed art. |
| Clearance / motion envelope | Space for occupants/access / all space swept by moving equipment. |
| Rig / skeleton / skinning | Animation controls / bone hierarchy / how mesh vertices follow bones. |
| FBX / export / import / reimport | A handoff format / writing transferable data / bringing it into Unreal / updating an existing imported asset. |
| Handoff fixture | Small known-size test proving units, orientation, pivots and collision before repeated production. |

Our 1 m cube should arrive as 100 Unreal centimeters. That test proves the recipe, not that every ship
room fits. [Blender glossary](https://docs.blender.org/manual/en/latest/glossary/index.html),
[project handoff plan](../implementation/phase-1-4-architecture-asset-validation-draft.md).

## Unreal, Gameplay And Input

| Term | Plain-language meaning / project use |
| --- | --- |
| Unreal Engine / editor | Runtime/tooling framework / application used to build and inspect the game. |
| Project template | Preassembled starting content/settings/behavior; editable, not a permanent restriction on the finished game. |
| Blank C++ | Minimal template with a C++ foundation. Our selected starting point; engine components and Blueprints remain available. |
| First Person / Third Person template | Starting character/camera/content examples; neither automatically supplies all our player requirements. |
| C++ / Blueprint | Text-based compiled code / Unreal's visual scripting and content configuration system. Both can implement behavior; our ownership split is a project choice. |
| Module / plugin | Code unit in an Unreal project / packaged extension providing functionality. |
| Actor / component | Object placed or spawned in the world / reusable part supplying behavior or data. |
| Map / level | Scene containing world content. Planned Test Lab and Awakening serve different purposes. |
| Authority / presentation | State owner that decides what is true / visuals, sound and UI showing that truth. |
| State machine / prerequisite | Defined states and transitions / condition required before an action. |
| Command / query / event | Request a change / read current state / announce something happened. |
| Callback / lifecycle / reset | Work invoked later / creation-to-teardown behavior / restoring a new session's starting state. |
| Session ID | Identifies the current fresh run. Reset changes it so work from an earlier run cannot affect the new one; not a player/account ID. |
| Operation ID | Identifies one tracked action, such as an ignition sequence or seat lift. Results/callbacks must match the current operation as well as the session. |
| Duplicate / conflicting request | Repeated attempt to start the same active action / action incompatible with current work or state. Neither should create competing sequences. |
| Stale callback | Delayed result from work that was reset, cancelled or replaced. Must not update current state just because it eventually arrives. |
| UI / HUD | User interface broadly / information displayed during gameplay. |
| Enhanced Input | Unreal system separating logical actions from device bindings and contextual input rules. |
| Input action / mapping context | Meaning such as Interact / bindings active in a situation such as exploration or seated use. |
| Focus / dead zone | Which interface receives input / ignored small controller-axis movement. |
| XInput / Steam Input / DS4Windows / vJoy | Controller API / input translation ecosystem / controller translation software / virtual joystick driver. Different layers, not synonyms. |

For our sim, a keyboard click or future controller button requests the same engineering action;
neither gets its own readiness rules. Actual device/backend combinations require testing.
[Epic Enhanced Input](https://dev.epicgames.com/documentation/unreal-engine/enhanced-input-in-unreal-engine),
[project input/ownership plan](../implementation/phase-1-4-architecture-asset-validation-draft.md).

**Template choice and starting-code choice are separate:** Blank/First Person/Third Person describes
the starting experience; C++/Blueprint describes how starting code is supplied. We chose Blank C++
to prove the minimal build first, then add our player at Phase 3.1. We can learn from character
templates without importing all their content or inventing our own engine.
[Epic templates reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-templates-reference).

For example, a seat-lift completion from session A must be ignored after resetting to session B.
Even within session B, a cancelled operation's late result must not complete its replacement.
The [session/operation contract](../implementation/phase-1-4-architecture-asset-validation-draft.md#session-and-operation-identity--accepted-2026-10-11)
owns our rules; tracking IDs do not require networking or change each action's interruption behavior.

### Asset Name Prefixes

These prefixes help identify the kinds of assets you see in an Unreal project or packaged-content
inspection. They are naming conventions, not what determines the underlying file's type.

| Prefix / example | What it identifies |
| --- | --- |
| `SM_EngineeringCylinder` | Static mesh: visible geometry for the cylinder. A static mesh can still move as a rigid object; it does not mean permanently fixed in place. |
| `BP_EngineeringCylinder` | Blueprint: configured object/behavior that may reference the cylinder mesh and materials. |
| `M_PaintedMetal` | Material: surface appearance rules. |
| `MI_PaintedMetal_Red` | Material instance: variation of the parent material. |
| `IA_Interact` | Input action: logical player action, separate from its physical key/button. |

These can describe different pieces of the same object, rather than duplicate models. The accepted
initial naming convention and folder layout live in the
[Phase 1.4 plan](../implementation/phase-1-4-architecture-asset-validation-draft.md#folder-subdivisions-and-initial-naming--accepted-2026-10-11).
[Epic's naming reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects).

## Files, Builds And Version Control

| Term | Plain-language meaning |
| --- | --- |
| .uproject / .uasset / .umap / .blend | Unreal project descriptor / Unreal asset / Unreal map / editable Blender source file. |
| Source asset / export / generated output | Editable original / handoff representation / rebuildable output such as a cache. |
| Git / GitHub | Version-history system / hosting and collaboration service for repositories. |
| Git LFS — Large File Storage | Stores designated large file contents separately while Git tracks pointers. Does not make binary files easy to merge. |
| LFS pointer / payload | Small reference stored in Git / actual binary content retrieved through LFS. An unresolved pointer is not a usable Blender or Unreal asset. |
| .gitattributes | Repository rules assigning handling to file paths, including LFS tracking. Separate from `.gitignore`, which controls normal addition of untracked files. |
| Handoff manifest / recipe | Record linking source, export and imported asset revisions / instructions and settings used to reproduce the handoff. |
| Known-good checkpoint / rollback | Recoverable version saved before a risky change / restoring the affected earlier state while preserving unrelated edits. |
| Fresh-checkout proof | Retrieve a recorded revision into a separate checkout and verify its real binary contents and test assets work without relying on the original working folder. |
| .gitignore | Excludes matching untracked files from normal Git addition; does not untrack already committed files. |
| Build / cook / package | Compile code / prepare content for the platform / assemble a runnable distribution. |
| Development / Shipping build | Build configurations emphasizing development diagnostics / distribution; costs and capabilities can differ. |
| Standalone packaged proof | Run the actual package outside the editor; missing content/dependencies can appear only here. |
| FModel | Inspection/extraction tool for supported packaged Unreal content. Not needed to author our source assets. |

Our source episodes/settei are research inputs, not game assets. Git LFS does not authorize their
publication. [Epic packaging overview](https://dev.epicgames.com/documentation/unreal-engine/packaging-your-project),
[project asset policy](../implementation/phase-1-4-architecture-asset-validation-draft.md).

For example, keep a cylinder's editable `.blend`, designated `.fbx`, Unreal mesh and import recipe
linked. If a reimport moves its pivot or closes its collision opening, restore the affected known-good
set and fix the recipe on the small fixture before applying it across the ship. Keeping only the
export would lose part of the editable authoring workflow.

The [accepted storage/recovery contract](../implementation/phase-1-4-architecture-asset-validation-draft.md#asset-storage-and-recovery-contract--accepted-2026-10-23)
assigns Blender originals, designated FBX exports and owned Unreal assets/maps to planned LFS storage;
text remains in ordinary Git, generated outputs are ignored, and reference media stays local-only.
This is a planning decision, not evidence that LFS is configured or asset recovery has been tested.
[GitHub's LFS explanation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
and [tracking configuration](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage)
explain the pointer and repository-rule mechanics.

## MCP And Development Automation

| Term | Plain-language meaning |
| --- | --- |
| MCP — Model Context Protocol | Protocol exposing tools/data to an AI client; here, optional editor automation. |
| Client / server / connector | Requests tools / provides them / integration connecting the systems. |
| Blender bridge / add-on | Separate MCP-facing process / Blender-side extension executing scene operations. |
| Transport: stdio / HTTP / TCP | Connection through process input/output / web-style messaging / a network byte stream. Different links can use different transports. |
| Loopback / localhost | Connection back to the same machine. Limits network exposure, not what executing code can access. |
| Non-admin | Process without elevated administrator privileges; still has ordinary account permissions. |
| Sandbox / VM | Restricted execution environment / virtual machine. Isolation depends on actual configuration. |
| Checkpoint / rollback | Recoverable saved state / restoring an earlier state after a failed experiment. |
| Pilot | Small bounded trial proving connection, usefulness and recovery before adoption. |

Our current direction is local, on-demand editor pilots; Sandbox work is deferred. MCP is not a
playable-game dependency. [Editor automation contract](../architecture/editor-automation.md).

## Common Mix-Ups

- **Vulkan versus deferred:** API choice versus renderer organization; separate decisions.
- **Lumen versus ray-traced shadows:** GI/reflections versus blockage of direct light; separate controls.
- **PBR versus ray tracing:** surface response versus tracing technique; PBR also works with rasterization.
- **Native versus AA off:** native describes input/output size; native images can still use AA.
- **DLAA versus DLSS Super Resolution:** native-input AA versus lower-input-resolution reconstruction.
- **Frame generation versus simulation speed:** additional displayed images do not advance our revival timer faster.
- **DoF versus view distance:** focus blur versus how far content is displayed.
- **Mipmaps versus mesh LOD:** texture detail versus geometry detail.
- **Bloom versus illumination:** visible glow versus actual light reaching nearby surfaces.
- **Visual geometry versus collision:** an object looking solid does not prove its physical blocking shape.
- **Tool success versus playtest proof:** successful execution does not establish readable visuals or good controls.
- **Shader compilation versus pipeline compilation:** cooked shader code does not eliminate all GPU/driver pipeline preparation.
- **Cold launch versus cold cache:** closing and reopening a game may preserve cached work.

## Adding To This Glossary

Add a term when it appears in a design discussion or test—not every possible engine term at once.
Use the full name, a short plain-language definition, an XGP example where helpful, and any important
confusion/compatibility note. Put it in the relevant category and link primary documentation for
version-sensitive details. Keep actual decisions in the implementation plan and link there rather
than maintaining competing settings lists. Correct or refine explanations as hands-on work teaches us more.
