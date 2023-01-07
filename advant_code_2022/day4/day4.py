def find_filly_overlap_part1(ls:list[str]):
    e1 = ls[0]
    e2 = ls[1]

    min1,max1 = e1.split('-')
    min2,max2 = e2.split('-')

    if int(min1) <= int(min2) and int(max1) >= int(max2):
        return True
    elif int(min2) <= int(min1) and int(max2) >= int(max1):
        return True
    else:
        return False

def is_overlap_part2(ls:list[str]):
    e1 = ls[0]
    e2 = ls[1]

    min1,max1 = e1.split('-')
    min2,max2 = e2.split('-')

    if int(min1) > int(max2) or int(max1)<int(min2):
        return False      
    else:
        return True       

with open('./advant_code_2022/day4/input.txt') as f: 
    sum = 0
    for line in f.readlines():
       ls =line.strip().split(',')
       res = find_filly_overlap_part1(ls)
       if res:
        sum = sum +1
    #print(sum)

with open('./advant_code_2022/day4/input.txt') as f: 
    sum = 0
    for line in f.readlines():     
       ls =line.strip().split(',')
       print(ls)
       print(type(ls))
       res = is_overlap_part2(ls)
       print(res)
       if res:
        sum = sum +1
    print(sum)

