import time
for x in range(20):
    vraag = int(input("Kies een optie:\nWilt u totaal bedrag min btw? kies 1.\nWilt u btw bij het bedrag optellen? kies 2.\n"))
    if vraag == 1:
        totalone = float(input("Voer nu uw bedrag in:\n"))
        btwone = float(input("Hoeveel % btw moet er vanaf?\n"))
        if btwone == 21:
            zonder = totalone / 100 * 21
            excl = totalone - zonder
            print(f"\n invoer: {totalone}\n")
            print(f"\nbtw los: ", zonder)
            print(f"excl btw: ", excl)
        elif btwone == 9:
            zonderi = totalone / 100 * 9
            excli = totalone - zonderi
            print(f"\n invoer: {totalone}\n")
            print(f"\nbtw los: ", zonderi)
            print(f"excl btw: ", excli)
        else:
            print("Er is iets fout gegaan.")
    elif vraag == 2:
        totaltwo = float(input("Voer nu uw bedrag in:\n"))
        btwtwo = float(input("Hoeveel % btw moet erbij?\n"))
        if btwtwo == 21:
            totalz = totaltwo * 1.21
            print(f"\n invoer: {totaltwo}\n")
            print(f"Bedrag + btw: {totalz}")
        elif btwtwo == 9:
            totalx = totaltwo * 1.09
            print(f"\n invoer: {totaltwo}\n")
            print(f"\n Bedrag + btw: {totalx}")
        else:
            print("Er is iets fout gegaan.")
    else:
        print("Kies 1 of 2.")
    time.sleep(2)



