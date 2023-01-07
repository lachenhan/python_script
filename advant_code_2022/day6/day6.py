with open('./advant_code_2022/day6/input.txt') as f: 
    line = f.readlines()[0]

s = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
#print(len(s))





def find_x_diff_char(s:str, x:int):
    for n in range(x,len(s)+1):
        if len(set(s[n-x:n])) == x:
            return n

def find_x_diff_char_2(s:str, x:int):
    for n in range(x,len(s)+1):
        d = dict((c,i) for i,c in enumerate(s[n-x:n]))
        if len(d) == x:

            return n    

print(find_x_diff_char(s,14))
print(find_x_diff_char_2(s,14))


