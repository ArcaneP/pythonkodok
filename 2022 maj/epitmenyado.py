# 2022 maj emelt

f = open("utca.txt", "r")
sor = f.readline()
adok = sor.split(" ")
telkek = []
for line in f:
    telkek.append(line.split())

print(adok)
print(telkek)

print("feladat 2. :", len(telkek), "telek található")


f.close()

