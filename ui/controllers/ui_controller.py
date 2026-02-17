import os
from ui.view import draw_menu
from ui.view import ask_filters
from api.controllers import get_dates
from dotenv import load_dotenv # type: ignore

def start_ui():
    option = draw_menu();
    if option == "1":
        filters = ask_filters()
        state = filters["state"]
        limit = filters["dates_amount"]

        if limit == 0:
            limit = int(os.getenv("DEFAULT_LIMIT"))

        get_dates(limit, state)
    elif option == "2":
        print("Opcion 2")        
    else:
        print("Opcion incorrecta.")    
