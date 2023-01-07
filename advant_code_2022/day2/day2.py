def cal_score_part1(ls: list[str]):
    """
    A for Rock, B for Paper, and C for Scissors
    X for Rock, Y for Paper, and Z for Scissors
    1 for Rock, 2 for Paper, and 3 for Scissors
    """
    op = ls[0]
    you = ls[1]
    if op.strip() == 'A' and you.strip()== 'X':
        return 4
    if op.strip() == 'B' and you.strip()== 'Y':
        return 5
    if op.strip() == 'C' and you.strip()== 'Z':
        return 6

    if op.strip() == 'A' and you.strip()== 'Y':
        return 8
    if op.strip() == 'B' and you.strip()== 'Z':
        return 9
    if op.strip() == 'C' and you.strip()== 'X':
        return 7

    if op.strip() == 'A' and you.strip()== 'Z':
        return 3
    if op.strip() == 'B' and you.strip()== 'X':
        return 1
    if op.strip() == 'C' and you.strip()== 'Y':
        return 2

def cal_score_part2(ls: list[str]):
    op = ls[0]
    you = ls[1]

    # end with a draaw
    if op.strip() == 'A' and you.strip()== 'Y':
        return 4
    if op.strip() == 'B' and you.strip()== 'Y':
        return 5
    if op.strip() == 'C' and you.strip()== 'Y':
        return 6

    # you win
    if op.strip() == 'A' and you.strip()== 'Z':
        return 8
    if op.strip() == 'B' and you.strip()== 'Z':
        return 9
    if op.strip() == 'C' and you.strip()== 'Z':
        return 7

    # you lose
    if op.strip() == 'A' and you.strip()== 'X':
        return 3
    if op.strip() == 'B' and you.strip()== 'X':
        return 1
    if op.strip() == 'C' and you.strip()== 'X':
        return 2


with open('./advant_code_2022/day2/input.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        score = cal_score_part2(line.strip().split(' '))
        sum = sum  + score

    print(sum)