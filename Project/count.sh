#!/bin/bash
while read -r line
do
    count=`cat word_tag_pair.txt | grep $line | wc -l`
    echo "$line $count"
done < "word_tag_pair.txt"