def dirReduc(arr):
    a = {'SOUTH':'NORTH', 'NORTH':'SOUTH', 'WEST':'EAST','EAST':'WEST'}
    k = 0
    while k != len(arr)-1:
        i = arr[k]
        if a[i] == arr[k+1]:
            arr.remove(a[i])
            arr.remove(i)
            k -= 1
        else: k += 1
    return arr
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))