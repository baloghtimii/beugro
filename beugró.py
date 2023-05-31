#1 feladat
with open('autok.txt', 'r') as file:
    lines = file.readlines()

data = []
for i in lines:
    data.append(i.split(';'))
for i in data:
    print(i)
#2 feladat
ossz = len(lines)
print(f'Összesen {ossz} ki be hajtás történt')

#3 feladat
counter = 0
for i in data:
    if i[2] == 'CEG301':
        counter += 1
print(f'A CEG301 autót összesen {counter}-szer vitték el')