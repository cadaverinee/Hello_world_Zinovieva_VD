# скока скока скока
prots = float(input('введите массу белков в г:'))
fats = float(input('введите массу жиров в г:'))
carbs = float(input('введите массу углеводов в г:'))

# расчет калорийности
calories = prots * 4 + fats * 9 + carbs * 4

# вывод вкусности
print(f"калорийность: {calories} ккал")