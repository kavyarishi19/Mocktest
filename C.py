t = int(input())
for i in range(t):
    N = int(input())
    i = 1
    m=0
    arr=[]
    while i*i <= N:
        j = 1
        while (j*j<=N):
            if (i*i + j*j ==N):
                if i<=j :
                    
                arr.append(i)
                arr.append(j)

                m+=1
            if(m==2):
                break
            j = j+1
        if(m==2):
            break
        i = i+1
    if(m==2 and arr[3]>arr[1] and arr[0]!=arr[3]):
        print(arr[0]," ",arr[1]," ",arr[2]," ",arr[3])
    elif(m==2 and arr[3]<arr[1] and arr[0]!=arr[3]):
        print(arr[2]," ",arr[3]," ",arr[0]," ",arr[1])
    else:
        print(-1," ",-1,"",-1," ",-1)
