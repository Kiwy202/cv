def hola():
    for i  in range (1, a+1):
        for j in range (1, i+1):
            print(i, end="")
        print()
    for i in range(a-1,0,-1):
        for j in range(1,i+1):
            print(i,end="")
        print("")

a= int(input())
b= int(input())
print("")

for ejecucion in range(b):
    hola()
    print("")