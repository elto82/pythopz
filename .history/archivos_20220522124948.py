def read():
    numbers =[]
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)


def write():
    names = ['Argiro','Antonio','Andres', 'Rocío','ñoño']
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
        print(f)


def run():
    # read()
    write()



if __name__ == '__main__':
    run()