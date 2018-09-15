def emicalculator():
    p=int(input('enter amount'))
    rate=float(input('enter rate of interest'))
    t=int(input('enter no of years'))
    r=rate/(12*100)
    n=t*12
    EMI=(p*r* pow(1+r,n))/(pow(1+r,n)-1)
    print('Monthly emi is=',EMI)
emicalculator()
