#!/bin/bash

# создаём 10 файлов
for i in {1..10}; do
    touch "test$i.txt"
done

# удаляем файлы в обратном порядке
i=10
while [ $i -ge 1 ]; do
    rm -f "test$i.txt"
    ((i--))
done
