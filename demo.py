def sortArray(l):
  t=[]
  for i in range(len(l)-1,0,-1):
    swapped=False
    for j in range(i):
      if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
        swapped=True

    if not swapped:
      break
  return l

print(sortArray([10,2,23,4,1,31,31,31,141]))

      
