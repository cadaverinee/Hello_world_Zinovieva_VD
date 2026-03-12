#!/bin/bash

SUM=$(awk '{sum+=$2} END{print sum}' students.txt)
echo "cумма всех оценок: $SUM"

AVG=$(awk '{sum+=$2; count++} END{print sum/count}' students.txt)
echo "средняя оценка: $AVG"

MAX=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "максимальная оценка: $MAX"
