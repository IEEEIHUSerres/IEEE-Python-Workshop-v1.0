def table_number_avg(table):
    if len(table) == 0:
        return 0

    sum_of_table = 0

    for number in table:
        sum_of_table = sum_of_table + int(number)

    return sum_of_table / len(table)
