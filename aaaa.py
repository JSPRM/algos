class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        uno,dos,tres = 1,2,0
        while(n>2):
            tres=uno+dos
            uno = dos
            dos = tres
            n -=1
        return tres
    
if __name__ == "__main__":
    hola = Solution()
    print(hola.climbStairs(5))