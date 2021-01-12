with open('input.txt', 'r') as f:
    a=f.readline()
    x=int(a)
    y=x-2
    z=x-1
    s=x+1
    v=x+2

with open('output.txt', 'w') as f:
    f.write(str(y))
    f.write('   ')
    f.write(str(z))
    f.write('   ')
    f.write(str(x))
    f.write('   ')
    f.write(str(s))
    f.write('   ')
    f.write(str(v))
    
