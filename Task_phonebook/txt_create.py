
def new_name(data):
    n, s, p = data
    with open ('phone_book.txt', 'a') as file:
        file.write('Имя: {}   Фамилия: {}   Номер: {}   \n'.format(n, s, p))
