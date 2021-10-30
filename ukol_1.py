from turtle import * #Import všech funkcí ze želvy

print("Zadejte počet sloupců hracího pole.")  #Volitelná velikost hrací plochy
x = int(input())
print("Zadejte počet řádků hracího pole.")
y = int(input())
for _ in range (x):   #Vykreslení šestiúhelníkové hrací plochy
    for _ in range(y):  
        for _ in range(6): #Vykreslení jednoho šestiúhelníku
            speed(10)
            forward(30) 
            left(60)
        left(120)
        forward(30)
        right(60)
        forward(30) 
        right(60) 
    forward(30)
    for _ in range(y): #Návrat želvy z vrchního šestiúhelníku na bod, odkud se bude vykreslovat další sloupec.
        right(60)
        forward(30)
        right(60)
        forward(30)
        left(120)
    left(60)
    forward(30)
    right(60)    
penup() #Želva při pohybu nebude psát
goto(0,0) #Přesun želvy na počáteční souřadnice


print("Souřadnice zadávejte následujícím způsobem:")
print("číslo sloupce -> enter -> číslo řádku -> enter")
pocpol = y*x

hrac1 = True
while pocpol > 0 : #Cyklus se bude opakovat, dokud nebudou všechna pole plná
    if hrac1 == True: #Střídání hráčů
        hraccis = 1
    else:
        hraccis = 2   
    print("Hráči",hraccis,"zadej souřadnice políčka.")
    sx = int(input())
    sy = int(input())
    while sx > x or sy > y: #Kontrola správnosti zadaných souřadnic
        print("Tato souřadnice je mimo pole hry. Zadejte souřadnice znovu.")
        sx = int(input())
        sy = int(input())
    
    for _ in range (sx-1): #Posun nekreslící želvy na správný sloupec
        forward(30)
        left(60)
        forward(30)
        right(60)
    for _ in range (sy-1): #Posun nekreslící želvy na správný řádek
        left(120)
        forward(30)
        right(60)
        forward(30)
        right(60)
    left(60) #Posun nekreslící želvy do středu šestiúhleníku
    forward(30)
    right(15)
    if hrac1 == True:
        pendown()
        for _ in range (4): #Vykreslení křížku
            forward(15)
            left(180)
            forward(15)
            left(90)
        right(45)
        
    else: #Vykreslení kolečka
        right(135)
        forward(15)
        left(90)
        pendown()
        circle(15)
        
    penup()
    goto(0,0)    
    pocpol -= 1 #Odečtení jednoho volného pole, na které byla právě nakreslena značka
    hrac1 = not hrac1 #Výměna hráčů
print("Konec hry!")   











exitonclick() #Nechá otevřené okno s želvou