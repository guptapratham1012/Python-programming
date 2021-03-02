print('------------------------------------------')
print('Print all positive numbers')
print('\nInstructions:')
print('\n')
print('Enter the numbers of the list, use space bar')
print('For example: -1 -2 3')
print('\n\n')
  
l2 = list(map(int,input('Enter the numbers : ').strip().split()))
print('Input: List2- ', l2)
print('Output: ')
for x in l2:
    if x>=0:
        print(x,end=' ')
print('\n------------------------------------------')
