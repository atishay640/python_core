# for loop
# use for itration

# for loop with list
alist = [4,5,6,4,5,5,5,21,5,4,21,5]

for a in alist:
    print(a)

print('----------------------------------------')
# for loop in tuple

atuple = (4,4,5,2,58,12,58,21,45)

for b in atuple:
    print(b)

print('--------------find even and odd --------------------------')

#
for num in alist:
    if num%2==0:
        print('even :', num)
    else:
        print('odd :', num)


print('-------------- Nested loop --------------------------')

alist = [(1,2),(3,32),(11,25),(61,72),(31,24)]
for atup in alist:
    for num in atup:
        print(num)

print('-------------- loop  for inner tuple --------------------------')

for (a,b) in alist:
    print(a, b)

print('-------------- loop  for dictionary --------------------------')

adic = {'key1' : 15 , 'key2' : 4 , 'key3' :46 , 'key4' : 44 }

for k,v in adic.items():
    print('key: ', k , 'values:' , v)
