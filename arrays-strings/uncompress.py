def uncompress(s):
    #input "2c3a1t"
    # output ccaaat
    # array
    # two pointers
    
    result = []
    numbers = '0123456789'
    i = 0
    j = 0

    while j < len(s):

        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j

    return ''.join(result)


print(uncompress("2c3a1t"))
