while True:
 n=input("Inserire un numero : ")
 if n.isnumeric():
    n=int(n)
    pass
 else: 
    print ("Invalid input")
    continue
 nf=n%2
 if nf==0 :
    print("Il numero inserito è pari")
 else :
    print("Il numero inserito è dispari")
 IsPrimo = True
 L1=(list(range(2, n)))
 for i in L1:
    if n%i == 0 :
       IsPrimo = False 
       break

 if IsPrimo:
  print("Il numero inserito è primo")
 else:
   print("Il numero inserito non è primo") 
