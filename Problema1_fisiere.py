with open('numere.txt', 'r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=b 
else:
    x=a

with open('minim.txt', 'w') as f:
    f.write(str(x))