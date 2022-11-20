#Aplicatie_Monitorizare

import os
#import cv2 as cv
import tkinter as tk
from tkinter import filedialog

totalVal = 0
maxVal = 0
completionPercentage = 0

def detLineValue(lin=""):
    val = 0

    startIndex = lin.rfind(')')

    if startIndex == 0 or startIndex == -1:
        return 0

    substringWithVal = lin[startIndex:]

    #startIndex = substringWithVal.rfind('-')

    #if startIndex == 0 or startIndex == -1:
       # return 0

    #substringWithVal = substringWithVal[startIndex + 1:]

    substrings = substringWithVal.split(' ')

    for substring in substrings:
        if substring.find('p') == -1:
            continue
        substring = substring.replace('p', '')

        try:
            subVal = int(substring)
        except:
            subVal = 0
            print("Error here: ", lin)
        val = val + subVal

    return val

def detLineMaxValue(lin):
    val = 0
    return val

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

file = open(file_path, 'r')
lines = file.readlines()

for line in lines:
    if line.find("Total:") != -1: #stops at the line with the total
        break
    if line.find("max") != -1: # -1 means text not found
        lineVal = detLineValue(line)
        lineMaxVal = detLineMaxValue(line)
        #print(lineVal)
        #print(lineMaxVal)
        totalVal = totalVal + lineVal
        maxVal = maxVal + lineMaxVal

if maxVal != 0:
    completionPercentage = totalVal * 100 / maxVal
else:
    completionPercentage = 0

print("Total: ", totalVal, 'p')
print("Max: ", maxVal, 'p')
print("Completare: ", completionPercentage, '%')
