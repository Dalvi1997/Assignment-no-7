def details():
    name=input('enter name')
    roll=int(input('enter roll no'))
    
    l=[]
    n=int(input('enter number of subjects'))
    print('enter values')
    for i in range(n):
        l.append(int(input()))
    sum=0
    for  each in l:
        sum=sum+each
    x =(sum/(n*100))*100
    print ("percent=",x)
    if(x>=60):
        print("grade= first class")
    elif(x>=40):
        print("grade=second class")
    else:
        print("fail")


def percentage():
    details()
    
def display():
    percentage()
display()
    

