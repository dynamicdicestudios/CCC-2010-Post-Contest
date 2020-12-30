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
            if sums[j] > sums[j + 1] and index != j and sums[j] <= temp1:
                index = j
            elif sums[j + 1] > sums[j] and index != j + 1 and sums[j+1] <= temp1:
                index = j + 1
            elif sums[j] == sums[j + 1] and index != j and sums[j] <= temp1:
                index = j
            elif num == 2:
                if index == 0:
                    index = 1
                else:
                    index = 0
        else:
            if sums[j] > sums[index] and index != j and sums[j] <= temp1 and j != first:
                index = j
    pref.append(computers[index][0])
    first = index
    if i == 0:
        temp1 = sums[index]
    else:
        temp2 = sums[index]

if temp1 == temp2:
    if len(pref[0]) < len(pref[1]):
        print(pref[1] + "\n" + pref[0])
    elif len(pref[0]) >= len(pref[1]):
        print(pref[0] + "\n" + pref[1])
else:
    print(pref[0] + "\n" + pref[1])
        
