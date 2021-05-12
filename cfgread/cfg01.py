#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
## display file to the screen - .read()
    print(configfile.read())

######## EXPLORE READLINES ##########
## re-create file object to explore new method
with open("vlanconfig.cfg", "r") as configfile:
## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

## Iterate through configlist
    for x in configlist:
        print(x, sep= " ")

