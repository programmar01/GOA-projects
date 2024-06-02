def mine_location(f):
    arr = []
    for col in range(len(f)):
        for row in range(len(f[col])):
            if f[col][row] == 1:
                arr.append(col)
                arr.append(row)
    return arr