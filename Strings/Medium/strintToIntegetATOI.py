# String to integer (atoi)


# optimal appoach 
# TC = O(2N) and SC = O(1)
def atoi(s):
    i = 0
    n = len(s)
    while i < n and s[i] == " ":
        i +=1
    sign = 1
    if i < n and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i +=1  
    num = 0
    int_max = 2**31 -1
    int_min = -2**31
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord("0")
        if num > int_max//10 or (num == int_max//10 and s[i] > "7"):
            return int_max if sign == 1 else int_min
        num = num * 10 + digit
        i +=1
    return sign * num