#!/bin/bash

df -h | awk 'NR>1 {print $1, $5; perc=$5+0; if(perc>90) print "заполнено более 90%!"}'
