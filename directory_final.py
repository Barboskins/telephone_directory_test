import csv
from pprint import pprint
import pandas as pd

# df = pd.DataFrame({
#     'Имя':['Гарри','Рон','Гермиона','Драко'],
#     'Фамилия':['Поттер','Уизли','Грейнджер','Малфой'],
#     'Отчество':['Джеймсовович','Артурович','Венделовна','Люциусович'],
#     'Организация':['Грифиндор','Грифиндор','Грифиндор','Слизерин'],
#     'Рабочий телефон': [4545, 4646, 4747, 4848],
#     'Личный телефон': [5555, 5656, 5757, 5858]
# })
# df.to_csv('directory.csv', index=False)


def show_all():
    with open('directory.csv', 'rt', encoding='utf-8', newline="") as f:
        reader = csv.DictReader(f)
        # vill = [row for row in reader]
        for row in reader:
            data = f'Имя - {row["Имя"]}, Фамилия - {row["Фамилия"]}, Отчество - {row["Отчество"]}, Организация - {row["Организация"]}, ' \
                   f'Рабочий телефон - {row["Рабочий телефон"]}, Личный телефон - {row["Личный телефон"]} '
            print (data)
        print('Конец списка')
        return


# print(show_all())


def create_entry():
    name = input('Введите имя ')
    last_name = input('Введите фамилию ')
    surname = input('Введите Отчество ')
    organization = input('Введите Организацию ')
    job_number = input('Введите рабочий номер ')
    home_number = input('Введите домашний номер ')
    with open('directory.csv', 'at', encoding='utf-8') as f:
        fieldnames = ['Имя', 'Фамилия', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
        writer = csv.DictWriter(
            f, fieldnames=fieldnames)
        writer.writerow({'Имя': name, 'Фамилия': last_name, 'Отчество': surname,'Организация': organization,
                         'Рабочий телефон': int(job_number), 'Личный телефон': int(home_number)})
        print('Запись добавлена')
        return


# print(create_entry())


def update_entry():
    name = input('Введите Имя, чьи данные хотите изменить?  ')
    fields_to_change = input('Какие данные Вы хотите изменить? (Имя, Фамилия, Отчество, Организация, Рабочий телефон или Личный телефон): ').split(',')
    data_to_update = {}
    for field in fields_to_change:
        # print(field)
        data_to_update[field] = input(f'Введите {field}: ')
        # print(data_to_update)
    df = pd.read_csv('directory.csv').set_index(['Имя'], drop=False).rename_axis(['_Имя'], axis=0)
    # print(df)
    df.loc[name, fields_to_change] = data_to_update
    df.to_csv('directory.csv', index=False)
    print('Спасибо, данные обновлены')
    return



# print(update_entry())

def search_entry():
    last_name = input('Введите фамилию ')
    organization = input('Введите Организацию ')
    job_number = input('Введите рабочий номер ')
    with open('directory.csv', 'rt', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Фамилия"] == last_name and row["Организация"] == organization or row["Рабочий телефон"] == job_number:
                print(row)
                break
        else:
            print('Записи с такими данными нет')
    print('Поиск окончен')
    return

# print(search_entry())