def create_list(x:int):
    l = [[]]
    for n in range(1,x+1):  
        ls = []
        with open('./advant_code_2022/day5/list.txt') as f: 
            lines = f.readlines()[:-1]
            for line in lines:
                for i, c in enumerate(line):
                    if i == n+3*(n-1):
                        if c.strip() != '':
                            ls.append(c)
                        else:
                            pass
        ls.reverse()
        l.append(ls)
    return l



def move_x_times(from_ls: list, to_ls: list, x: int):
    count = 0
    while count < x:
        e = from_ls.pop()
        to_ls.append(e)
        count = count + 1


def move(from_ls: list, to_ls: list, x: int):
    l = []
    count = 0
    while count < x:
        e = from_ls.pop()
        l.append(e)
        count = count + 1
    l.reverse()
    to_ls.extend(l)



final_l = create_list(9)
print(final_l)


##part 1
"""
with open('./advant_code_2022/day5/input.txt') as f: 
    lines = f.readlines()

for line in lines:
    ls = line.strip().split(' ')
    f = int(ls[-3])
    t = int(ls[-1])
    time = int(ls[1])
    #print(f,t,time)
    move_x_times(final_l[f],final_l[t],int(ls[1]))

print( final_l[1:])
for x in final_l[1:]:
    print(x[-1],end='')
"""

##part 2
with open('./advant_code_2022/day5/input.txt') as f: 
    lines = f.readlines()

for line in lines:
    ls = line.strip().split(' ')
    f = int(ls[-3])
    t = int(ls[-1])
    time = int(ls[1])
    #print(f,t,time)
    move(final_l[f],final_l[t],int(ls[1]))

print( final_l[1:])
for x in final_l[1:]:
    print(x[-1],end='')
