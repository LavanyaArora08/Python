#program 1
Basket=["Apple","Potato","Carrot"]
print (Basket[1])
#program 2
L=[1,2,5,4,"a","dog","cat","lion"]
print(L[1:8:2])
print(L[-1::-2])
#program 3
f="apple"
print(L[5] + f[1:3])
a="MZSSISSIPPI"
print(a[1:8:3])
#program 4
sub=[]
for i in range(5):
   a=input("Enter sub")
   sub.append(a)
print(sub)
#program 5
li=[1,2,3,3,3,4,5]
for i in range(len(li)):
    if 3 in li:
        li.remove(3)
print(li)
#program 6
newlist=[]
flat=[[1,2],["Apple","Orange"],["potato","cow"]]
for i in range(len(flat)):
    newlist.extend(flat[i])
print(newlist)
#program 7
abc=[1,2,3,4,7,8]
for i in range(len(abc)):
    if abc[i]==1 :
        print ("ONE")
    else:
        if abc[i]==2:
            print("TWO")
        else:
            if abc[i]==3:
                print ("Three")
            else:
                if abc[i]==7:
                    print ("Seven") 
                else:
                    if abc[i]==8:
                        print ("Eight")
#program 8
max=[23,12,45,67,55]
temp=max[0]
for i in range(len(max)):
    if temp>max[i]:
        temp=temp
    else :
        temp=max[i]
print(temp)
#program 9
listt=[]
square=[]
print("Enter 10 number")
for i in range(10):
   num=int(input())
   if num%2==1:
       listt.append(num)
   sq=num*num
   square.append([num,sq])
print (listt)
print (square)
#program 10
sum = 0
matrix=[]
a=[]
for i in range(3):
    for j in range (3):
        a=int(input())
        matrix.append([a,a])
        sum+=2*a
print(matrix)
print(sum)
#program 11
a=int(input("Enter the number "))
if(a==0):
    print("Number is 0 ")
elif (a%2==0):
    print("Number is even")
else:
    print("Number is odd")
#program 12
a= 55
if a>=0:
    if a==0:
        print("Zero")
    else :
        print("Positive")
else:
    print("Negative")
#program 13
i=1
sum=0
while i<=5:
    sum=sum+i
    i=i+1
print("sum= ",sum)
#program 14
l=["Papaya","Orange","MANGO"]
for i in range(3):
    
    if l[i]=="Orange":
        continue
    print(l[i])

#program 15
a=int(input("Enter the number "))
if(a==0):
    print("Number is 0 ")
elif (a%2==0):
    print("Number is even")
else:
    print("Number is odd")
#program 16
reversee=[1,2,3,4,5]
reversee2=list(reversed(reversee))
print(reversee2)
#program 17
for i in range (5):
    if i %2==0 :
        pass
    else: 
        print (i)
#program 18

for i in range(5):
    print(i)