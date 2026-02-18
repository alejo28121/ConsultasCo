from ui.view import show_dates
import keyboard # type: ignore
import time 

def pag_controller(table, limit, offset = 0, index = 10, page = 1):
    time.sleep(0.3)
    if (index > 10):
        while True:
            if (keyboard.is_pressed("right")):
                show_dates({ "offset" : offset + 10, "index" : index + 9, "page" : page + 1}, table, limit)
            else:
                break
    else:
        show_dates({ "offset" : offset, "index" : index, "page" : page }, table, limit)
