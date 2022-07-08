#!/usr/bin/env python3
import sys
#from this import d
import numpy as np
import cv2
import os
import torch
import ssl  
import pandas as pd
import tqdm
import seaborn as sn
import matplotlib.pyplot as plt


ssl._create_default_https_context = ssl._create_unverified_context 


#take folder of images as arguemtn
#run each image through yolo
#add results to a text file
#test

#print ("hi")

def my_function(dirName):   
    imgs = []              
    results = open('results.txt', 'w')
    model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')  
    k=0
    for f in os.listdir(dirName):       #iterating over the folder 
        if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"):  
            i = os.path.join (dirName, f)    
            print (i)                 
            img = cv2.imread(i)        
            outcome = model(img)          
            txt = outcome.print()  
            #print(outcome.print())           
            results.write(txt)           
        #k += 1
        #if (k>10):
            #break
        
    
   
            
    results.close()

#######results.write(os.path.join(dirName, f) + "\n")

#
    # list of filenames in folder
    #start new text file
    #for every img in filename list of type image
    #   load image
    #   inferrence
    #   aphend results into text file
    #write text file


def main (x):
    return my_function(x)   
    
    
if __name__ == '__main__':
    #check if it is called with one argument, if so, call main with that argument
    if (len(sys.argv) == 2):
        sys.exit(main(sys.argv[1]))
    else :
        print ("Must have one argument")
        sys.exit(1)
    print(f"Argument Count: " + str(len(sys.argv)))
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
    for arg in sys.argv:
        print ("Arg: " + arg)
  

