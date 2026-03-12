#!/bin/bash

echo "имена студентов:"
awk '{print $1}' students.txt

echo -e "\nоценки студентов:"
awk '{print $2}' students.txt

echo -e "\nномер строки и имя:"
awk '{print NR, $1}' students.txt
