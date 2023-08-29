from os import getenv

import shimoku_api_python as Shimoku

access_token = getenv("SHIMOKU_API_TOKEN")
universe_id: str = getenv("SHIMOKU_UNIVERSE_ID")
workspace_id: str = getenv("SHIMOKU_BUSINESS_ID")

s = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
)
s.set_workspace(uuid=workspace_id)

s.set_board("Custom Board")

s.set_menu_path("trigger", "trigger-by-file")

input_data = {
    "fields": [
        {
            "title": "Input file",
            "fields": [
                {
                    "mapping": "file",
                    "fieldName": "File",
                    "inputType": "file",
                    "dragAndDrop": True,
                }
            ],
        },
    ]
}

s.plt.input_form(order=0, options=input_data)
