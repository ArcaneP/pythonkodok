szam = 0
Oszam = 3
counter = 0

with open("szamok.txt", "w") as out:
    while szam <= 300:
        szam+=1
        if(szam % Oszam == 0):
            if(counter < 100):
                out.write("%d" % szam + "\n")
                print('szam oszhato 3 al: ', szam)
                counter += 1
