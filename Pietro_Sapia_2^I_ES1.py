dictionar={"A":"ottimo" , "B":"distinto" , "C":"discreto" , "D":"sufficiente" , "E":"insufficiente"}
nomi=[]
voti=[]
votil=[]
a=10
for i in range (a) :
    nomi.append (input(f"Inserire nome alunno {i+1} : "))
for i in range (a) :
    voti.append (input(f"Inserire voto alunno {i+1} : "))
for i in voti:
    votil.append(dictionar[i])
print("""
""")
print (nomi[0], votil[0])
print (nomi[1], votil[1])
print (nomi[2], votil[2])
print (nomi[3], votil[3])
print (nomi[4], votil[4])
print (nomi[5], votil[5])
print (nomi[6], votil[6])
print (nomi[7], votil[7])
print (nomi[8], votil[8])
print (nomi[9], votil[9])

input("Premi invio per uscire ;)")
