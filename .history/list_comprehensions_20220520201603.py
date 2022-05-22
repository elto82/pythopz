def run():
    # crear una lista con los primeros 100 numeros al cuadrado y no guardar los rsultados que son divisibles por 3
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         square.append(i**2)
    # print(square)
    
    squares = [i**2 for i in range(1,101) if i% 3 !=0]
    print(squares)
    
    mult469 =[i for i in range(1,10000) if i%4 ==0 and i%6 == 0 and i%9 == 0]
    print(mult469)




if __name__ == '__main__':
    run()
