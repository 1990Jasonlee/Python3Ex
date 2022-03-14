def language_input():
    pick = int(input('Enter number for corresponding language: 1-English 2-Spanish 3-French'))


def greet(name):
    print(f'Hello {name}')

def name_input():
    input_name = input('Enter a name:')
    greet(input_name)
name_input()

