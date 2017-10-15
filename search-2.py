#!/usr/bin/env python3

import os
import random
import sys

rdm = raw_input("Would you let me make a choice? 0 or 1: ")

#cur_dir = os.getcwd()

if rdm == '1':
    print("Playing random song")
    folder=os.listdir(os.getcwd())
    file=random.choice(folder)
    ext3=['.mp3']
    print('First random pick: '+file)

    while file[-4:] not in ext3 :
        print('Not an MP3 file  : '+file)
        file=random.choice(folder)
    else:
        os.startfile(file)
        print('Song name: '+file)

    sys.exit()

else:
    if rdm == '0':
        file_name = raw_input("File Name: ") #file to be searched
        #cur_dir = raw_input("Search Directory: ") # Dir from where search starts can be replaced with any path
        cur_dir = os.getcwd()
        while True:
            file_list = os.listdir(cur_dir)
            parent_dir = os.path.dirname(cur_dir)
            if file_name in file_list:
                print ("File Exists in: "), cur_dir
                #
                os.startfile(file_name)
                #
                break
            else:
                if cur_dir == parent_dir: #if dir is root dir
                    print ("File not found")
                    break
                else:
                    cur_dir = parent_dir




