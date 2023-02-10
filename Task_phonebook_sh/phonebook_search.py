import data_search_input as di
import csv_search as cs
import txt_search as ts

def p_s():
    data = di.name_search()
    cs.search_csv(data)
    ts.search_txt(data)


    