num = int(input())
computers = []
sums = []
pref = []
temp1 = 1000000
temp2 = 1000000
index = -1000000
first = -1000000

for i in range(num):
    inp = input()
    inp = inp.split(" ")
    computers.append(inp)

for i in range(num):
    for j in range(1, 4):
        computers[i][j] = int(computers[i][j])

for i in range(num):
    sums.append(computers[i][1]*2 + computers[i][2]*3 + computers[i][3])

for i in range(2):
    index = -1000000
    for j in range(num):
        if j == 0:
            if sums[j] > sums[j + 1]:
                index = j
            elif sums[j + 1] > sums[j]:
                index = j + 1
            elif sums[j] == sums[j + 1]:
                if len(computers[j][0]) < len(computers[j+1][0]):
                    index = j+1
                elif len(computers[j][0]) >= len(computers[j+1][0]):
                    index = j
            elif num == 2:
                if first == 0:
                    first = 1
                else:
                    first = 0
                break
        else:
            if sums[j] >= sums[index] and index != j and sums[j] <= temp1 and j != first:
                if sums[j] == sums[index]:
                    if len(computers[j][0]) > len(computers[index][0]):
                        index = j
                else:
                    index = j
    pref.append(computers[index][0])
    if i == 0:
        first = index
        temp1 = sums[index]
    else:
        if num == 2:
            temp2 = sums[first]
        else:
            temp2 = sums[index]

if temp1 == temp2:
    if len(pref[0]) < len(pref[1]):
        print(pref[1] + "\n" + pref[0])
    elif len(pref[0]) >= len(pref[1]):
        print(pref[0] + "\n" + pref[1])
else:
    print(pref[0] + "\n" + pref[1])
        
