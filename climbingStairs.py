def climbStairs(n: int,x:int = 3,xd:list =[1,2]) -> int:
    sum=xd[x-3]+xd[x-2]
    xd.append(sum)
    if n>x:
        return climbStairs(n,x+1,xd)
    else:
        return xd[n-1]

if __name__ == "__main__":
    print(climbStairs(4))