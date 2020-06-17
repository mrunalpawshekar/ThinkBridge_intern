one=["zero","one","two","three","four","five","six","seven","eigth","nine"]
two_digit=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
ten_mul=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eigthy","ninty"]
ten_power=["hundred","thousand"]
l=0   #to set limits
b=0   #last place
c=0   #first place
d=0   #mid place

print("enter amount")
str1=float(input())
x=str1   
y=int(x)     #to separate integer values from decimal
z=(x-y)*100  #float to int
zd=round((z))  

n1=int(str1)
n2=int(str1)
length=0
while(n1>0):    #finding length of str
    length+=1
    n1%10
    n1//=10     #send int value of quotient 
if length==1:
    print(one[n])
if length==2:
    b=n2%10         #store last place
    while(n2>0):    # to find first place
        c=n2%10     #store first place  ,it continuosly changes till n2=0
        n2//=10     #take quotient 
    if b==0:        #if last place is 0 then print multiples of tens
        print(ten_mul[c])
    if c==1:        #if first place is 1 print fron 10-19
        print(two_digit[b])
    if b!=0 and c!=1:  # if first !=1 and last !=0 print nos accordingly
        print(ten_mul[c],one[b])
if length==3:
    b=n2%10
    while(n2>0):
        c=n2%10
        d=n2%10
        n2//=10
        l+=1 
        if(l==2): #to set limit for 2nd place
            e=d    #store mid value
    print(one[c],ten_power[0], "and",ten_mul[e],one[b],end="")
if length==4:
    b=n2%10
    while(n2>0):
        e=d=c=n2%10
        n2//=10
        l+=1
        if(l==2):
            f=d
        if(l==3):
            g=e
    print(one[c],ten_power[1],one[g],ten_power[0], "and",ten_mul[f],one[b],end="")
if length==5:
    b=n2%10
    while(n2>0):
        f=e=d=c=n2%10
        n2//=10
        l+=1
        if(l==2):
            g=d
        if(l==3):
            h=e
        if(l==4):
            j=f
    if c==1:
        print("RS", two_digit[j],ten_power[1],one[h],ten_power[0],"and",ten_mul[g],one[b],end="")
    if j==0:
        print("RS", ten_mul[c],ten_power[1],one[h],ten_power[0],"and",ten_mul[g],one[b],end="")
    if c!=1 and j!=0:
         print("RS" ,ten_mul[c],one[j],ten_power[1],one[h],ten_power[0],"and",ten_mul[g],one[b],end="")
print(" ",zd,"/100")




    

            
        
        
        
        
        
        

        
        
 
    

    
