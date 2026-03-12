weight = float(input("Введите вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))
height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("\n--- отчет о состоянии здоровья ---")
print(f"рост:\t\t{height_cm} см")
print(f"вес:\t\t{weight} кг")
print(f"ИМТ:\t\t{bmi:.2f}")