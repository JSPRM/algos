class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=""
        r=""
        izq = 0
        der = 0
        while(der < len(s)):
            if s[der] in r:
                r=""
                izq +=1
            r += s[der]
            if len(r)>len(result):
                result= r
            der += 1
        return result
            
        
    
def lengthOfLongestSubstring(s: str) -> int:
        usado = {}
        resultado = inicio = 0
        for i,char in enumerate(s):
            if char in usado and inicio <= usado[char]:
                inicio = usado[char] + 1
            else:
                resultado = max(resultado, i - inicio + 1)
            usado[char] = i
        return resultado
            


if __name__ == "__main__":
    r = "dvdf"
    print(lengthOfLongestSubstring(r))
    