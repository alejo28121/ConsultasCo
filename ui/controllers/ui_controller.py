import os
from ui.view import draw_menu
from ui.view import ask_filters
from api.controllers import get_dates
from ui.controllers import pag_controller
from dotenv import load_dotenv # type: ignore

def start_ui():
    option = draw_menu();
    if option == "1":
        filters = ask_filters()
        state = filters["state"]
        limit = filters["dates_amount"]

        if limit == 0:
            limit = int(os.getenv("DEFAULT_LIMIT"))

        table  = get_dates(limit, state)

        pag_controller(limit = limit, table = table)
    elif option == "2":
        print("Opcion 2")        
    else:
        print("Opcion incorrecta.")    
