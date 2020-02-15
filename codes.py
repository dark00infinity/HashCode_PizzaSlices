def sum_list(array,max_sum):
    curindlist=[]
    curvallist=[]
    sum=0
    maxscore=0
    startindex=len(array)
    while (len(curvallist)>0 and curindlist[0]!=0) or len(curindlist)==0:
        startindex=startindex - 1
        for i in range(startindex,-1,-1):
            currentvalue=array[i]
            tempsum=sum+currentvalue
            if tempsum==max_sum:
                sum=tempsum
                curindlist.append(i)
                curvallist.append(currentvalue)
                break
            elif tempsum>max_sum:
                continue
            elif tempsum<max_sum:
                sum=tempsum
                curindlist.append(i)
                curvallist.append(currentvalue)
                continue
        if maxscore < sum:
            maxscore=sum
            solutionindex=[]
            solutionvalue=[]
            for y in curindlist:
                solutionindex.append(y)
            for y in curvallist:
                solutionvalue.append(y)
        if maxscore==max_sum:
            break
        if len(curvallist)!=0:
            last=curvallist.pop()
            sum=sum-last
        if len(curindlist)!=0:
            lastindex=curindlist.pop()
            startindex=lastindex
        if len(curindlist)==0 and startindex==0:
            break
    solutionindex.reverse()
    print(solutionindex)
sum_list([1,2,3,4,5],7)
