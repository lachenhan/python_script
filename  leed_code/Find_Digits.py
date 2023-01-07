

fname = input("Enter file name: ")
fh = open(fname)
dig = 0
c = 0
def find_digit(x):
    c = 0
    r = ""
    for e in x:
        if e.isdigit():
            r = x[c : ]
            break
        c = c + 1
    return r 
    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    dig = dig + float(find_digit(line))
    c = c + 1

r = dig/c

print("Average spam confidence:", r)





