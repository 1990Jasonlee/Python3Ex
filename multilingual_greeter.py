def language_input():
    global pick
    pick = int(input('Enter number for corresponding language: 1-English 2-Spanish 3-French'))

def name_input():
    global input_name
    if pick == 1:
        input_name = input('Enter a name:')
    elif pick == 2:
        input_name = input('Ingresa un nombre:')
    elif pick == 3:
        input_name = input('Entrez un nom:')
    else:
        print('invalid choice')


def greet():
    if pick == 1:
        print(f'Hello {input_name}')
    elif pick == 2:
        print(f'Hola {input_name}')
    elif pick == 3:
        print(f'Bonjour {input_name}')


language_input()
name_input()
greet()
