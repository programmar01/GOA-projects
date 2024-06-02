def rot13(m):

    labc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    uabc = ''
    for i in labc:
        uabc += i.upper()
    con = labc + uabc
    fabc = ''
    
    for char in m:
        if char in con:
            fabc += con[con.index(char) + 13]
        else:
            fabc += char
    
    return fabc
