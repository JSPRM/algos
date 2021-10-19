def birthdayCakeCandles(candles):
    count=0
    max=0
    for i in candles:
        if max == i:
            count+=1
        if max<i:
            max = i
            count=1
    return count
    
if __name__ == "__main__":
    arr=[3,2,1,3]
    birthdayCakeCandles(arr)