from fractions import gcd
lst = (input()).split('=')
r, l = lst[0], lst[1]
r, l = list(r), list(l)
if r[0] != '-':
    r.insert(0, '+')
if l[0] != '-':
    l.insert(0, '+')
for i in range(len(l)):
    if l[i] == '+':
        l[i] = '-'
        continue
    if l[i] == '-':
        l[i] = '+'
new = list("".join(r) + "".join(l))
count_x = number = 0
while 'x' in new:
    for i in range(len(new)):  # count x
        minez = 1
        if new[i] == 'x':
            while new[i-minez] not in ['+', '-']:
                minez += 1
            su = "".join(new[i-minez+1:i])
            if su == "":
                su = "1"
            if new[i-minez] == '+':
                count_x += int(su)
            else:
                count_x -= int(su)
            del new[i-minez:i+1]
            break
if count_x == 0:
    print("invalid")
    exit(0)
i = 1
while i != len(new)-1 and len(new) != 0:
    for i in range(1, len(new)):  # count x
        if new[i] in ['+', '-']:
            if new[0] == '+':
                number += int("".join(new[1:i]))
            else:
                number -= int("".join(new[1:i]))
            del new[0:i]
            break
if len(new) != 0:
    if new[0] == '+':
        number += int("".join(new[1:]))
    else:
        number -= int("".join(new[1:]))
div = gcd(abs(count_x), abs(number))
count_x //= div
number //= div
number *= -1
if count_x < 0:
    number *= -1
print(number, end=" ")
print(abs(count_x))
exit_program = input("Enter to close")
