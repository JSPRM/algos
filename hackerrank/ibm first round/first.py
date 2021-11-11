
from collections import deque 

def backspace(s1: str) -> str:
    res = deque()
    for val in s1:
        if val == "#" and len(res) >0:
            res.pop()
        else:
            if val != "#":
                res.append(val)
    return res


def compareStrings(s1: str, s2: str) -> bool:
    uno = backspace(s1)
    dos = backspace(s2)
    if uno == dos:
        return 1
    else:
        return 0
            
if __name__ == "__main__":
    uno = "yf#c#"
    dos = "yy#k#pp##"
    print(compareStrings(uno,dos))
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s1 = input()

#     s2 = input()

#     result = compareStrings(s1, s2)

#     fptr.write(str(result) + '\n')

#     fptr.close()