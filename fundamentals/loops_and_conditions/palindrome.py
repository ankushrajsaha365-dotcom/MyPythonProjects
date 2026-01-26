## Check whether a given number is a palindrome.


num = int(input("Enter a number:"))
rev = 0
n = num
while num!= 0:
    rem = num%10
    rev = rev*10 + rem
    num//=10

if n == rev:
    print("The given number is a Palindrome")
else:
    print("The given number isn't a Palindrome")