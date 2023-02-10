

def search_csv(data):
    with open ('phone_book.csv', 'r') as f:
        for line in f:
            if data in line:
                print(line)

