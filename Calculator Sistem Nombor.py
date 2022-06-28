
def PerpuluhanToPerduaan():

        x = int(input("Sila masukkan nombor perpuluhan yang ingin ditukarkan kepada nombor perduaan: "))
        y = 0
        jawapanAkhir = ""

        for i in range(0, 16):
            y = x % 2
            x = x // 2
            print(str(x) + " baki " + str(y))
            jawapanAkhir += str(y)

        print("Nombor perduaan ialah " +jawapanAkhir[::-1])

def PerpuluhanToPerlapanan():

    x = int(input("Sila masukkan nombor perpuluhan yang ingin ditukarkan kepada nombor perlapanan : "))
    y = 0
    jawapanAkhir = ""

    for i in range(0, 6):
        y = x % 8
        x = x // 8
        print(str(x) + " baki " + str(y))
        jawapanAkhir += str(y)

    print("Nombor perlapanan ialah "+jawapanAkhir[::-1])

def PerpuluhanToPerenambelasan():

    x = int(input("Sila masukkan nombor perpuluhan yang ingin ditukarkan kepada nombor perenambelasan : "))
    y = 0
    jawapanAkhir = ""

    for i in range(0, 6):
        y = x % 16
        x = x // 16
        if(y==10):
            y="A"
        elif(y==11):
            y="B"
        elif(y==12):
            y="C"
        elif(y==13):
            y="D"
        elif(y==14):
            y="E"
        elif(y==15):
            y="F"
        print(str(x) + " baki " + str(y))
        jawapanAkhir += str(y)

    print("Nombor perenambelasan ialah "+ jawapanAkhir[::-1])

