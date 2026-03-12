ph = float(input("введите значение pH: "))

if ph < 7:
    print(f'pH {ph} - это кисло')
elif ph == 7:
    print(f'pH {ph} - это нейтрально')
else:
    print(f'pH {ph} - это щелочно')