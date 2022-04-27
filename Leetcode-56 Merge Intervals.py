intervals = [[1,4],[4,5]]
# Output: [[1,6],[8,10],[15,18]]
print(sorted(intervals))
temp=[]
temp.append(intervals[0])
print(temp)
for i in range(1,len(intervals)):
    startpoint2= intervals[i][0]
    endpoint2= intervals[i][1]
    current=temp.pop()
    startpoint1=current[0]
    endpoint1=current[1]
    endMaX=max(endpoint1,endpoint2)
    if endpoint1>=startpoint2:
        #Merging will be occured
        merge=[]
        merge.append(startpoint1)
        merge.append(endMaX)
        temp.append(merge)
    else:
        #No Merging
        temp.append(current)
        temp.append(intervals[i])
print(temp)
    
