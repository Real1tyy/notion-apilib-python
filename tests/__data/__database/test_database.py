# Standard Library
# {
#     "title": [
#         {
#             "type": "text",
#             "text": {
#                 "content": "Goals",
#                 "link": null
#             },
#             "annotations": {
#                 "bold": false,
#                 "italic": false,
#                 "strikethrough": false,
#                 "underline": false,
#                 "code": false,
#                 "color": "default"
#             },
#             "plain_text": "Goals",
#             "href": null
#         }
#     ],
#     "description": [
#         {
#             "type": "text",
#             "text": {
#                 "content": "Goals are what you want to achieve in a particular area in the given timeframe, they are used for writing future plans and things that you need to focus on in a particular area of life.",
#                 "link": null
#             },
#             "annotations": {
#                 "bold": false,
#                 "italic": false,
#                 "strikethrough": false,
#                 "underline": false,
#                 "code": false,
#                 "color": "default"
#             },
#             "plain_text": "Goals are what you want to achieve in a particular area in the given timeframe, they are used for writing future plans and things that you need to focus on in a particular area of life.",
#             "href": null
#         }
#     ],
#     "is_inline": false,
#     "properties": {
#         "Tasks": {
#             "id": "GFoK",
#             "name": "Tasks",
#             "type": "relation",
#             "relation": {
#                 "database_id": "706cd118-dfaf-40c2-8802-9314d62e2357",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Goal",
#                     "synced_property_id": "%5BGK_"
#                 }
#             }
#         },
#         "Shorter-Term Goals": {
#             "id": "JVG%5C",
#             "name": "Shorter-Term Goals",
#             "type": "relation",
#             "relation": {
#                 "database_id": "1a91e289-d5d9-470d-9e30-ff1dfde63c60",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Longer-Term Goal",
#                     "synced_property_id": "Xi%3E%3C"
#                 }
#             }
#         },
#         "Notebooks": {
#             "id": "KbuK",
#             "name": "Notebooks",
#             "type": "relation",
#             "relation": {
#                 "database_id": "773d0524-4a86-45e3-890e-00d9f0c000fb",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Goals",
#                     "synced_property_id": "Irw%5C"
#                 }
#             }
#         },
#         "ID": {
#             "id": "NqKZ",
#             "name": "ID",
#             "type": "unique_id",
#             "unique_id": {
#                 "prefix": "GOAL"
#             }
#         },
#         "Projects": {
#             "id": "R%3CIi",
#             "name": "Projects",
#             "type": "relation",
#             "relation": {
#                 "database_id": "d37fff0f-8ba5-4a3a-833d-34c772091be3",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Goal",
#                     "synced_property_id": "%3Eun%3B"
#                 }
#             }
#         },
#         "Progress": {
#             "id": "R_gY",
#             "name": "Progress",
#             "type": "rollup",
#             "rollup": {
#                 "rollup_property_name": "Archive",
#                 "relation_property_name": "Tasks",
#                 "rollup_property_id": "PNoF",
#                 "relation_property_id": "GFoK",
#                 "function": "percent_checked"
#             }
#         },
#         "Areas": {
#             "id": "Rekt",
#             "name": "Areas",
#             "type": "relation",
#             "relation": {
#                 "database_id": "97b48d4f-ece7-41b3-95ce-37ec64e93346",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Goals",
#                     "synced_property_id": "H%3Ao%7B"
#                 }
#             }
#         },
#         "Last Edited Time": {
#             "id": "ShKZ",
#             "name": "Last Edited Time",
#             "type": "last_edited_time",
#             "last_edited_time": {}
#         },
#         "Notes": {
#             "id": "Vk%3FL",
#             "name": "Notes",
#             "type": "relation",
#             "relation": {
#                 "database_id": "aa9c9ea5-b03b-436e-92a9-1edea5f69b19",
#                 "type": "single_property",
#                 "single_property": {}
#             }
#         },
#         "Longer-Term Goal": {
#             "id": "Xi%3E%3C",
#             "name": "Longer-Term Goal",
#             "type": "relation",
#             "relation": {
#                 "database_id": "1a91e289-d5d9-470d-9e30-ff1dfde63c60",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Shorter-Term Goals",
#                     "synced_property_id": "JVG%5C"
#                 }
#             }
#         },
#         "Created Time": {
#             "id": "a%3AuR",
#             "name": "Created Time",
#             "type": "created_time",
#             "created_time": {}
#         },
#         "Archive": {
#             "id": "aKFM",
#             "name": "Archive",
#             "type": "checkbox",
#             "checkbox": {}
#         },
#         "Description": {
#             "id": "cCje",
#             "name": "Description",
#             "type": "rich_text",
#             "rich_text": {}
#         },
#         "Type": {
#             "id": "gAID",
#             "name": "Type",
#             "type": "select",
#             "select": {
#                 "options": [
#                     {
#                         "id": "yk\\o",
#                         "name": "Never Ending",
#                         "color": "yellow",
#                         "description": null
#                     },
#                     {
#                         "id": "QQFJ",
#                         "name": "30 Years Goal",
#                         "color": "pink",
#                         "description": null
#                     },
#                     {
#                         "id": "~e>]",
#                         "name": "20 Years Goal",
#                         "color": "purple",
#                         "description": null
#                     },
#                     {
#                         "id": "p{kE",
#                         "name": "10 Years Goal",
#                         "color": "orange",
#                         "description": null
#                     },
#                     {
#                         "id": "I_e[",
#                         "name": "5 Years Goal",
#                         "color": "blue",
#                         "description": null
#                     },
#                     {
#                         "id": ">{{u",
#                         "name": "3 Years Goal",
#                         "color": "green",
#                         "description": null
#                     },
#                     {
#                         "id": "{^^`",
#                         "name": "1 Year Goal",
#                         "color": "red",
#                         "description": null
#                     }
#                 ]
#             }
#         },
#         "Status": {
#             "id": "iGd%7D",
#             "name": "Status",
#             "type": "status",
#             "status": {
#                 "options": [
#                     {
#                         "id": "438a310b-cff1-4458-8a10-410be7031351",
#                         "name": "Inbox",
#                         "color": "default",
#                         "description": null
#                     },
#                     {
#                         "id": "e56331a7-d479-4a96-8c09-97fac268841b",
#                         "name": "In progress",
#                         "color": "blue",
#                         "description": null
#                     },
#                     {
#                         "id": "377fe5db-a5ba-41e6-914f-c6caa5463e12",
#                         "name": "Achieved",
#                         "color": "green",
#                         "description": null
#                     }
#                 ],
#                 "groups": [
#                     {
#                         "id": "58de44d0-847f-4660-9cf3-f431a2c409e9",
#                         "name": "To-do",
#                         "color": "gray",
#                         "option_ids": [
#                             "438a310b-cff1-4458-8a10-410be7031351"
#                         ]
#                     },
#                     {
#                         "id": "63876edf-8365-46df-bac1-38b35a95f634",
#                         "name": "In progress",
#                         "color": "blue",
#                         "option_ids": [
#                             "e56331a7-d479-4a96-8c09-97fac268841b"
#                         ]
#                     },
#                     {
#                         "id": "4f46452a-5d7f-456c-ad01-c9bd266dc2d7",
#                         "name": "Complete",
#                         "color": "green",
#                         "option_ids": [
#                             "377fe5db-a5ba-41e6-914f-c6caa5463e12"
#                         ]
#                     }
#                 ]
#             }
#         },
#         "Currently Focused": {
#             "id": "%7CGsS",
#             "name": "Currently Focused",
#             "type": "checkbox",
#             "checkbox": {}
#         },
#         "Resources": {
#             "id": "%7Cn%7CJ",
#             "name": "Resources",
#             "type": "relation",
#             "relation": {
#                 "database_id": "41f9cfea-be22-44b8-8425-ab27bf68c8a6",
#                 "type": "dual_property",
#                 "dual_property": {
#                     "synced_property_name": "Goals",
#                     "synced_property_id": "WYT%5B"
#                 }
#             }
#         },
#         "Name": {
#             "id": "title",
#             "name": "Name",
#             "type": "title",
#             "title": {}
#         }
#     },
# }
