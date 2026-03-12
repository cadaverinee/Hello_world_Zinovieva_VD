op_name = input('введите имя оператора: ')
sensor_value = input('введите текущее давление (Па): ')

# запись данных в файл
with open('sensor_log.txt', 'w', encoding='utf-8') as file:
    file.write(f'оператор\tзначение\n')
    file.write(f'{op_name}\t\t{sensor_value}\n')

print('данные успешно сохранены в sensor_log.txt')