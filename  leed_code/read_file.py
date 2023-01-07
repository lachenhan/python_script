fname = input("Enter file name: ")
fh = open(fname)
for f in fh:
    print(f.upper().rstrip())