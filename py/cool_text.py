import time 

def cool_print(s):
    alphabet = list(chr(i) for i in range(32, 127))
    res = ""
    for i in range(0, len(s)):
        for j in alphabet:
            if j == s[i]:
                res += j
                print(res)
                break
            else:
                print(res + j)
            time.sleep(0.01)

cool_print(input("input something to be printed: "))
input("\nctrl + c to close")