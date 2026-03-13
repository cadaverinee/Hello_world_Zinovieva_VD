#!/bin/bash

# запрос массы у пользователя
read -p "введите вашу массу (кг): " WEIGHT

# вычисление ИМТ
BMI=$(echo "scale=2; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc)

# округляем до целого числа
BMI_INT=$(printf "%.0f" "$BMI")

# вывода
echo "ваш индекс массы тела: $BMI_INT"
