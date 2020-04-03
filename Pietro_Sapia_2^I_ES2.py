BigliettoRivToL=3.40
BigliettoRivChieriL=4.20

BigliettoRivToP=3.40/100*90
BigliettoRivToS=3.40/100*85
BigliettoRivToD=3.40/100*75

BigliettoRivChieriP=4.20/100*90
BigliettoRivChieriS=4.20/100*85
BigliettoRivChieriD=4.20/100*75

BigliettoRivTo1=str(input("Dove vuoi andare? "))
if BigliettoRivTo1.lower() == "torino" :
    A=str(input("""Qual è la tua situazione lavorativa?
                [premere P per pensionato]
                [premere S per studente]
                [premere D per disoccupato]
                [premere L per lavoratore]

                Situazione lavorativa : """))
    if A.upper()=="P" :
        print (f"Il costo del biglietto è {BigliettoRivToP}")
    elif A.upper()=="S" :
        print (f"Il costo del biglietto è {BigliettoRivToS}")
    elif A.upper()=="D" :
        print (f"Il costo del biglietto è {BigliettoRivToD}")
    else :
        print (f"Il costo del biglietto è {BigliettoRivToL}")

elif BigliettoRivTo1.lower() == "chieri" :
    A=str(input("""Qual è la tua situazione lavorativa?
                [premere P per pensionato]
                [premere S per studente]
                [premere D per disoccupato]
                [premere L per lavoratore]

                Situazione lavorativa : """))
    if A.upper()=="P" :
        print (f"Il costo del biglietto è {BigliettoRivChieriP}")
    elif A.upper()=="S" :
        print (f"Il costo del biglietto è {BigliettoRivChieriS}")
    elif A.upper()=="D" :
        print (f"Il costo del biglietto è {BigliettoRivChieriD}")
    else :
        print (f"Il costo del biglietto è {BigliettoRivChieriL}")
else :
    print("La tratta selezionata non è disponibile")

input("Premi invio per uscire ;)")
