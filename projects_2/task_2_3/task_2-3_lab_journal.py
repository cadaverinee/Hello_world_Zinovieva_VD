# ввод
name = input("ФИО исследователя: ")
date = input("Дата: ")
experiment = input("Эксперимент: ")
vyvod = input("Вывод: ")

# ширина рамки
width = 50
border = "+" + "-" * (width - 2) + "+"

# оформление
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write(f"{border}\n")
    file.write(f"| {'Электронный лабораторный журнал':<{width-2}} |\n")
    file.write(f"{border}\n")
    file.write(f"| ФИО исследователя : {name:<{width-22}} |\n")
    file.write(f"| Дата             : {date:<{width-22}} |\n")
    file.write(f"| Эксперимент      : {experiment:<{width-22}} |\n")
    file.write(f"{border}\n")
    file.write(f"| Вывод: {'':<{width-9}} |\n")
    lines = vyvod.split('. ')

    for line in lines:
        file.write(f'| {line:<{width - 2}} |\n')
    file.write(f"{border}\n")
print("данные успешно сохранены в файл 'journal.txt'.")