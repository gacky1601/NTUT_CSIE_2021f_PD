def check(sex):

    result = ''
    for i in range(10):



        for kpop in range(10):
            nowNum = sex[i][kpop]
            
            if i <= 5:
                column = [sex[i+k][kpop] for k in range(5)]
                above = [sex[k][kpop] for k in range(i)]
                above = above if above != [] else [-1]
                below = [sex[k][kpop] for k in range(-1, i+4, -1)]
                below = below if below != [] else [-1]
                if column.count(nowNum) == 5 and nowNum != 0 and above[-1] != nowNum and below[-1] != nowNum:
                    return '%s win' % column[0]
                elif column.count(1) == 4 and column.count(0) == 1 and above[-1] != 1 and below[-1] != 1:
                    for k in range(5):
                        if column[k] == 0:
                            result = '%s%s' % (i+k, kpop)

            if kpop <= 5:
                row = sex[i][kpop:kpop+5]
                rrightt = sex[i][-1:kpop+4:-1]
                rrightt = rrightt if rrightt != [] else [-1]
                
                lefffft = sex[i][:kpop]
                lefffft = lefffft if lefffft != [] else [-1]
                if row.count(nowNum) == 5 and nowNum != 0 and rrightt[-1] != nowNum and lefffft[-1] != nowNum:
                    return '%s win' % row[0]
                elif row.count(1) == 4 and row.count(0) == 1 and rrightt[-1] != 1 and lefffft[-1] != 1:
                    for k in range(5):
                        if row[k] == 0:
                            result = '%s%s' % (i, kpop+k)

            if i <= 5 and kpop <= 5:
                sexxxxxxxx = [sex[i+k][kpop+k] for k in range(5)]
                rrightt = [sex[i+k+5][kpop+k+5]
                         for k in range(10-(max([i, kpop])+5))]
                rrightt = rrightt if rrightt != [] else [-1]
                lefffft = [sex[i-k-1][kpop-k-1] for k in range(min([i, kpop]))]
                lefffft = lefffft if lefffft != [] else [-1]
                if sexxxxxxxx.count(nowNum) == 5 and nowNum != 0 and rrightt[0] != nowNum and lefffft[0] != nowNum:
                    return '%s win' % row[0]
                elif sexxxxxxxx.count(1) == 4 and sexxxxxxxx.count(0) == 1 and rrightt[0] != 1 and lefffft[0] != 1:
                    for k in range(5):
                        if sexxxxxxxx[k] == 0:
                            result = '%s%s' % (i+k, kpop+k)

            if i <= 5 and kpop >= 4:
                slashL = [sex[i+k][kpop-k] for k in range(5)]
                rrightt = [sex[i-k-1][kpop+k+1] for k in range(min([i, (9-kpop)]))]
                rrightt = rrightt if rrightt != [] else [-1]
                lefffft = [sex[i+k+5][kpop-k-5] for k in range(10-(max([i, kpop])+5))]
                lefffft = lefffft if lefffft != [] else [-1]
                if slashL.count(nowNum) == 5 and nowNum != 0 and rrightt[0] != nowNum and lefffft[0] != nowNum:

                    return '%s win' % slashL[0]
                elif slashL.count(1) == 4 and slashL.count(0) == 1 and rrightt[0] != 1 and lefffft[0] != 1:
                    for k in range(5):
                        if slashL[k] == 0:
                            result = '%s%s' % (i+k, kpop-k)

    return result


sex = []
for i in range(10):
    temmmmmmmp = []

    for kpop in input():
        temmmmmmmp.append(int(kpop))
    sex.append(temmmmmmmp)


print(check(sex))