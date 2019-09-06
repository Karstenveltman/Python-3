def helloworldultra(n):
    for i in range(n):
        print("Hello World")

#helloworldultra(10)

def tafel5():
    for i in range(12):
        tafel = i+1
        
        print(5*tafel)


#tafel5()


def aantalwoord(naam, nummer):
    for i in range(nummer):
        print(naam)


#aantalwoord("Hello World", 2)


def kerstboom(string):
    for i in range(len(string)):
        a = i + 1
        woord = string[i] * a
        print(woord)





#kerstboom("qwerty")


def r5():
    return 5

#print(r5())

def r5maali(i):
    return 5*i

#print(r5maali(3))

def max_van_3(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > b and  c > a:
        print(c)

#max_van_3(3, 4, 5)



def reverse_string(string):
    a = ""
    b = ""
    for i in string:
        a = i
        a += b
        b = a
    return b

#print(reverse_string("woord"))

def priemgetal(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
            else:
                return True
    else:
        return False
#print(priemgetal(300))


def palindrome(string):
    a = ""
    b = ""
    for i in string:
        a = i
        a += b
        b = a
    if b == string:
        return True
    else:
        return False

print(palindrome("lepel"))





    
