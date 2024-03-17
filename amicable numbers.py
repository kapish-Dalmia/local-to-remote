a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))
sum1 = 0
sum2 = 0


#factors of 1st number:

for i in range(1, a//2 + 1):
    if a % i == 0 :
        sum1 += i
    else:
        continue

#factors of 2nd number:

for i in range(1, b//2 + 1):
    if b % i == 0 :
        sum2 += i
    else:
        continue

if sum1 == b and sum2 == a:
    print('The given pair of numbers are amicable.')
else:
    print('The given two pairs of numbers are not amicable.')
