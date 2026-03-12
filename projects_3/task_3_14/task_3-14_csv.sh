#!/bin/bash

echo "названия товаров:"
awk -F, '{print $2}' data.csv

echo -e "\nтовары дороже 20:"
awk -F, '$3>20 {print $2, $3}' data.csv

TOTAL=$(awk -F, '{sum+=$3} END{print sum}' data.csv)
echo -e "\nобщая стоимость: $TOTAL"
