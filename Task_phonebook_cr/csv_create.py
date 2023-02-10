
def new_name(data):
    n, s, p = data
    with open ('phone_book.csv', 'a') as file:
        file.write('Имя: {}   Фамилия: {}   Номер: {}   \n'.format(n, s, p))
        file.close()
    