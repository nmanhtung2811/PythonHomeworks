for i in range(1, 10):
    print('\t', i, end='\t')
print()
print("-----------------------------------------------------------------------\n")
for k in range(1, 10):
    print(k, "|")
    for l in range(1, 10):
        print('\t', k*l, end='\t')
    print("\n")