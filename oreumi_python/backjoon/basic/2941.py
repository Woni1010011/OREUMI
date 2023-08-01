string = input()

li = ['c=', 'c-', 'dz=', 'd-', 'lj', 's=', 'z=', 'nj']

for i in li :
    string = string.replace(i, "*")

print(len(string))
    
