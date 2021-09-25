password = input()

weak = []
for i in range(10):
    weak.append(str(i) * 4)
    increase = ''
    for j in range(4):
        increase += str((i + j) % 10)
    weak.append(increase)

if password in weak:
    print('Weak')
else:
    print('Strong')

