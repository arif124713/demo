list= []


def add_item():
    l=input("enter the task: ")
    list.append(l)

def remove_item():
    m=int(input("enter index no.: "))
    del list[m]

def view_list():
    print(list)
A= False
while(A==False):
    k= int(input("Hey welcome \n 1.Add item \n 2.remove item \n 3.view list \n  type number only: "))

    if (k==1):
        add_item()
    elif (k==2):
        remove_item()
    elif(k==3):
        view_list()
    else:
        A=True