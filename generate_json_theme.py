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
NAME = "Python Generated Theme"
VISUAL_BACKGROUND = "#EFF5F6"

# set theme from yaml config file
THEME = 0 # 0: tpr; 1: tableau

FONT = config[THEME]["font"]
PAGE_BACKGROUND = config[THEME]["page"]["background"]
PAGE_BACKGROUND_TRANSPARENCY = config[THEME]["page"]["transparency"]
COLOUR_PALETTE = config[THEME]["palette"]

now = datetime.now().strftime("%Y-%m-%d-%H%M%S")

# create json blob
json_blob = {
    "name": f"{NAME}-{now}",
    "dataColors": COLOUR_PALETTE,
    "firstLevelElements": COLOUR_PALETTE[9],
    "secondLevelElements": COLOUR_PALETTE[3], 
    "thirdLevelElements": "#F3F2F1",
    "fourthLevelElements": "#B3B0AD",
    "background": "#F2F2F2",
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
                    "show": False,
                    "color": {"solid": {"color": "#F0F2F2"}},
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
                    "color": {"solid": {"color": "#808080"}},
                    "position":"Outer",
                    "preset":"BottomRight"
                    }],
                "visualHeaderTooltip":[{
                    "type": "Default",
                    "titleFontColor":{"solid":{"color":"#E34820"}},
                    "text": "Your developer hasn't added a tooltip",
                    "fontSize": 10,
                    "fontFamily": FONT,
                    "background":{"solid":{"color":"#D1CAB8"}},
                    "transparency": 8,
                    "bold": False,
                    "italic": False,
                    "underline": False
                        }],
                "visualHeader": [{
                    "showVisualInformationButton": True,
                    "showVisualWarningButton": False,
                    "showVisualErrorButton": False,
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
                    "showTooltipButton": False,
                    "showSmartNarrativeButton": False
                            }],
                "visualTooltip": [{
                    "show": True,
                    "type": "Default",
                    "fontSize": 11,
                    "fontFamily": FONT,
                    "bold": True,
                    "italic": False,
                    "underline": False,
                    "background": {"solid": {"color": "#636363"}},
                    "transparency": 10,
                    "titleFontColor": {"solid": {"color": "#A7A5D9"} },
                    "ThemeDataColor": {"solid": {"color": "#171717"}}
                            }],
                "general":  [{
                    "responsive": True,
                    "altText": "Enter an alternative text"
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
                    "color": {"solid": {"color": "#030303"}},
                    "fontFamily": FONT,
                    "fontSize":8,
                    "enableBackground": True,
                    "backgroundColor": {"solid": {"color": "#E8E8E8"}},
                    "backgroundTransparency": 10,
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
                    "gridVertical": True,
                    "gridVerticalColor": {"solid": {"color": "#0A7AA6"}},
                    "gridVerticalWeight": 1,
                    "gridHorizontal": False,
                    "gridHorizontalColor": {"solid": {"color": "#0A7AA6"}},
                    "gridHorizontalWeight": 1,
                    "textSize": 11,
                    "rowPadding": 2,
                    "outlineColor": {"solid": {"color": "#FFFFFF"}},
                    "outlineWeight": 1
                    }],
                "columnHeaders": [{
                    "fontColor": {"solid": {"color": "#FFFFFF"}},
                    "backColor": {"solid": {"color": COLOUR_PALETTE[0]}},
                    "outline": "Frame",
                    "alignment": "Centre",
                    "wordWrap": True
                    }],
                "values": [{
                    "fontColorPrimary": {"solid": {"color": "#3D4E57"}},
                    "backColorPrimary": {"solid": {"color": "#F5F4F0"}},
                    "fontColorSecondary": {"solid": {"color": "#3D4E57"}},
                    "backColorSecondary": {"solid": {"color": "#E3DFD4"}},
                    "outline": "Frame",
                    "alignment": "center",
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
							"show": True,
							"color": {"solid": {"color": COLOUR_PALETTE[0]}},
							"radius": 3
							}],
				"dropShadow": 	[{
							"show": False,
							"color": {"solid": {"color": "#E8E8E8"}},
							"position":"Outer",
							"preset":"TopLeft"
							}]
			    }
		    },
        "card": {
		    "*": {
				"labels": 	[{
							"color": {"solid": {"color": "#000000"}},
							"labelPrecision": 1,
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
						"transparency": 0
						}],
				"border": 	[{
							"show": True,
							"color": {"solid": {"color": "#F5F4F0"}},
							"radius": 10
							}],
				"dropShadow": 	[{
							"show": True,
							"color": {"solid": {"color": "#808080"}},
							"position":"Outer",
							"preset":"BottomRight"
							}],
				"visualTooltip":[{
							"show": False,
							"titleFontColor":{"solid":{"color":"#FFFFFF"}},
							"valueFontColor":{"solid":{"color":"#FFFFFF"}},
							"fontSize": 11,
							"fontFamily": "FONT Black",
							"background":{"solid":{"color":"#D1CAB8"}},
							"transparency": 8,
							"bold": True,
							"italic": False,
							"underline": False
							}]
                    }
                },
        "slicer": {
            "*": {
				"data":  [{
							"mode": "Before"													
							}],
				"pendingChangesIcon": [{
							"show": True,
							"position": "left",
							"size": 12,
							"color": {"solid": {"color": "#786DB3"}},
							"transparency": 0,
							"tooltipText": "Awaiting final confirmation"
							}],
				"selection": [{
							"show": True,
							"singleSelect": True,
							"strictSingleSelect": False,
							"selectAllCheckboxEnabled": True
							}],
				"numericInputStyle":[{
							"fontColor": {"solid": {"color": "#786DB3"}},
							"backgroundColor": {"solid": {"color": "#B7B7B7"}},
							"fontSize": 9,
							"fontFamily": FONT
							}],
				"slider": 	[{ 
							"color": {"solid": { "color": COLOUR_PALETTE[1]} }
							}],
				"date":[{
							"fontColor": {"solid": {"color": "#6e6e6e"}},
							"background": {"solid": {"color": "#cfcfcf"}},
							"fontFamily": FONT,
							"textSize": 10
							}],
				"items":    [{
							"fontColor": {"solid": {"color": "#000000"}},
							"backgroundColor": {"solid": {"color": "#786DB3"}},
							"outline": "None",
							"textSize": 10,
							"fontFamily": FONT,
							"bold": False,
							"italic": False,
							"underline": False
							}],
				"title":    [{
							"show": False
							}],
				"subTitle":    [{
							"show": False
							}],
				"divider":    [{
							"show": False
							}]
                    }
                },
        "actionButton": {
            "*": {
				"text": [
							{
							"$id": "hover",
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
							"text": "Button disabled",
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
							"show": False
							},
							{
							"$id": "default",
							"shapeType": "help",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"lineColor": {"solid": {"color": COLOUR_PALETTE[5]}},
							"lineTransparency": 10,
							"lineWeight": 2,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "left",
							"iconSize": 22
							},
							{
							"$id": "hover",
							"shapeType": "help",
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
							"placement": "left",
							"iconSize": 22
							},
							{
							"$id": "selected",
							"shapeType": "help",
							"padding": 3,
							"verticalAlignment": "middle",
							"horizontalAlignment": "center",
							"lineColor": {"solid": {"color": COLOUR_PALETTE[0]}},
							"lineTransparency": 10,
							"lineWeight": 5,
							"topMargin": 3,
							"bottomMargin": 3,
							"leftMargin": 3,
							"rightMargin": 3,
							"placement": "left",
							"iconSize": 22
							},
							{
							"$id": "disabled",
							"shapeType": "help",
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
							"placement": "left",
							"iconSize": 22
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
							"weight": 1
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
							"tooltip": "Click button to activate bookmark"
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
