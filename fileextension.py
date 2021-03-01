fn= input("Input the Filename: ")
f = fn.split(".")
a='py'
b='java'
c='txt'

if f[-1]==a:
    print('The extension of the file is : \'Python\'')
if f[-1]==b:
    print('The extension of the file is : \'Java\'')
if f[-1]==c:
    print('The extension of the file is : \'Text\'')
