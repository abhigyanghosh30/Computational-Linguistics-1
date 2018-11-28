#! /usr/bin/python3 

file = open('test_hindi_compare_0.txt','r')
file2 = open('test_hindi_compare_1.txt','w')
lines = file.readlines()
for line in lines:
    words=line.split('|')
    if(words[0]!="NULL"):
        file2.write(line)