a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
value=int(input("enter value"))
start=a[0]
end=a[-1]
mid=0
if((value==start)or(value==end)):
    print("yes")
if(value>end):
    print("sorry")
if(value<start):
    print("sorry")
if((value<end)and(value>start)):
    while(mid!=value):    
        n=0
        while(n<len(a)):
            n=n+1
            mid=(start+end)/2
            if(value==mid):
                print("yes")
                break
            if (value>mid):
                start=mid
            if(value<mid):
                end=mid
print(start,end,n)                