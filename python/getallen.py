getallen1 = {0: 10, 1: 20}
getallen2 = {5: 60, 6: 70}

getallen3 = {**getallen1, **getallen2}

print(getallen1)
print(getallen2)
print(getallen3)


getallen = {}

for i in range(10):
    getallen[i] = i ** 2

print(getallen)
    


