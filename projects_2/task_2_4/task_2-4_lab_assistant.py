# объем физраствора
vol = float(input('введите нужный объем физраствора (мл): '))

# расчет массы соли
salt = vol * 0.009

# объем воды
water = vol

# отчитываемся
report = ('ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n'
        + '-' * 23 + '\n'
        + f'общий объем: {vol:.2f} мл\n'
        + f'масса соли: {salt:.2f} г\n'
        + f'объем воды: {water:.2f} мл\n'
)

with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(report)