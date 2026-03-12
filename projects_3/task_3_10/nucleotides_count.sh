#!/bin/bash

# заголовок таблицы
printf "%-15s %-7s %-7s %-7s %-7s\n" "файл" "A" "T" "G" "C"

# перебираем все FASTA-файлы
for file in *.fasta; do
    # пропускаем пустые файлы
    if [ ! -s "$file" ]; then
        continue
    fi

    # получаем последовательность без заголовков и переносов строк
    SEQ=$(grep -v "^>" "$file" | tr -d '\n')

    # подсчёт нуклеотидов
    A_COUNT=$(echo "$SEQ" | grep -o "A" | wc -l)
    T_COUNT=$(echo "$SEQ" | grep -o "T" | wc -l)
    G_COUNT=$(echo "$SEQ" | grep -o "G" | wc -l)
    C_COUNT=$(echo "$SEQ" | grep -o "C" | wc -l)

    # выводим результат в таблицу
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A_COUNT" "$T_COUNT" "$G_COUNT" "$C_COUNT"
done
