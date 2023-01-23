#2022 maj emelt

f = open("utca.txt", "r")
sor = f.readline()
adok = sor.split(" ")
telkek = []
for line in f:
    telkek.append(line.split())
print(adok)
print(telkek)

print("2. feladat:", len(telkek), "telek található")
f.close()

print("3. feladat. Egy tulajdonos adószáma: ")
adoszam = input()
telek_szam = 0
for telek in telkek:
    if adoszam == telek[0]:
        print(telek[1],"utca",telek[2])
        telek_szam += 1

if telek_szam == 0:
    print("Nem szerepel az adatállományban!")

print("4. feladat.  ")
#shift + f10 = run py


def ado(sav,terulet):
    global adok
    if sav == "A":
        ertek = terulet*int(adok[0])
    if sav == "B":
        ertek = terulet*int(adok[1])
    if sav == "C":
        ertek = terulet*int(adok[2])

    if ertek < 10000:
        return 0
    else:
        return ertek


print("5. feladat.  ")

dbA = dbB = dbC = 0
adoA = adoB = adoC = 0

for telek in telkek:
    sav = telek[3]
    telek_ter = int(telek[4])

    adoErtek = ado(sav, telek_ter)

    if(sav == "A"):
        dbA += 1
        adoA += adoErtek

    if (sav == "B"):
        dbB += 1
        adoB += adoErtek

    if (sav == "C"):
        dbC += 1
        adoC += adoErtek

print("A sávba", dbA  ,"telek esik, az adó", adoA,"Ft.")
print("A sávba", dbB, "telek esik, az adó", adoB, "Ft.")
print("A sávba", dbC, "telek esik, az adó", adoC, "Ft.")

 #Dictionary adok = {"A": 800, "B": 600, "C": 100}

print("6. feladat.  ")
utcak = []
utca = telkek[0][1]
sav = telkek[0][3]

for i in range(1,len(telkek)):
    utcaUj = telkek[i][1]
    savUj = telkek[i][3]

    if (utca == utcaUj) and (sav != savUj):
       if not (utca in utcak):
           utcak.append(utca)

    elif(utca != utcaUj):
        utca = utcaUj
        sav = savUj

for utca in utcak:
    print(utca)

