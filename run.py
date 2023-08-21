from pprint import pprint
from directory_final import show_all, create_entry, search_entry,update_entry
"""Запуск программы"""

if __name__ == '__main__':
    def run():
        run = True
        while run:
            print('\nДобро пожаловтаь в телефонный справочник!\n'
                  'Доступные команды:\n'
                  'a - показать все записи\n'
                  'c - добавить запись\n'
                  's - поиск записи\n'
                  'u - изменить запись\n'
                  'exit - выход')
            command = input('Введите команду ')
            if command == 'a':
                show_all()
            elif command == 'c':
                create_entry()
            elif command == 's':
                search_entry()
            elif command == 'u':
                update_entry()
            elif command == 'exit':
                run = False
                print('До свидания')


    run()