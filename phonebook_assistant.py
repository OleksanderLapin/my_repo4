phone_book = {}

def input_error(func):
    def inner(*args):
        try: 
            return func(*args) 
        except (KeyError, ValueError, IndexError): 
            return print('Use digit for phone number')  

    return inner
    
@input_error   
def add_contact(name_and_phone): 
    name, phone = name_and_phone.split(' ')
    phone_book[name] = int(phone)  
    
@input_error    
def change_contact(name_and_phone):  
    name, phone = name_and_phone.split(' ')     
    if name not in phone_book.keys():   
        phone_book[name] = int(phone)    
    else:    
        for key in phone_book.keys():            
            if key == name:                 
                phone_book[key] = int(phone)                              

def main():
    while True:
        b = input('Enter command:')
        c = ['good bye', 'close', 'exit']
        d = b.split(' ', maxsplit = 1)[0].lower()         
        if b in c:
            break
        elif b == 'show all':
            print(phone_book)
            continue
        elif b == 'hello':
            print('How can i help you?')
            continue
        elif b == 'add':
            add_contact(input('Enter user name:'))
            print('New contact was added!')
            continue
        elif b == 'change':
            change_contact(input('Give me name and phone please'))
            print('The contacts was changed!')
            continue
        elif b == 'phone':
            g = input('Enter name of contact: ')
            if g in phone_book.keys():
                print(f'The phone number {g} of is {phone_book[g]}')
            else:
                print(f'User name {g} is not in phonebook')
            continue
        elif d == 'add':
            add_contact(b.split(' ', maxsplit = 1)[1])
            print('New contact was added!')
        elif d == 'change':
            change_contact(b.split(' ', maxsplit = 1)[1])
        elif d == 'phone':
            g = b.split(' ', maxsplit = 1)[1]
            if g in phone_book.keys():
                print(f'The phone number {g} of is {phone_book[g]}')
            else:
                print(f'User name {g} is not in phonebook')
            continue
            
        else:
            print('Please enter correct command.')
            continue

main()
print(phone_book)
