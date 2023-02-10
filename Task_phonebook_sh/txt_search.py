def search_txt(data):
    with open ('phone_book.txt', 'r') as f:
        for line in f:
            if data in line:
                print(line)