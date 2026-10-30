# Canvas styling and geometry

Read only when creating/changing layout or annotations. Existing accepted geometry is preserved during unrelated processing edits.

APPEARANCE CHOICE
- Before creating a new Data Flow, ask whether its ClicData canvas uses light mode or dark mode. Do not generate the final styled flow until the choice is known. Reuse an explicit theme already supplied for the current task; ask again for a new task if its theme is unknown.
- Use light mode for canonical teaching examples, explicitly labeled as such. The historical cosmetic demo used dark mode; that does not choose the theme of a new task.
- Dark mode: description/body/note Font.Color rgba(240, 240, 240, 1); panel Border.Color rgba(180, 180, 180, 1). Light mode: both use rgba(50, 50, 50, 1). Keep transparent description backgrounds, category fills at alpha 0.10 and contrasting header colors from the palette in both themes. Theme is a generation option, not an invented clipboard property.

CANVAS LAYOUT
- Center the entire node group horizontally within its panel, including groups with multiple nodes. Preserve relative spacing and branch arrangement. Reserve the header and description areas, then center the group vertically within the remaining processing area with equal top/bottom padding. Centering the processing area does not mean centering nodes over the description. Enlarge panels when necessary; avoid overlaps.
- For estimated full shaded node footprint width 119, group width is max(Left+119)-min(Left). Shift all nodes by panel.Left+(panel.Width-groupWidth)/2-min(Left). Use the equivalent bounding-box calculation vertically within the reserved processing area. Editor node sizes may differ; verify centering after import.
- Arrange processing chains left to right.
- Align parallel source paths and keep related helper branches close above or below their consumers.
- Use top/bottom ports for nearby supporting branches where appropriate. Preserve existing ports unless rerouting is requested or necessary.
- Keep spacing compact but readable. Allow more room for annotations, long labels and section boundaries.
- Use separate, non-overlapping section panels with consistent padding.
- Negative coordinates are valid; do not reposition a supplied flow merely to make coordinates positive.
- Treat any estimated node dimensions or spacing values as layout aids, not guaranteed editor dimensions.
- Check that nodes, titles and description labels do not overlap. Actual connector routing and text wrapping require editor verification.

DEFAULT SECTION STYLING — ALL FUTURE DATA FLOW PROJECTS
Use annotation-templates.json and the current palette below. Read the template file only when constructing annotations. Each meaningful section has:
1. A background panel with an empty Text value.
2. A full-width title label at the top, normally 51 canvas units high.
3. A separate transparent description label below the title and above the nodes.
4. Additional explanatory text below the nodes only when needed.

Use:
- Background panels: matching section color at alpha 0.10, enabled border per the selected theme, shadow disabled.
- Title labels: opaque section color for BOTH Background.Color and Font.Background.Color; contrasting Font.Color per the palette below; border and shadow disabled.
- Description labels: Background.Color and Font.Background.Color rgba(50, 50, 50, 0); Font.Color per the selected theme; border and shadow disabled.
- Use the documented label structure. Do not invent font-size, alignment or z-index properties or claim exact centered rendering without editor evidence.
- Serialize background panels before processing nodes and labels afterward, following the documented serialization structure. Verify actual layering in the editor.

Observed annotation property classes:
- DataFlowAnnotationBackgroundPanelProperties:#Infinis.DataFlows
- DataFlowAnnotationLabelProperties:#Infinis.DataFlows

Use their complete property structure from annotation-templates.json, adapting IDs, positions, dimensions, text and palette colors. Class names alone are not sufficient to construct an annotation. Keep template adaptations distinct from editor-tested exports.

TRANSFORMATION COLOR PALETTE
Match the ClicData node categories in the user-supplied 2026-10-21 screenshot. RGB values were sampled from the category stripes; panel alpha 0.10 and header styling are our annotation convention, not editor defaults. This replaces the earlier purpose-based palette, including the input/output-only green restriction. Tables also include Table Merge and Table Fusion; Combine belongs to orange Calculations & Lookup. Group Rows is blue; JSON-to-Rows is cyan. Purple identifies annotation-only sections, not every panel simply because it is an annotation object.

For mixed sections, use the dominant processing category and describe the steps; split sections when helpful. Use `rgba(50, 50, 50, 1)` title text for green, yellow and cyan headers, and white for blue, orange, red, purple and neutral headers. Keep descriptive titles so meaning does not depend on color. Preserve the existing panel/title/description structure, enabled panel border and disabled shadows.

