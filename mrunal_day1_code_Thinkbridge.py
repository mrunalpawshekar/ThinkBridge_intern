#   Write a program that takes a number like 12345.67 and prints "Rs. Twelve Thousand Three Hundred Forty Five and 67/100"
# Author : Mrunal Pawshekar
# language : Python
one=["zero","one","two","three","four","five","six","seven","eigth","nine"]
two_digit=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
ten_mul=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eigthy","ninty"]
ten_power=["hundred","thousand","lakh","crore"]
print("enter amount")
str1=float(input())
x=str1   
y=int(x)     #to separate integer values from decimal
z=(x-y)*100  #float to int
zd=round((z))
n1=int(str1)
n2=int(str1)
def finding(n1):
    length=0
    limit=0#to set limits
    mid2=0
    mid3=0
    mid4=0
    mid5=0
    last=n1%10      #store last place
    while(n1>0):    #finding length of str
        length+=1
        first=n1%10 #store first place  ,it continuosly changes till n2=0
        n1//=10     #takes quotient
        limit+=1 
        if(limit==2): #to set limit for 2nd place
           mid2=first    #store mid value-mid2
        if(limit==3):
            mid3=first
        if(limit==4):
            mid4=first
        if(limit==5):
            mid5=first
            
    return length,first,mid2,mid3,mid4,last,mid5
length,first,mid2,mid3,mid4,last,mid5=finding(n1)    #to find length of str #send int value of quotient 
if length==1:
    print(one[n1])
if length==2:
    if last==0:         #if last place is 0 then print multiples of tens
        print(ten_mul[first])
    if first==1:        #if first place is 1 print fron 10-19
        print(two_digit[last])
    if last!=0 and first!=1:    #if first !=1 and last !=0 print nos accordingly
        print(ten_mul[first],one[last])
if length==3:
    print(one[first],ten_power[0], "and",ten_mul[mid2],one[last],end="")
if length==4:
    print(one[first],ten_power[1],one[mid3],ten_power[0], "and",ten_mul[mid2],one[last],end="")
if length==5: 
    if first==1:
        print("RS", two_digit[mid4],ten_power[1],one[mid3],ten_power[0],"and",ten_mul[mid2],one[last],end="")
    if mid4==0:
        print("RS", ten_mul[first],ten_power[1],one[mid3],ten_power[0],"and",ten_mul[mid2],one[last],end="")
    if first!=1 and mid4!=0:
         print("RS" ,ten_mul[first],one[mid4],ten_power[1],one[mid3],ten_power[0],"and",ten_mul[mid2],one[last],end="")
if length==6:
     if first==1:
         print("RS" ,one[first],ten_power[2],ten_mul[mid5],one[mid4],ten_power[1],one[mid3],ten_power[0],ten_mul[mid2], one[last])
     if mid5==0:
         print("RS", one[first],ten_power[2],one[mid4],ten_power[1],one[mid3],ten_power[0],ten_mul[mid2],one[last])
     if first!=1 and mid5!=0 and mid5==1:
         print("RS" ,one[first],ten_power[2],two_digit[mid4],ten_power[1],one[mid3],ten_power[0],ten_mul[mid2],one[last])
     if first!=1 and mid5!=0 and mid4==0:
         print("RS" ,one[first],ten_power[2],ten_mul[mid5],ten_power[1],one[mid3],ten_power[0],ten_mul[mid2],one[last])
     if first!=1 and mid5!=0 and mid4!=0:
         print("RS", one[first],ten_power[2],ten_mul[mid5],one[mid4],ten_power[1],one[mid3],ten_power[0],ten_mul[mid2],one[last])
print(" ",zd,"/100")




    

            
        
        
        
        
        
        

        
        
 
    

    
