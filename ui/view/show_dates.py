
def show_dates(points, df_dates, limit_dates):
    from ui.controllers import pag_controller
    offset = points["offset"]
    index = points["index"]
    page = points["page"]
    total_pages = (limit_dates + 9) // 10
    print(df_dates.iloc[offset : index + 1])
    if(index >= 10 and page <= total_pages):
        print("\n< Pagina {} de {} >" .format(page, total_pages))
        print("\nUse las teclas ← | → para cambiar de pagina o ESC para salir.")
        pag_controller(df_dates, limit = limit_dates, offset = offset, index = index + 1, page = page, page_limit = total_pages)

