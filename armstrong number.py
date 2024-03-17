num = int(input('Enter the number: '))
leng = len(str(num))
sum = 0
new_num = num

for a in range(1 , leng + 1):
    x = (new_num % 10)**leng
    sum += x
    new_num = new_num // 10

if sum == num:
    print(str(num) + ' is an armstrong number.')
else:
    print(str(num) + ' is not an armstrong number.')
