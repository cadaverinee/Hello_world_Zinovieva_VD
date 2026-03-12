#!/bin/bash

echo "студенты с оценкой > 80:"
awk '$2>80 {print $0}' students.txt

echo -e "\nстуденты с оценкой < 70:"
awk '$2<70 {print $0}' students.txt

echo -e "\nпервая строка файла:"
head -n 1 students.txt
