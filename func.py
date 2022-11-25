import pandas as pd
import matplotlib.pyplot as plt

# A function for creating a new table
def new_table():
    NoOfCols = int(input('Enter no. columns: '))
    NoOfRows = int(input('Enter no of rows: '))

    dic = {}
    for i in range(NoOfCols):
        row = []
        key = input(f"Enter column name {i + 1}: ")
        for j in range(NoOfRows):
            value  = input(f"Enter row value {j + 1}: ")
            row.append(value)
        dic[key] = row

    df = pd.DataFrame(dic)
    print(df)

    op = input('Would you like to save? y/n: ')
    if op.lower() == 'y':
        filename = input('Enter filename: ')
        df.to_csv(f'.//{filename}.csv',index=None)
    else: pass

# A function for printing specific lines from a file
def PrintDialog(StartLineNo,EndLineno, file):
    ncount = 0
    for i in file:
        if i == '\n':
            ncount += 1
        if StartLineNo-1 <= ncount and ncount < EndLineno:
            print(i, end='') 

#A function to print an existing table
def retrieve():
    
    fname = input('Enter filename [FILE MUST BE ON CURRENT DIRECTORY]: ')
    try:
        df = pd.read_csv(f'.//{fname}.csv')
        print(df)
    except:
        print('File does not exist!')

#A visualiser function but a part of retrieve function.
    opc = input("Would you like to visualise this data? y/n: ")
    if opc.lower() != 'y':
        pass
    else:
        x = input("Enter the column on x-axis: ")
        y = input("Enter the column on y-axis: ")
        opc = input('-Press 1 for Bar graph.\n-Press 2 for Line graph.\n: ')
        if opc not in  ['1','2']: 
            print('bye!')
        if opc == '1':
            try:
                xaxis = list(df.loc[:,x])
                yaxis = list(df.loc[:,y])
                plt.bar(xaxis,yaxis)
                plt.show()
            except:
                print("Table can't be generated.\nKindly select select new values.")
        if opc == '2': 
            try:
                plt.plot(xaxis,yaxis)
                plt.show()
            except:
                print("Table can't be generated.\nKindly select select new values.")
