#program to print 1 to 10 tables using NESTED LOOP

for i in range(1, 11):
    for j in range(i, (i*10)+1, i):
            print(j, end="\t")
    print()