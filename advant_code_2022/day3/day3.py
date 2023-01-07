def cal_letter_num(l: str):
    if l.islower():
        return ord(l) - 96
    else:
        return ord(l) - 38

    
def find_common_letter(s: str):
    s1, s2 = s[:len(s)//2], s[len(s)//2:]
    for l1 in s1:
        for l2 in s2:
            if l1 == l2:
                return cal_letter_num(l1)

def find_common_letter_in_list_with_3ele(ls: list[str]):   
    s1 = ls[0]
    s2 = ls[1]
    s3 = ls[2]
    for l1 in s1:
        for l2 in s2:
            for l3 in s3:
                if l1 == l2 == l3:
                    return cal_letter_num(l1)

# part 1
with open('./advant_code_2022/day3/input.txt') as f:
    sum = 0
    for line in f.readlines():
        sum = sum + find_common_letter(line.strip())
    #print(sum)


# part 2
with open('./advant_code_2022/day3/input.txt') as f:
    sum = 0
    lines = f.readlines()
    ls = [','.join(lines[i:i+3]) for i in range(0, len(lines), 3)]
    
    for l in ls:
        l_list = l.split(',')

        print(l_list)
        sum = sum + find_common_letter_in_list_with_3ele(l_list)
    print(sum)