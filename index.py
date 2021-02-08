
#1
def a():
    return 5
print(a())

# returns 5 and prints 5

#2
def a():
    return 5
print(a()+a())

# returns 5 per function call and adds them togeather in the console.log printing 10

#3
def a():
    return 5
    return 10
print(a())

#returns 5 and prints 5 the second return won't be ran since return exits the function

#4
def a():
    return 5
    print(10)
print(a())

#returns 5 then prints 5 the print(10) wont be touched since return exits the function

#5
def a():
    print(5)
x = a()
print(x)

# prints 5 then prints nothing since the function didn't return anything, it just prints

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#prints 3 and 5 then will throw an error since nothing is returned there is nothing for print(a(1,2) + a(2,3)) to add together

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# will print 25 since the return turns 2 and 5 into strings and returns the concatinated string

#8
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# prints 100 then returns 10 and prints 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#returns 7 prints 7
#returns 14 prints 14
#returns 7 and returns 14 adds them together in the console.log and prints 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#returns 8 and prints 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#prints 500 prints 500 prints 300 prints 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# prints 500 prints 500 prints 300 returns 300 prints 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#prints 500 prints 500 prints 300 returning 300 asigning 300 to b then prints 300 again

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#prints 1 prins 3 prints 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#prints 1 print 3 return 5 print 5 return 10 print 10