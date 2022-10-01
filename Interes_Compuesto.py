# Interés Compuesto : 

print("---------------------------")
print("--- INTERÉS - COMPUESTO ---")
print("---------------------------")

#Input
C = int(input("Digite el valor de la capital C: "))

#Processing
N = 2*C
sum = C
while C < N:
    C= C*0.05 +C
    sum = sum + 1

#Output
print("Su dinero se duplicara en " , sum ,"Meses" )
    

    