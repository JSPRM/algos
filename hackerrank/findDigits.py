def findDigits(n):
    digits=  len(str(n))
    for i in range(0,digits):
        print((n//pow(10,i)%10))

if __name__ == "__main__":
    print(findDigits(1223))