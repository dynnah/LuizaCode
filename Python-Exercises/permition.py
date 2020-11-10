def PermutationsStep(num):
    
    string = str(num)
    if len(string) == 1:
        return -1
    for i in range(len(string)-2,-1,-1):
        if string[i] < string[i+1]:
            return int(string[:i] + string[i+1:] + string[i])
    else:
        return -1