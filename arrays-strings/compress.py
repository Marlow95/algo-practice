def compress(s):

    s += '!'
    result = []
    j = 0
    i = 0

    while j < len(s):
        
        if s[j] == s[i]:

            j += 1

        else:

            num = j - i

            if num == 1:

                result.append(s[i])
            
            else:

                result.append(str(num))
                result.append(s[i])
            i = j
    
    return ''.join(result)

print(compress('ccaaat'))