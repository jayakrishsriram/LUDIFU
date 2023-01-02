def average(a):
    b= sum(a)/len(a)
    print('Average:',b)
c=list(map(int,input('Enter the number:').split()))
average(c)