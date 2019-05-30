A = input()
B = input()

l1 = int(A)*int(B[2])
l2 = int(A)*int(B[1])
l3 = int(A)*int(B[0])
l4 = l3*100 + l2*10 + l1
print(l1,l2,l3,l4, sep = '\n')
