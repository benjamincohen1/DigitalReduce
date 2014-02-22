def letter_count(data):

    chars = {chr(x + 97): 0 for x in range(26)}

    for c in data:
        if ord(c) < 97 or ord(c) > (97 + 26):
            pass
        else:
            chars[c.lower()] += 1
    # for x in sorted(chars.keys()):
    #     print str(x) + ": " + str(chars[x])


    return chars


print letter_count(open('out.txt').readline())