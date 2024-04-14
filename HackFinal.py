import pandas as pd


def addBook(ID, bookName):
    data_raw = pd.read_excel("rented.xlsx")
    data = data_raw.to_numpy()
    # print(data[0])
    arr=  []
    unfilled = False
    curr_users = []
    filled_len = len(data[0])
    for item in data:
        curr_users.append(item[0])
    
    i = curr_users.index(ID)
    for j, value in enumerate(data[i]):
        if str(value) == "nan":
            filled_len = j
            unfilled = True
            break
    
    if unfilled:
        for item in data:
            arr.append(item[-1])
        data_raw.pop(filled_len)
    else:
        arr = [""] * len(data)
    arr[i] = bookName
    # print(arr)
    data_raw.insert(filled_len, filled_len, arr)
    data_raw.to_excel("rented.xlsx", index=False)

    # data = data.insert()


def removeBook(ID, bookName):
    data_raw = pd.read_excel("rented.xlsx")
    data = data_raw.to_numpy()
    curr_users = []
    for item in data:
        curr_users.append(item[0])
    i = curr_users.index(ID)
    for j, item in enumerate(data[i]):
        if item == bookName:
            break
    arr = []
    for item in data:
        arr.append(item[j])
    
    data_raw.pop(j)
    
    arr[i] = ""

    data_raw.insert(j, j, arr)
    data_raw.to_excel("rented.xlsx", index=False)

def showUser(ID):
    data_raw = pd.read_excel("rented.xlsx")
    data = data_raw.to_numpy()
    curr_users = []
    for item in data:
        curr_users.append(item[0])
    i = curr_users.index(ID)
    print(data[i])

def showAll():
    data_raw = pd.read_excel("rented.xlsx")
    print(data_raw)
    
    

# addBook(101, "NightFall")

# removeBook(101, "NightFall")

# showUser(101)

showAll()

