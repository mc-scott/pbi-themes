"""
Script to generate a json blob using global variables for use as 
a Power BI theme
"""

from pathlib import Path
from datetime import datetime

import json
import yaml

# set downloads path
DOWNLOADS_PATH = str(Path.home() / "Downloads")

# open config file
with open("config.yaml", "r", encoding="utf-8") as f:
    config = list(yaml.safe_load_all(f))

# set variables to alter json theme
NAME = "python-generated-theme"
VISUAL_BACKGROUND = "#F2F2F2"  #EFF5F6
TITLE_TEXT_COLOUR = "FFFFFF"
TEXT_COLOUR = "#3D4E57"

# set theme from yaml config file
# tpr = 0; tableau = 1
THEME = 0

FONT = config[THEME]["font"]
PAGE_BACKGROUND = config[THEME]["page"]["background"]
PAGE_BACKGROUND_TRANSPARENCY = config[THEME]["page"]["transparency"]
COLOUR_PALETTE = config[THEME]["palette"]
TOOLTIP_TRANSPARENCY = config[THEME]["tooltip_transparency"]

now = datetime.now().strftime("%Y-%m-%d-%H%M%S") # remove HMS when finished prototyping

# create json blob
json_blob = {
    "name": f"{NAME}-{now}",
    "$schema": "https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/refs/heads/main/Report%20Theme%20JSON%20Schema/reportThemeSchema-2.138.json",
    "dataColors": COLOUR_PALETTE,
    "firstLevelElements": COLOUR_PALETTE[9],
    "secondLevelElements": COLOUR_PALETTE[3], 
    "thirdLevelElements": "#F3F2F1",
    "fourthLevelElements": "#B3B0AD",
    "background": VISUAL_BACKGROUND,
    "secondaryBackground": "#C8C6C4",
    "tableAccent": COLOUR_PALETTE[0],
    "good": "#1AAB40",
    "neutral": "#D9B300",
    "bad": "#D64554",
    "maximum": "#118DFF",
    "center": "#D9B300",
    "minimum": "#DEEFFF",
    "null": "#FF7F48",
    "textClasses": {
        "callout": {
            "fontSize": 45,
            "fontFace": FONT,
            "color": "#252423"
        },
        "title": {
            "fontSize": 18,
            "fontFace": FONT,
            "color": "#252423"
        },
        "header": {
            "fontSize": 12,
            "fontFace": FONT,
            "color": "#252423"
        },
        "label": {
            "fontSize": 10,
            "fontFace": FONT,
            "color": "#252423"
        },
        "largeTitle": {
            "fontSize": 14,
            "fontFace": FONT,
            "color": "#808080"
       },
       "largeLabel": {
            "fontSize": 12,
            "fontFace": FONT,
            "color": "#808080"
       },
       "smallLabel": {
            "fontSize": 8,
            "fontFace": FONT,
            "color": "#949494"
       },
       "semiboldLabel": {
            "fontSize": 8,
            "fontFace": FONT,
            "color": "#808080"
       },
       "boldLabel": {
            "fontSize": 8,
            "fontFace": FONT,
            "color": COLOUR_PALETTE[0]
       },
       "lightLabel": {
            "fontSize": 8,
            "fontFace": FONT,
            "color": "#949494"
       },
       "largeLightLabel": {
            "fontSize": 12,
            "fontFace": FONT,
            "color": "#949494"
       },
       "smallLightLabel": {
            "fontSize": 8,
            "fontFace": FONT,
            "color": "#949494"
       }
    },
    "visualStyles": {
        "*": {
            "*": {
                "title": [{
                    "show": True,
                    "heading": "Heading2",
                    "fontColor": {"solid": {"color": "#FFFFFF"}},
                    "background": {"solid": {"color": COLOUR_PALETTE[0]}},
                    "alignment": "center",
                    "fontSize": 14,
                    "fontFamily": FONT,
                    "bold": True,
                    "italic": False,
                    "underline": False,
                    "titleWrap": True
                    }],
                "subTitle": [{
                    "show": True,
                    "heading": "Heading3",
                    "fontColor": {"solid": {"color": "#FFFFFF"}},
                    "background": {"solid": {"color": COLOUR_PALETTE[0]}},
                    "alignment": "center",
                    "fontSize": 12,
                    "fontFamily": FONT,
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "titleWrap": True
                    }],
                "divider": [{
                    "show": True,
                    "color": {"solid": {"color": VISUAL_BACKGROUND}},
                    "style": "solid",
                    "width": 2,
                    "ignorePadding": True
                    }],
                "spacing": [{
                    "customizeSpacing": True,
                    "spaceBelowTitle": 3,
                    "spaceBelowSubTitle": 3,
                    "spaceBelowTitleArea": 2
                    }],
                "lockAspect": [{
                    "show": False
                        }],
                "background": [{
                    "show": True,
                    "color": {"solid": {"color": VISUAL_BACKGROUND}},
                    "transparency": 15
                        }],
                "border":   [{
                    "show": True,
                    "color": {"solid": {"color": VISUAL_BACKGROUND}},
                    "radius": 5
                    }],
                "dropShadow":   [{
                    "show": True,
                    "color": {"solid": {"color": "#424242"}},
                    "position":"Outer",
                    "preset":"BottomRight"
                    }],
                "visualHeaderTooltip":[{
                    "type": "Default",
                    "titleFontColor":{"solid":{"color": COLOUR_PALETTE[1]}},
                    "fontSize": 12,
                    "fontFamily": FONT,
                    "background":{"solid":{"color": TEXT_COLOUR}},
                    "transparency": TOOLTIP_TRANSPARENCY,
                    "bold": False,
                    "italic": True,
                    "underline": False
                        }],
                "visualHeader": [{
                    "showVisualInformationButton": True,
                    "showVisualWarningButton": True,
                    "showVisualErrorButton": True,
                    "showDrillRoleSelector": True,
                    "showDrillToggleButton": True,
                    "showDrillUpButton": True,
                    "showDrillDownLevelButton": True,
                    "showDrillDownExpandButton": True,
                    "showPinButton": True,
                    "showFocusModeButton": True,
                    "showFilterRestatementButton": True,
                    "showSeeDataLayoutToggleButton": True,
                    "showOptionsMenu": True,
                    "showTooltipButton": True,
                    "showSmartNarrativeButton": False
                            }],
                "visualTooltip": [{
                    "show": True,
                    "type": "Default",
                    "fontSize": 12,
                    "fontFamily": "Consolas",
                    "bold": True,
                    "italic": False,
                    "underline": False,
                    "background": {"solid": {"color": TEXT_COLOUR}},
                    "transparency": TOOLTIP_TRANSPARENCY,
                    "fontColor": COLOUR_PALETTE[1],
                    "titleFontColor": {"solid": {"color": COLOUR_PALETTE[1]}},
                    "ThemeDataColor": {"solid": {"color": "#171717"}}
                            }],
                "general":  [{
                    "responsive": True,
                    "keepLayerOrder": True
                            }],
                "padding": [{
                    "left":3,
                    "right":3,
                    "top":3,
                    "bottom":3
                        }],
                "categoryAxis": [{
                    "show": True,
                    "axisScale": "Linear",
                    "position": "center",
                    "labelColor": {"solid": {"color": "#949494"}},
                    "fontFamily": FONT,
                    "fontSize": 10,
                    "showAxisTitle": True,
                    "titleFontSize": 10,
                    "titleFontFamily": FONT,
                    "titleColor": {"solid": {"color": "#949494"}},
                    "gridLineShow": True,
                    "gridLineColor":  {"solid": {"color": "#949494"}},
                    "gridLineThickness": 1,
                    "gridlineStyle": "Solid"
                    }],
                "valueAxis": [{
                    "show": True,
                    "position": "center",
                    "axisScale": "Linear",
                    "labelColor": {"solid": {"color": "#949494"}},
                    "fontFamily": FONT,
                    "fontSize": 10,
                    "showAxisTitle": True,
                    "titleFontSize": 10,
                    "titleFontFamily": FONT,
                    "titleColor": {"solid": {"color": "#949494"}},
                    "gridLineShow": True,
                    "gridLineColor":  {"solid": {"color": "#949494"}},
                    "gridLineThickness": 1,
                    "gridlineStyle": "Solid",
                    "axisStyle": "ShowTitleOnly"
                        }],
                "labels": [{
                    "show": True,
                    "labelPosition": "Auto",
					"labelDisplayUnits": 0, # value display units (0=Auto, 1=None, 1000=Thousands...)
                    "labelPrecision": 1,
                    "color": {"solid": {"color": "#030303"}},
                    "fontFamily": FONT,
                    "fontSize": 8,
                    "enableBackground": True,
                    "backgroundColor": {"solid": {"color": "#D6D6D6"}},
                    "backgroundTransparency": 15,
                    "backgroundRadius": 5
                    }],
                "plotArea": [{
                    "transparency": 10
                    }],
                "legend": [{
                    "show": True,
                    "showTitle": True,
                    "legendColor": {"solid": {"color": "#949494"}},
                    "fontFamily": FONT,
                    "fontSize": 10
                    }],
                "lineStyles": [{
                    "ShadedArea": True,
                    "strokeWidth": 1,
                    "lineStyle": "Solid",
                    "showMarker": True,
                    "markerShape": "Triangle",
                    "markerSize": 2,
                    "markerColor": {"solid": {"color": "#949494"}}
                    }] ,
                "slices": [{
                    "innerRadiusRatio": 20
                    }] ,
                "grid": [{
                    "gridVertical": False,
                    "gridVerticalColor": {"solid": {"color": COLOUR_PALETTE[2]}},
                    "gridVerticalWeight": 1,
                    "gridHorizontal": False,
                    "gridHorizontalColor": {"solid": {"color": COLOUR_PALETTE[2]}},
                    "gridHorizontalWeight": 1,
                    "textSize": 11,
                    "rowPadding": 2,
                    "outlineColor": {"solid": {"color": "#FFFFFF"}},
                    "outlineWeight": 1,
                    "imageHeight": 100
                    }],
                "columnHeaders": [{
                    "fontColor": {"solid": {"color": "#FFFFFF"}},
                    "backColor": {"solid": {"color": COLOUR_PALETTE[0]}},
                    "outline": "Frame",
                    "alignment": "Centre",
                    "wordWrap": True,
					"bold": True,
					"italic": False,
					"underline": False
                    }],
                "values": [{
                    "fontColorPrimary": {"solid": {"color": TEXT_COLOUR}},
                    "backColorPrimary": {"solid": {"color": "#F5F4F0"}},
                    "fontColorSecondary": {"solid": {"color": TEXT_COLOUR}},
                    "backColorSecondary": {"solid": {"color": "#E6E6E6"}},
                    "outline": "Frame",
                    "alignment": "Center",
                    "wordWrap": True
                    }],
                "total": [{
                    "totals": True,
                    "fontColor": {"solid": {"color": "#FFFFFF"}},
                    "backColor": {"solid": {"color": COLOUR_PALETTE[0]}},
                    "outline": "Frame"
                    }]
				}
        },
        "page": {
            "*": {
                "background": [{
                    "color": {"solid": {"color": PAGE_BACKGROUND}},
                    "transparency": PAGE_BACKGROUND_TRANSPARENCY
                }],
                "outspace": [{
                    "transparency": 0
                }]
            }
        },
        "textbox":  {
            "*" : {
				"background": [{
							"show": False,
							"color": {"solid": {"color": COLOUR_PALETTE[0]}},
							"transparency": 0
							}],
				"lockAspect": [{ 
							"show": False
							}],
				"border": 	[{
							"show": False,
							"color": {"solid": {"color": COLOUR_PALETTE[0]}},
							"radius": 3
							}],
				"dropShadow": 	[{
							"show": False
							}]
			    }
		    },
        "card": {
		    "*": {
                "general": [{
                   			"altText": "A card visual displaying high level summary values. Developer can choose to add additional info here." 
							}],
                "visualHeaderTooltip":[{
                    		"text": "Select chart bars or table rows to cross-filter this visual."
							}],
				"labels": 	[{
							"color": {"solid": {"color": "#000000"}},
							"fontSize": 32,
							"fontFamily": FONT,
							"preserveWhitespace": False,
							"bold": False,
							"italic": False,
							"underline": False
							}],
				"categoryLabels":  [{
							"show": True,
							"color": {"solid": {"color": "#808080"}},
							"fontSize": 12,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False
							}],
				"wordwrap": [{ 
							"show": True 
							}],
				"title":    [{
							"show": False,
							}],
				"subTitle":    [{
							"show": False,
							}],
				"divider":    [{
							"show": False,
							}],
                "background": 	[{
						"show": True,
						"color": {"solid": {"color": VISUAL_BACKGROUND}},
						"transparency": PAGE_BACKGROUND_TRANSPARENCY
						}],
				"border": 	[{
							"show": True,
							"color": {"solid": {"color": "#F5F4F0"}},
							"radius": 10
							}],
				"visualTooltip":[{
							"show": False,
							"titleFontColor":{"solid":{"color":"#FFFFFF"}},
							"valueFontColor":{"solid":{"color":"#FFFFFF"}},
							"fontSize": 11,
							"fontFamily": "FONT Black",
							"background":{"solid":{"color":"#D1CAB8"}},
							"transparency": TOOLTIP_TRANSPARENCY,
							"bold": True,
							"italic": False,
							"underline": False
							}]
                    }
                },
        "tableEx": {
            "*": {
                "general": [{
                            "altText": "A table visual. Developer can choose to add additional info here.",
							}],
                "visualHeaderTooltip":[{
                    		"text": "Click a column header to sort ascending or descending by that column. Select a row from the table to cross-filter other visuals. Hold CTRL to multi-select rows."
							}],
                "title": [{
							"show": True,
                            "text": "Add a table title",
							"fontColor": { "solid": { "color": "#FFFFFF" } },
							"background": { "solid": { "color": COLOUR_PALETTE[0] } },
							"alignment": "center",
							"fontSize": 12,
							"wordWrap": True,
                            "bold": True,
							"italic": True,
							"underline": False
							}],
                "subTitle": [{
							"show": False
							}],
                "values": [{
                    		"urlIcon": True
							}]
			}
		},
        "pivotTable": {
			"*": {
                "general": [{
                    		"altText": "A matrix visual. Developer can choose to add additional info here."
							}],
				"visualHeaderTooltip":[{
							"text": "Select the plus icon to expand rows. Select a cell, row, or column from the table to cross-filter other visuals. Hold CTRL to multi-select."
							}],
                "title": [{
							"show": True,
                            "text": "Add a matrix title",
							"fontColor": { "solid": { "color": "#FFFFFF" } },
							"background": { "solid": { "color": COLOUR_PALETTE[0] } },
							"alignment": "center",
							"fontSize": 12,
							"wordWrap": True,
                            "bold": True,
							"italic": True,
							"underline": False
							}],
                "subTitle": [{
							"show": False
							}],
                "stylePreset":[{
                    		"name":"None"
							}],
                "rowHeaders": [{
							"fontColor": { "solid": { "color": TEXT_COLOUR}},
							"outline": "Frame",
							"stepped": True,
							"steppedLayoutIndentation": 15,
							"urlIcon": True,
							"wordWrap": True,
							"fontFamily": FONT,
							"fontSize": 12,
							"alignment": "Left",
							"showExpandCollapseButtons": True
							}],
                "columnTotal":    [{
							"fontColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"backColor": {"solid": {"color": VISUAL_BACKGROUND}},
							}],
                "rowTotal":    [{
							"fontColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"backColor": {"solid": {"color": VISUAL_BACKGROUND}},
							}],
               "subTotals": [{
							"$id": "Row",
							"fontColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"backColor": {"solid": {"color": VISUAL_BACKGROUND}},
                            "applyToHeaders": True,
							},
							{
							"$id": "Column",
							"fontColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"backColor": {"solid": {"color": VISUAL_BACKGROUND}},
                            "applyToHeaders": True,
							},
							{
							"rowSubTotals": True,
							"columnSubTotals": True,
							"rowSubTotalsPosition": "Bottom",
							"perRowLevel": True,
							"perColumnLevel": True,
							"rowSubtotalsLabel": "Total",
							"columnSubtotalsLabel": "Total"
							}],
			}
		},
		# Dashboard styling
        "slicer": {
            "*":{
				"general": [{
                    		"altText": "A slicer used for page-level filtering. Developer can choose to add additional info here."
							}],
                "title": [{
							"show": False
							}],
                "header": [{
							"textSize": 10,
							"bold": True
							}],
				"visualHeaderTooltip":[{
							"text": "Use this slicer for page-level filtering. Select an item or slider the bar to filter the page. Hold CTRL to multi-select if necessary."
							}],
				"data": [{
							"mode": "Dropdown"
							}],
				"selection": [{
							"show": True,
							"singleSelect": False,
							"strictSingleSelect": False,
							"selectAllCheckboxEnabled": True
							}],
				"numericInputStyle":[{
							"fontColor": {"solid": {"color": "#786DB3"}},
							"backgroundColor": {"solid": {"color": "#B7B7B7"}},
							"fontSize": 9,
							"fontFamily": FONT
							}],
				"items":    [{
							"fontColor": {"solid": {"color": COLOUR_PALETTE[0]}},
                            "background": {"solid": {"color": VISUAL_BACKGROUND}},
							"outline": "None",
							"textSize": 10,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False
							}]
			}
		},
		"actionButton": {
            "*": {
                "visualHeaderTooltip":[{
							"text": "Select items to navigate to button path. Follow instructions in tooltip text that appears when hovering to enable this button if necessary."
							}],
                "shape": [{
            				"$id": "default",
							"tileShape": "pill"
            				}],
				"text": [{
							"show": True
							},
                            {
                            "$id": "default",
                            "text": "Add text",
                            "fontColor": {"solid": {"color": "#FFFFFF"}},
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"fontSize": 10,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3
							},
							{
							"$id": "hover",
                            "text": "Click here",
							"fontColor": {"solid": {"color": "#FFFFFF"}},
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"fontSize": 10,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3
							}
							,
							{
							"$id": "selected",
                            "text": "Selected",
							"fontColor": {"solid": {"color": "#FFFFFF"}},
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"fontSize": 10,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3
							}
							,
							{
							"$id": "disabled",
							"text": "Disabled",
							"fontColor": {"solid": {"color": "#808080"}},
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"fontSize": 10,
							"fontFamily": FONT,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3							
							}],
				"icon": [{
							"show": True
							},
							{
							"$id": "default",
							"shapeType": "rightArrow",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "right",
							"lineColor": {"solid": {"color": COLOUR_PALETTE[3]}},
							"lineTransparency": 10,
							"lineWeight": 2,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "right",
							"iconSize": 16
							},
							{
							"$id": "hover",
							"shapeType": "rightArrow",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "right",
							"lineColor": {"solid": {"color": COLOUR_PALETTE[3]}},
							"lineTransparency": 10,
							"lineWeight": 2,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "right",
							"iconSize": 16
							},
							{
							"$id": "selected",
							"shapeType": "rightArrow",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"lineColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"lineTransparency": 10,
							"lineWeight": 2,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "right",
							"iconSize": 16
							},
							{
							"$id": "disabled",
							"shapeType": "blank",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"lineColor": {"solid": {"color": "#F5F4F0"}},
							"lineTransparency": 10,
							"lineWeight": 2,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "right",
							"iconSize": 4
							}],
				"outline": [{
							"show": True
							},
							{
							"$id": "default",
							"lineColor": {"solid": {"color": "#808080"}},
							"transparency": 10,
							"weight": 1
							},
							{
							"$id": "hover",
							"lineColor": {"solid": {"color": "#808080"}},
							"transparency": 10,
							"weight": 1
							},								{
							"$id": "selected",
							"lineColor": {"solid": {"color": "#808080"}},
							"transparency": 10,
							"weight": 3
							},								{
							"$id": "disabled",
							"lineColor": {"solid": {"color": "#808080"}},
							"transparency": 10,
							"weight": 1							
							}],
				"fill":
						[{
							"show":True
							},
							{
							"$id": "default",
							"transparency": 20,
							"fillColor": {"solid":{"color": COLOUR_PALETTE[0]}},
							"scaling": "Fill"
							},
							{
							"$id": "hover",
							"transparency": 20,
							"fillColor": {"solid":{"color":COLOUR_PALETTE[3]}},
							"scaling": "Fill"
							},
							{
							"$id": "selected",
							"transparency": 20,
							"fillColor": {"solid":{"color": "#808080"}},
							"scaling": "Fill"
							},
							{
							"$id": "disabled",
							"transparency": 0,
							"fillColor": {"solid":{"color":"#F5F4F0"}},
							"scaling": "Fill"
							}],
				"dropShadow": 	[{
							"show": False,
							"color": {"solid": {"color": "#E8E8E8"}},
							"position":"Outer",
							"preset":"TopLeft"
							}],
				"visualLink": [{
							"show": True,
							"type": "Bookmark",
							"tooltip": "Click here"
							}],
				"background": 	[{
							"show": False,
							"color": {"solid": {"color": "#F5F4F0"}},
							"transparency": 0
							}],
				"lockAspect": [{ 
							"show": False
							}],
				"border": 	[{
							"show": False,
							"color": {"solid": {"color": "#F5F4F0"}},
							"radius": 5
							}]
			}
		}

    }
}

# write file to downloads folder
with open(f"{DOWNLOADS_PATH}\\generated-theme-{now}.json", "w", encoding= "utf-8") as f:
    json.dump(json_blob, f)
