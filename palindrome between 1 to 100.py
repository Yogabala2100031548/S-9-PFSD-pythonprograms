n = int(input(" Please Enter the Maximum Value : "))
print("Palindrome Numbers between 1 and %d are : " %(n))
for num in range(1, n + 1):
    temp = n
    rev = 0
while(n > 0):
        dig = n % 10
        rev = (rev * 10) + dig
        n = n //10
if(num == rev):
        print("%d " %num, end = '  ')