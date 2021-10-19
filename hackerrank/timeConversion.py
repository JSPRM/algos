
def timeConversion(s):
    hora = int(s[:2]) % 12
    if s[-2:] == "PM":
        hora += 12
    return f"{hora:>02}" + s[2:-2]
    
if __name__ == "__main__":
    print(timeConversion("13:05:45AM"))
