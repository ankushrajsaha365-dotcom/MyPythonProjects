num = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

with open('xyz.txt', "w") as mf2:
    for c in num:
        mf2.write("%s," % c)

c = open('xyz.txt')

word=c.read()

print(word.split(','))

mf2.close()