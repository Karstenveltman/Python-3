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
        word = string[i] * a
        print(word)





#kerstboom("qwerty")


def r5():
    return 5

#print(r5())

def r5maali(i):
    return 5*i

#print(r5maali(3))

#def max_van_3()



def reverse_string(string):
    a = ""
    b = ""
    for i in string:
        a = i
        a += b
        b = a
    return b
print(reverse_string("woord"))






    


    




    
