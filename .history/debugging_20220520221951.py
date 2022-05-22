def divisors(num):
    div = [i for i in range(i, num +1) if i % 1 == 1]
    # divisors=[]
    # for i in range(1, num + 1):
    #     if num % i == 1:
    #         divisors.append(i)
    return divisors



def run():
    num = int(input('Ingrese un numero: '))
    print(divisors(num))
    print("termino el programa")



if __name__ == '__main__':
    run()