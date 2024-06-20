import os
#Writing into the file
with open('file.txt','w') as f:
    f.write('''Hello BITM Hi
Have a great day
Enjoy with your training days
Be focused and achieve your goal''')
    f.close()
#Reading and writing file to the console
with open('file.txt','r') as f:
    a=f.read()
    print(a)
    f.close()
#Replacing the word and rewriting the file
a=a.replace('Hello','BITM')
with open('file.txt','w') as f:
    f.write(a)
    f.close()
with open('file.txt','r') as f:
    a=f.read()
    print(a)
    f.close()
#Extracting the text from file
with open('file.txt','rb') as f:
    print(f.tell())
    f.seek(-35,2)
    print(f.read().decode('utf-8'))
    f.close()  
#Removing the file
os.remove('file.txt')