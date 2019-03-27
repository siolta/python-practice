file_name = input("What should the file be named? >  ")

with open(file_name, 'a') as f:
    content = input("Content>>  ") # + '\n'

    while len(content.strip()) > 0:
        f.write(content,)
        content = input("Content>>  ") # + '\n'
