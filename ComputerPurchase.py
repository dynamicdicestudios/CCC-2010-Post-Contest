num = int(input())
computers = []
sums = []
pref = ["", ""]
temp1 = 10000000
temp2 = 10000000
index = -10000000
first = -10000000

for i in range(num):
    inp = input()
    inp = inp.split(" ")
    computers.append(inp)

for i in range(num):
    for j in range(1, 4):
        computers[i][j] = int(computers[i][j])
    sums.append(computers[i][1]*2 + computers[i][2]*3 + computers[i][3])
if num != 1:
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
            else:
                if num == 2:
                    if first == 0:
                        first = 1
                    else:
                        first = 0
                    break
                elif sums[j] >= sums[index] and index != j and sums[j] <= temp1 and j != first:
                    if sums[j] == sums[index]:
                        if len(computers[j][0]) > len(computers[index][0]):
                            index = j
                        elif i == 1 and (computers[index][0] == pref[0] or computers[index][0] > computers[j][0]):
                            index = j
                    else:
                        index = j
        pref[i] = computers[index][0]
        if i == 0:
            first = index
            temp1 = sums[index]
        else:
            if num == 2:
                temp2 = sums[first]
            else:
                temp2 = sums[index]

    if temp1 == temp2:
        if pref[0] <= pref[1]:
            print(pref[0] + "\n" + pref[1])
        elif pref[0] > pref[1]:
            print(pref[1] + "\n" + pref[0])
    else:
        print(pref[0] + "\n" + pref[1])
else:
    print(computers[0][0])
