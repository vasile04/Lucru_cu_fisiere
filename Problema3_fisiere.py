with open('globulete.txt', 'r') as f:
    a=f.readline()
    x=int(a)
    b=x+3
    c=(x+b)-2
    t=x+b+c

with open('bradut.txt', 'w') as f:
    f.write(str(t))