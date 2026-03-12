# ввод данных
medium_name = input("введите название среды: ")
agar_conc = input("введите концентрацию агара (%): ")
steril_temp = input("введите температуру стерилизации (°C): ")

# запись данных в файл
with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(f"{medium_name}\n")
    file.write(f"- концентрация агара: {agar_conc}%\n")
    file.write(f"- температура стерилизации: {steril_temp}°C\n")

print("файл 'recipe.txt' успешно сформирован!")