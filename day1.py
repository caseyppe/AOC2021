lines = open("input.txt","r").read().splitlines()
deep = 0
cumdeep = 0
x=0
for depth in lines:
    lines[x] = int(depth)
    if x>0:
        if lines[x] > lines[x-1]:
            deep+=1
    if x>2:
        if lines[x-3]+lines[x-2]+lines[x-1] < lines[x]+lines[x-2]+lines[x-1]:
            cumdeep+=1
    x+=1

print('there are ' + str(deep) + 'deeper spaces')
print('there are ' + str(cumdeep) + 'deeper spaces')
