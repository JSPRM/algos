def miniMaxSum(arr):
    min=0
    max=0
    sum=0
    for i,val in enumerate(arr):
        sum+=val
        if min > val or i==0:
            min = val
        if max< val:
            max=val
    print(sum-max,sum-min)  