def PerduaanToPerpuluhan():
    x = input("Sila masukkan nombor perduaan yang ingin ditukarkan kepada nombor perpuluhan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        TotalSum += int(individualNum) * 2 ** i

    print("Nombor perpuluhan ialah "+ str(TotalSum))

def PerlapananToPerpuluhan():
    x = input("Sila masukkan nombor perlapanan yang ingin ditukarkan kepada nombor perpuluhan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        TotalSum += int(individualNum) * 8 ** i

    print("Nombor perpuluhan ialah "+str(TotalSum))

def PerlapananToPerduaan():
    x = input("Sila masukkan nombor perlapanan yang ingin ditukarkan kepada nombor perduaan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        TotalSum += int(individualNum) * 8 ** i

    print("Nombor perpuluhan ialah " + str(TotalSum))

    y = 0
    jawapanAkhir = ""

    for i in range(0, 10):
        y = TotalSum % 2
        TotalSum = TotalSum // 2
        print(str(TotalSum) + " baki " + str(y))
        jawapanAkhir += str(y)

    print("Nombor perduaan ialah "+ jawapanAkhir[::-1])

def PerduaanToPerlapanan():
    x = input("Sila masukkan nombor perduaan yang ingin ditukarkan kepada nombor perlapanan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        TotalSum += int(individualNum) * 2 ** i
    print("Nombor perpuluhan ialah " + str(TotalSum))

    y = 0
    jawapanAkhir = ""

    for i in range(0, 6):
        y = TotalSum % 8
        TotalSum = TotalSum// 8
        print(str(TotalSum) + " baki " + str(y))
        jawapanAkhir += str(y)

    print("Nombor perlapanan ialah " +jawapanAkhir[::-1])

def PerenambelasanToPerpuluhan():
    x = input("Sila masukkan nombor perenambelasan yang ingin ditukarkan kepada nombor perpuluhan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        if (individualNum == "A"):
            individualNum = 10
        elif (individualNum == "B"):
            individualNum = 11
        elif (individualNum == "C"):
            individualNum = 12
        elif (individualNum == "D"):
            individualNum = 13
        elif (individualNum == "E"):
            individualNum = 14
        elif (individualNum == "F"):
            individualNum = 15
        TotalSum += int(individualNum) * 16 ** i

    print("Nombor perpuluhan ialah " +str(TotalSum))

def PerenambelasanToPerduaan():
    x = input("Sila masukkan nombor perenambelasan yang ingin ditukarkan kepada nombor perduaan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        if (individualNum == "A"):
            individualNum = 10
        elif (individualNum == "B"):
            individualNum = 11
        elif (individualNum == "C"):
            individualNum = 12
        elif (individualNum == "D"):
            individualNum = 13
        elif (individualNum == "E"):
            individualNum = 14
        elif (individualNum == "F"):
            individualNum = 15
        TotalSum += int(individualNum) * 16 ** i

    print("Nombor perpuluhan ialah " + str(TotalSum))

    y = 0
    jawapanAkhir = ""

    for i in range(0, 16):
        y = TotalSum % 2
        TotalSum = TotalSum // 2
        print(str(TotalSum) + " baki " + str(y))
        jawapanAkhir += str(y)

    print("Nombor perduaan ialah " + jawapanAkhir[::-1])

def PerduaanToPerenambelasan():
    x = input("Sila masukkan nombor perduaan yang ingin ditukarkan kepada nombor perenambelasan : ")
    reverseOrder = x[::-1]
    count = len(str(x))
    TotalSum = 0

    for i in range(0, count):
        individualNum = reverseOrder[i]
        TotalSum += int(individualNum) * 2 ** i
    print("Nombor perpuluhan ialah " + str(TotalSum))

    y = 0
    jawapanAkhir = ""

    for i in range(0, 6):
        y = TotalSum % 16
        TotalSum = TotalSum // 16
        if(y==10):
            y="A"
        elif(y==11):
            y="B"
        elif(y==12):
            y="C"
        elif(y==13):
            y="D"
        elif(y==14):
            y="E"
        elif(y==15):
            y="F"
        jawapanAkhir += str(y)

    print("Nombor perenambelasan ialah " + jawapanAkhir[::-1])


Teruskan=" "
while(Teruskan!="t"):

    print("\n\n#######################  Calculator Sistem Nombor V1.00  #######################")
    print("\n1. Sistem Nombor Perpuluhan kepada Sistem Nombor Perduaan")
    print("2. Sistem Nombor Perpuluhan kepada Sistem Nombor Perlapanan")
    print("3. Sistem nombor Perpuluhan kepada Sistem Nombor Perenambelasan")
    print("4. Sistem Nombor Perduaan kepada Sistem Nombor Perpuluhan")
    print("5. Sistem Nombor Perlapanan kepada Sistem Nombor Perpuluhan")
    print("6. Sistem Nombor Perlapanan kepada Sistem Nombor Perduaan")
    print("7. Sistem Nombor Perduaan kepada Sistem Nombor Perlapanan")
    print("8. Sistem Nombor Perenambelasan kepada Sistem Nombor Perpuluhan")
    print("9. Sistem Nombor Perenambelasan kepada Sistem Nombor Perduaan")
    print("10. Sistem Nombor Perduaan kepada Sistem Nombor Perenambelasan")
    print("\n###########################################################################")
    pilihan = int(input("\nSila masukkan pilihan anda: "))

    if(pilihan==1):
        PerpuluhanToPerduaan()
    elif(pilihan==2):
        PerpuluhanToPerlapanan()
    elif(pilihan==3):
        PerpuluhanToPerenambelasan()
    elif(pilihan==4):
        PerduaanToPerpuluhan()
    elif(pilihan==5):
        PerlapananToPerpuluhan()
    elif(pilihan==6):
        PerlapananToPerduaan()
    elif(pilihan==7):
        PerduaanToPerlapanan()
    elif(pilihan==8):
        PerenambelasanToPerpuluhan()
    elif(pilihan==9):
        PerenambelasanToPerduaan()
    elif(pilihan==10):
        PerduaanToPerenambelasan()
    else:
        print("Pilihan anda tidak valid.")

    Teruskan=input("\n\nAdakah anda ingin meneruskan aplikasi ini?(y/t) ")

print("\n\nTerima kasih kerana menggunakan aplikasi ini.")


