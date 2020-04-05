while True:
 n=input("Enter a number : ")
 if n.isnumeric():
    n=int(n)
    pass
 else: 
    print ("Invalid input")
    continue
 nf=n%2
 if nf==0 :
    print("The number entered is even")
 else :
    print("The number entered is odd")
 IsPrimo = True
 L1=(list(range(2, n)))
 for i in L1:
    if n%i == 0 :
       IsPrimo = False 
       break

 if IsPrimo:
  print("The number entered is a prime number")
 else:
   print("The number entered isn't a prime number")
 input("""
Press enter to restart the program
""")
