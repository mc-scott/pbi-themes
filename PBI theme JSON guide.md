# JSON theme readme

## name
Metadata specifying the name of the theme

## dataColors
Up to 8 colours specified in an array `["...", "..."]` in hexadecimal format

## firstLevelElements 
Labels background color (when outside data points), trend line color, textbox default color, table and matrix values and totals font colors, data bars axis color, card data labels, gauge callout value color, KPI goal color, KPI text color, slicer item color (when in focus mode), slicer dropdown item font color, slicer numeric input font color, slicer header font color, scatter chart ratio line color, line chart forecast line color, map leader line color, filter pane and card text color

## secondLevelElements
“Light” secondary text classes, label colors, legend label color, axis label color, table and matrix header font color, gauge target and target leader line color, KPI trend axis color, slicer slider color, slicer item font color, slicer outline color, line chart hover color, multi-row card title color, ribbon chart stroke color, shape map border color, button text font color, button icon line color, button outline color

## thirdLevelElements
Axis gridline color, table and matrix grid color, slicer header background color (when in focus mode), multi-row card outline color, shape fill color, gauge arc background color, applied filter card background color, disabled button outline color

## fourthLevelElements
Legend dimmed color, card category label color, multi-row card category labels color, multi-row card bar color, funnel chart conversion rate stroke color, disabled button text font color, disabled button icon line color

## background
Labels background color (when inside data points), slicer dropdown items background color, donut chart stroke color, treemap stroke color, combo chart background color, button fill color, filter pane and available filter card background color

## secondaryBackground
Table and matrix grid outline color, shape map default color, ribbon chart ribbon fill color (when match series option is turned off), when background is not set to FFFFFF, the disabled button fill color, and the disabled button outline color
...

## tableAccent
This element overrides the table and matrix grid outline color

## textClass
**Generic text attributes**

### callout
...

### title
...

### header
...

### label
...

### largeTitle
Visual title

### largeLabel
Multi-row card data label

### smallLabel
Reference line labels, slicer data range labels, slicer numeric input text style, slicer search box, key influencers influencer text

### semiboldLabel
Key influencers profile text

### boldLabel
Matrix subtotals, matrix grand totals, table totals

### lightLabel
Legend text, button text, category axis labels, funnel, chart data labels, funnel chart conversion rate labels, gauge target, scatter chart category label, slicer items

### largeLightLabel
Card category labels, gauge labels, multi-row card category labels

### smallLightLabel
Data labels, value axis labels

## visualStyles
**High level visual style.  You can specify a format element once only in a theme file and nonetheless see it applied to *any* visual that supports it. You can subsequently overwrite or extend these common attributes at the level of each individual visual if you so wish**

### title
Corresponds to the Title subsection of the Title section

### subTitle
Corresponds to the Subtitle subsection of the Title section

### divider
Corresponds to the Spacing subsection of the Title section

### lockAspect
Corresponds to the Lock aspect subsection of the Properties section

### background
Corresponds to the Background subsection of the Effects section

### border
Corresponds to the Border subsection of the Effects section

### dropShadow
Corresponds to the Shadow subsection of the Effects section

### visualTooltip
Corresponds to the Tooltips section

### visualHeader
Corresponds to the Icons subsection of the Header Icons section

### visualHeaderTooltip
Corresponds to the Help Tooltip subsection of the Header Icons section
**Formatting for shared (or common) elements**

### categoryAxis
X axis

### valueAxis
Y axis

### labels
Data labels

### plotArea
The plot area

### legend
