def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'name': 'Argiro', 'lastname':'Arias'}
    
    super_list = [
        {'name': 'Salome', 'lastname':'Arias'},
        {'name': 'Marina', 'lastname':'Cardona'},
        {'name': 'Yesenia', 'lastname':'Cardona'},
        {'name': 'Monica', 'lastname':'Gutierrez'},
        {'name': 'Omar', 'lastname':'Argumedo'},
        {'name': 'Yankeira', 'lastname':'Argumedo'},
    ]
    
    super_dict = {
        'natural_nums':[1,2,3,4,5,7],
        'integer_nums':[-3,0,-7,-8,5],
        'floating_nums':[2.5,4.4,5.23,9.55]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
        
    for key, value in super_list.items():
        print(key, '-', value)

if __name__ == '__main__':
    run()