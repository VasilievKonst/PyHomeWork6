import data_input as di
import txt_create as tc
import csv_create as cc

def add_to_phonebook():
    data = di.new_contact()
    tc.new_name(data)
    cc.new_name(data)
    

    

