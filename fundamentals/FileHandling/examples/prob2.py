num = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

with open('abc.txt', "w") as mf:
    for c in num:
        mf.write("%s\n" % c)

c = open('abc.txt')

print(c.read())