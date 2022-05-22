def divisors(num):
    did = []
    divisors=[]
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors



def run():
    pass




if __name__ == '__main__':
    run()