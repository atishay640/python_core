# for loop
# use for itration

# for loop with list
alist = [4,5,6,4,5,5,5,21,5,4,21,5]
flag = 0

while flag < 10:
    print(flag)
    flag += 1
else:
    print(" >= 10")

print('---------------------------------')
name = 'vikas cing'

for ch in name:
    print(ch)


print('--------------break, continue and pass keyword------------------')

# break : to come out from current loop
# continue : to come at the top of the loop
# pass : does nothing

for a in alist:
    # nothing is there
    pass
print('-------------------------------')

for a in alist:
    print(a)
    if a == 21:
        break
print('-------------------------------')

for a in alist:
    if a == 21:
        continue
    print(a)
print('-------------------------------')
