import pandas as pd
import time as t
import matplotlib.pyplot as plt
import func as f 

dialogs = open(r"./Dialogs.txt", "r")
dis = dialogs.read()
f.PrintDialog(1,4, dis)
op_choice = input('\n y/n: ')
if op_choice.lower() == 'y':
    pass
else: 
    quit()

while True:   
    f.PrintDialog(5,11, dis)
    op_choice = int(input())
    if op_choice not in [ 1, 2, 3]:
        print("Not available! Select again.")
    else: pass
    if op_choice == 1:
        f.new_table()
    if op_choice == 2:
        f.retrieve()
    if op_choice == 3:
        print('Have a great day!')
        t.sleep(2)
        quit()
    








