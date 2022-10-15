#https://www.wechall.net/challenge/training/prime_factory/index.php
def isPrime(a):
    for i in range(2,a):
        if (a%i)==0:
            return False
    return True


list1=[]
list2=[]
dictionary={}
for i in range(1000000,1000050,1):
    if isPrime(i)==True:
        list1.append(i)
for i in list1:
    sum = 0
    for x in str(i):
        sum+=int(x)
    list2.append(sum)

for i in range(0,len(list1)):
    dictionary[list1[i]]=list2[i]
print(dictionary)