

def add_note():
    note = input('Enter note: ')
    with open('notes.txt','a',encoding='utf-8') as file:
        file.write(note + '\n')


def show_notes():
    try:

        with open('notes.txt','r',encoding='utf-8') as file:
            lines = file.readlines()
        if not lines:
            print('No notes yet')
        else:
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print('No notes yet')


def clear_notes():

    with open('notes.txt','w',encoding='utf-8') as file:
        file.write('')


choice = ''

while choice!='0':
    print('1 - Add note')
    print('2 - Show notes')
    print('3 - Clear notes')
    print('0 - Exit')

    choice = input('Choose option: ')


    if choice == '1':
        add_note()
    elif choice == '2':
        show_notes()
    elif choice == '3':
        clear_notes()
    elif choice == '0':
        print('Goodbye')
    else:
        print('Invalid choice')