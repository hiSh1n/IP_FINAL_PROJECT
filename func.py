import pandas as pd

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
    else: quit()

# A function for printing specific lines from a file
def PrintDialog(StartLineNo,EndLineno, file):
    ncount = 0
    for i in file:
        if i == '\n':
            ncount += 1
        if StartLineNo-1 <= ncount and ncount < EndLineno:
            print(i, end='') 

def retrieve():
    fname = input('Enter filename [FILE MUST BE ON CURRENT DIRECTORY]: ')
    try:
        df = pd.read_csv(f'.//{fname}.csv')
        print(df)
    except:
        print('File does not exist!')
        