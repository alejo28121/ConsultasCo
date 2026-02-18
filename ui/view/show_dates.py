def show_dates(points, df_dates, limit_dates):
    from ui.controllers import pag_controller
    offset = points["offset"]
    index = points["index"]
    page = points["page"]
    if(index >= 10 and index <= limit_dates):
        print(df_dates.iloc[offset : index])
        print("< {} / {} >" .format(offset, index))
        pag_controller(df_dates, limit = limit_dates, offset = offset, index = index + 1)

