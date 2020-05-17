def iterating_through_table_cells(the_table, foo):  # ITTC
    """
    Перебирает поочерёдно все ячейки объекта класса table в matplotlib
    и выполняет над ними действия содержащиеся в функции-аргументе foo.
    """
    cells = the_table.get_celld()
    for cell in cells.keys():
        item = the_table.__getitem__(cell)
        foo(item)
    return the_table
