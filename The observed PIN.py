from itertools import product as p

s = {1:[1,2,4], 2:[2,1,5,3], 3:[3,2,6], 4:[4,1,5,7], 5:[5,2,4,6,8], 6:[6,3,5,9], 7:[7,4,8], 8:[8,7,5,9,0], 9:[9,8,6], 0:[0, 8]}

def get_pins(observed):
    return [''.join(map(str, i)) for i in list(p(*[s[int(i)] for i in str(observed)]))]
print(get_pins(8))