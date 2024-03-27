def snail(snail_map):
    map = snail_map
    a = []
    if len(map) > 1:
        while len(map)>1:
            a += map[0]
            map.remove(map[0])
            for i in map:
                a += [i[-1]]
                i.pop()
            a += list(reversed(map[-1]))
            map.pop()
            for i in list(reversed(map)):
                a += [i[0]]
                i.remove(i[0])
            if map and len(map[0]) == 1:
                a += map[0]
    else: a = map[0]
    return a
print(snail([[1,2,3,2,1],
             [4,5,6,3,6],
             [7,8,9,6,8],
             [1,2,3,2,1],
             [7,8,9,6,8]]))