#! /usr/bin/python3

rfile = open('suspected_rules.txt','r')
wfile = open('probable_rules.txt','w')
rlines = rfile.readlines()
i=0
while(rlines[i]!='\n'):
    if rlines[i].split('/')[1] == rlines[i+1].split('/')[1]:
        if rlines[i+1].split('/')[1] == rlines[i+2].split('/')[1]:
            i+=1
        else:
            i+=2
    else:
        wfile.write(rlines[i])
        i+=1
