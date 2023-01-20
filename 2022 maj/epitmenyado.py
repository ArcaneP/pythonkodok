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



