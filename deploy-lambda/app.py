import os

import shimoku_api_python as Shimoku
from shimoku_components_catalog.html_components import beautiful_indicator, panel


def lambda_handler(event, context):
    access_token: str = os.environ["SHIMOKU_API_TOKEN"]
    universe_id: str = os.environ["SHIMOKU_UNIVERSE_ID"]
    workspace_id: str = os.environ["SHIMOKU_BUSINESS_ID"]

    s = Shimoku.Client(
        access_token=access_token,
        universe_id=universe_id,
    )
    s.set_workspace(uuid=workspace_id)

    s.set_board("From Lambda Board")

    s.set_menu_path("trigger", "trigger-by-lambda")
    title = "MAU únicos"
    background_url = "https://images.unsplash.com/photo-1628771065518-0d82f1938462?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"
    text = "Lorem ipsum"

    indicator = beautiful_indicator(title=title, background_url=background_url)
    s.plt.html(
        indicator,
        order=0,
        rows_size=1,
        cols_size=12,
    )

    html = panel(
        href=None,
        text=text,
        symbol_name="Panorama",
    )

    s.plt.html(
        html=html,
        order=1,
        rows_size=1,
        cols_size=12,
    )

    count_unique_users = [
        {
            "description": "July",
            "title": "Número de Usuarios Únicos en el último mes",
            "value": 923,
            "color": "warning-background",
        },
        {
            "description": "Todo el periodo",
            "title": "Número de Usuarios Únicos desde el Principio",
            "value": 19034,
            "color": "success-background",
        },
    ]

    next_order = s.plt.indicator(
        data=count_unique_users,
        order=2,
        rows_size=1,
        cols_size=12,
        value="value",
        header="title",
        footer="description",
        color="color",
    )
    print("dashboard created")
    return
