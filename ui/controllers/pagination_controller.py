from ui.view import show_dates
import keyboard # type: ignore
import time 
import sys
import os

def clear_console():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux / macOS
    else:
        os.system("clear")

def pag_controller(table, limit, offset = 0, index = 10, page = 1, page_limit = 10):
    time.sleep(0.3)
    if index > 10 and page != page_limit:
        index -= 1
        while True:
            if keyboard.is_pressed("flecha derecha"):
                clear_console()
                show_dates({ "offset" : offset + 10, "index" : index + 10, "page" : page + 1}, table, limit)
            elif keyboard.is_pressed("flecha izquierda") and offset != 0:
                clear_console()
                show_dates({ "offset" : offset - 10, "index" : index - 10, "page" : page - 1}, table, limit)
            elif keyboard.is_pressed("esc"):  
                clear_console()
                sys.exit()
    elif page == page_limit:
        clear_console()
        sys.exit()
    else:
        clear_console()
        show_dates({ "offset" : offset, "index" : index, "page" : page}, table, limit)
