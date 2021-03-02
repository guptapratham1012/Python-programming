def most_frequent(x):
   d=dict()
   for key in x:
      if key not in d:
         d[key]=1
      else:
         d[key]+=1
   return d

x=str(input('Input : Please enter a string: '))
print('\n----------------------------------------------\n')
print('Output : ',most_frequent(x))
print('\n----------------------------------------------\n')