| Section category | Opaque header RGBA | Panel RGBA | Header text |
| --- | --- | --- | --- |
| Tables: input, output, Table Merge, Table Fusion | `rgba(112, 173, 71, 1)` | `rgba(112, 173, 71, 0.10)` | dark |
| Filter & Grouping: filters, Group Rows, Pivot, Unpivot | `rgba(68, 114, 196, 1)` | `rgba(68, 114, 196, 0.10)` | white |
| Calculations & Lookup: calculations, aggregates, lookup, Join, Combine | `rgba(197, 91, 18, 1)` | `rgba(197, 91, 18, 0.10)` | white |
| Data Cleaning: selection, cleanup, types, normalization, deduplication | `rgba(255, 192, 2, 1)` | `rgba(255, 192, 2, 0.10)` | dark |
| AI & Processing: AI, language, sentiment, geocoding, IP location | `rgba(196, 68, 68, 1)` | `rgba(196, 68, 68, 0.10)` | white |
| Parsing & Splitting: text/JSON to columns or rows | `rgba(0, 176, 240, 1)` | `rgba(0, 176, 240, 0.10)` | dark |
| Designer & Annotations: annotation-only sections | `rgba(90, 51, 148, 1)` | `rgba(90, 51, 148, 0.10)` | white |
| Other / administrative (fallback) | `rgba(50, 50, 50, 1)` | `rgba(50, 50, 50, 0.10)` | white |

## Editor grid evidence — 2026-10-21

The latest user-supplied editor export supersedes the earlier 10px assumption. Every supplied position and annotation dimension is a multiple of **17 canvas units**: panel 289×272 (17×16 grid steps), header 289×51 (17×3), description 255×68 (15×4), and 17-unit description insets. Even original/desired sizes use the same grid. This strongly supports a 17-unit grid for this instance; zoomed screenshot pixels do not equal serialized canvas units, and one export does not establish all editor versions.

Use multiples of 17 for new layout positions and annotation sizes, with equal widths for matching sections and 51-unit headers. Center using the whole shaded node footprint. In this centered sample, the implied node width is 289−2×(2941−2856)=119 (7×17); use 119×68 as the working node-footprint estimate, with height still estimated from the screenshot. Do not add Width/Height properties to processing nodes. For chains, keep a shared bounding box and symmetric margins; choose panel width parity to allow exact centering on the grid. If rounding is unavoidable, the maximum nearest-grid offset is 8.5 units. Preserve supplied geometry during unrelated edits.

## Caption placement — 2026-10-21

After positioning the nodes, preserve their accepted coordinates and place the description midway between header and processing group. For any number of nodes or branches, groupTop = min(node.Top); groupLeft = min(node.Left); groupRight = max(node.Left + fullNodeWidth). Center the group horizontally using (groupLeft + groupRight)/2, never by averaging individual node centers. For the caption, gapTop = header.Top + header.Height, gapBottom = groupTop and caption.Top = (gapTop + gapBottom − caption.Height)/2. The empty gaps above and below the caption must match. On the 17-unit grid, choose caption.Height with the same grid-step parity as the gap so this division stays on-grid; retain enough height for the text. Use equal 17-unit horizontal insets. If text cannot fit, enlarge/re-layout the section explicitly rather than overlap or silently clip it. This caption adjustment must not move nodes, headers or panels.

## Styling utility scope

Use `python3 scripts/style_flow.py input.json --theme light --out output.json` (or dark) only when layout changes are authorized. This utility snaps geometry and can move processing nodes; it is unsuitable for annotation-only or caption-only edits that must preserve those coordinates. Its `position_captions` function adjusts captions while leaving processing nodes untouched; check requested preservation explicitly. Template dimensions/positions are illustrative and must be adapted to the 17-unit grid and current 51-unit headers.


## Optional step: table names for clearer annotations — 2026-10-28

If readable source/output table names or preferred business labels are not already supplied or available in retrieved metadata, optionally ask:

“Optional — you can share the source/output table names or preferred labels to make the section titles and descriptions clearer. You can skip this; I’ll use the available names.”

This is a naming aid, not a prerequisite for generation. Do not ask again when names are already known, request extra data solely for cosmetic naming, or block work waiting for this optional answer. Use supplied names to explain the source and processing purpose concisely. If skipped, use available metadata or neutral descriptive labels without inventing business meaning. Annotation labels do not replace verified dataset/column bindings or authorize changing resource names or destinations.
