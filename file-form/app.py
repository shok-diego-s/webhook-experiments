from os import getenv

import shimoku_api_python as Shimoku

access_token: str = getenv("SHIMOKU_API_TOKEN")
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

s.plt.input_form(
    order=0,
    options=input_data,
)  # todo: activity_name=


s.activities.create_webhook(
    url=getenv("SHIMOKU_API_GATEWAY"),
    name="activity-zappa",
    method="GET",
)

dict_activity = s.activities.get_activity(
    name="activity-zappa",
)

print(dict_activity)

# input_data = s.plt.get_input_forms()
# print(input_data)
