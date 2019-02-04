#! /usr/bin/python3

count = 0
file1 = open('test_hindi_compare_1.txt','r')
file2 = open('test_hindi_9.txt','r')
lines1 = file1.readlines()
lines2 = file2.readlines()
for i in range(0,len(lines1)):
    if lines1[i]!=lines2[i]:
        count+=1
        print(i)
        print(lines1[i]+lines2[i])
print(count)
