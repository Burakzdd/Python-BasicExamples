import random
print("Hoşgeldiniz \n")
print("SOL İÇİN L , SAĞ İÇİN R; AŞAĞI İÇİN B; YUKARI İÇİN T BASINIZ")

grid = [['2','.','.','.'],
        ['.','4','.','.'],
        ['.','.','.','4'],
        ['.','.','2','.']
        ]
direction = {'L':0, 'B':1, 'R':2, 'T':3, 'X':4}
#print(grid)

for i in range(len(grid)):
    res = "\t\t"
    for j in range(len(grid[i])):
        for _ in range(4): res += " "
        res += grid[i][j]
    print(res)
    print('\n')

totalscore=0
losestatus=0

while 1:
    tmp = input("SOL İÇİN L , SAĞ İÇİN R; AŞAĞI İÇİN B; YUKARI İÇİN T BASINIZ")
    if tmp in ('r','R','l','L','t','T','b','B','X','x'):
        dir = direction[tmp.upper()]
        if dir == 4:
            print("Final Score:"+str(totalscore))
        else:

            for i in range(dir): grid = list(map(list,zip(*grid[::-1])))
        for i in range(len(grid)):
            temp = []
            for j in grid[i]:
                if j != '.':
                    temp.append(j)
            temp += ['.'] * grid[i].count('.')
            for j in  range(len(temp) - 1):
                if temp[j] == temp[j+1] and temp[j] !='.' and temp[j+1] !='.':
                    temp[j] = str(2*int(temp[j]))
                    totalscore += int(temp[j])
                    temp[j+1] = '.'
            grid[i] = []
            for j in temp:
                if j != '.':
                    grid[i].append(j)
            grid[i] += '.' * temp.count('.')
        for i in range(4-dir): grid = list(map(list,zip(*grid[::-1])))

        num = random.randint(1,2) *2
        x = random.randint(0,3)
        y = random.randint(0,3)
        losestatus = 0
        isFound = False
        if grid[x][y] != '.':
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if(grid[i][j]) == '.':
                        x= i
                        y = j
                        losestatus = 0
                        isFound = True
            if not isFound:
                x = -1
                y = -1
                losestatus = 1
        if not losestatus:
            grid[x][y] = str(num)

        for i in range(len(grid)):
            res = "\t\t"
            for j in range(len(grid[i])):
                for _ in range(4): res += " "
                res += grid[i][j]
            print(res)
            print('\n')
        if losestatus:
            print("Game Over")
            print("Final Score:"+ str(totalscore))
            break
        print("Final Score:"+ str(totalscore))
    else:
        print("Yanlış bir tuş girdiniz")
