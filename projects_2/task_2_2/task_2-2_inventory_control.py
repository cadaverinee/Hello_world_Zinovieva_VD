reagent_name = input('введите название реагента: ')
quantity = input('введите количество реагента: ')

report = f'реактив {reagent_name} поступил на склад в количестве {quantity}'
print(report)

#запишем в тхт файл
with open('inventory.txt', 'w', encoding='utf-8') as file:
    file.write(report)