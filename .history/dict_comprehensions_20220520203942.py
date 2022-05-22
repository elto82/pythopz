import math
def run():
    # diccionario con los 100 primero numeros elevados al cubo
    # my_dict = {}
    
    # for i in range(1,101):
    #     my_dict[i] = i**3
        
    # print(my_dict)
    
    # diccionario con los 100 primeros numeros donde no sean divisibles por 3
    # my_dict ={}
    
    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3
    
    my_dict ={i: i**3 for i in range(1,101) if i %3 !=0}
            
    print(my_dict)    
    
    squareroot ={i:math.sqrt(i) for i in range(1,1001) }


if __name__ == '__main__':
    run()