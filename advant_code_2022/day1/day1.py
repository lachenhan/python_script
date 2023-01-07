

with open('./advant_code_2022/day1/input.txt') as f:
    lines = f.readlines()

sum_ls = []
sum = 0

lines.append('\n')
for line in lines:
    if line != '\n' :
        sum = sum + int(line)
    else:
        sum_ls.append(sum)
        sum = 0


def find_second_large_number(ls:list):
    max_v = max(ls)
    x = 0
    for i in ls:
        i = int(i)
        if i > x and i < max_v:
            x = i
    return x


sum_ls.remove(66306)

print(find_second_large_number(sum_ls))


print(66306 + 64532 + 64454)