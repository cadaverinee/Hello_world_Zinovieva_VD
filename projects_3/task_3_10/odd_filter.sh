#!/bin/bash

for i in {1..20}; do
    # пропускаем чётные числа
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi

    # выводим нечётное число
    echo $i

    # останавливаем цикл, если число 15
    if [ $i -eq 15 ]; then
        break
    fi
done
