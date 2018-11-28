#! /usr/bin/python3

count = 0
file1 = open('test_hindi_compare_1.txt','r')
file2 = open('test_hindi_1.txt','r')
lines1 = file1.readlines()
lines2 = file2.readlines()
for i in range(0,len(lines1)):
    if lines1[i]!=lines2[i]:
        count+=1
        print(lines1[i-1].split('|')[1][:-1]+"|"+lines1[i].split('|')[1][:-1]+"|"+lines2[i+1].split('|')[1][:-1]+"/"+lines2[i-1].split('|')[1][:-1]+"|"+lines2[i].split('|')[1][:-1]+"|"+lines2[i+1].split('|')[1][:-1])
print(count)
