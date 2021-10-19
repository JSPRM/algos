def staircase(n):
    char="#"
    for i in range(0,n):
        print("%*s" %(n,char))
        char+="#"

if __name__ == "__main__":
    staircase(4)
    arr=[1,2,3,4]
    for i,val in enumerate(arr):
        print(i)