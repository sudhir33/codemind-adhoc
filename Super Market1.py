n=int(input())
cus=list(map(int,input().split()))#[1,2,3,1,2,3,4,3,2,4,5,6]
top=int(input())

l=list(set(cus))
l.sort()
arr=[]
for i in l:
    arr.append(cus.count(i))


for i in range(1, len(arr)):
    key = arr[i]
    k1=l[i]
    j = i-1
    while j >= 0 and key < arr[j] :
        arr[j + 1] = arr[j]
        l[j+1]=l[j]
        j -= 1
        arr[j + 1] = key
        l[j+1]=k1
   

print(*l[-1:-top-1:-1])