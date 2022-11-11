credit_card = input("enter credit card: ")
reverse = credit_card[::-1]
odd = 0
b = []
d = []
for i in range(len(reverse)):
    if i % 2 == 0:
        odd += int(reverse[i])
    else:
        b.append(int(reverse[i]) * 2)
for j in b:
    if j > 9:
        c = int(str(j)[0]) + int(str(j)[1])
        d.append(str(c))
    else:
        d.append(j)
if (sum(map(int,d)) + odd) % 10 == 0:
    print("valid credit card")
else:
    print("invalid credit card")
