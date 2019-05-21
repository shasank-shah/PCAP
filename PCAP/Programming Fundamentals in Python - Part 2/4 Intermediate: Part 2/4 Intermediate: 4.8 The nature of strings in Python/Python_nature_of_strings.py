word = 'by'
print(len(word))

empty = ''
print(len(empty))

I_am = 'I\'m'
print(len(I_am))

str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

c1 = 'a'
print(ord(c1))

print(chr(99))

string = 'silly walks'
for ix in range(len(string)):
    print(string[ix], end=' ')
print()

lst = []
for indx in range(len(string)):
    lst.insert(0, string[indx])

print(lst)

lst = []
for indx in range(len(string)):
    lst.append(string[indx])

print(lst)