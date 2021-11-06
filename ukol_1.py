from turtle import forward, speed, left, right, penup, pendown, goto, circle,exitonclick   #Import vybraných funkcí ze želvy

print("Zadejte velikost délky jedné strany šestiúhleníku") #Volitelná velikost délky strany šestiúhelníku
a = float(input())
while a <= 0: #Kontrola zadávané délky strany
    print("Nezadávejte nekladnou velikost délky. Zadejte ji prosím znovu.")
    a = float(input())

print("Zadejte počet sloupců hracího pole.")  #Volitelná velikost hrací plochy
x = int(input())
print("Zadejte počet řádků hracího pole.")
y = int(input())
while x <= 0 or y <= 0: #Kontrola zadávaných rozměrů sítě
    print("Nezadávejte nekladné velikosti hracího pole. Zadejte je prosím znovu.")
    print("Zadejte počet sloupců hracího pole.")  
    x = int(input())
    print("Zadejte počet řádků hracího pole.")
    y = int(input())
for _ in range (x):   #Vykreslení šestiúhelníkové hrací plochy
    for _ in range(y):  
        for _ in range(6): #Vykreslení jednoho šestiúhelníku
            speed(10)
            forward(a) 
            left(60)
        left(120)
        forward(a)
        right(60)
        forward(a) 
        right(60) 
    forward(a)
    for _ in range(y): #Návrat želvy z vrchního šestiúhelníku na bod, odkud se bude vykreslovat další sloupec.
        right(60)
        forward(a)
        right(60)
        forward(a)
        left(120)
    left(60)
    forward(a)
    right(60)    
penup() #Želva při pohybu nebude psát
goto(0,0) #Přesun želvy na počáteční souřadnice


print("Souřadnice zadávejte následujícím způsobem:")
print("číslo sloupce -> enter -> číslo řádku -> enter")
pocpol = y*x

hrac1 = True
for _ in range (pocpol) : #Cyklus se bude opakovat, dokud nebudou všechna pole plná
    if hrac1 == True: #Střídání hráčů
        hraccis = 1
    else:
        hraccis = 2   
    print("Hráči",hraccis,"zadej souřadnice políčka.")
    sx = int(input())
    sy = int(input())
    while sx > x or sy > y or sx <= 0 or sy <= 0: #Kontrola správnosti zadaných souřadnic
        print("Tato souřadnice je mimo pole hry. Zadejte prosím souřadnice znovu.")
        sx = int(input())
        sy = int(input())
        
    for _ in range (sx-1): #Posun nekreslící želvy na správný sloupec
        forward(a)
        left(60)
        forward(a)
        right(60)
    for _ in range (sy-1): #Posun nekreslící želvy na správný řádek
        left(120)
        forward(a)
        right(60)
        forward(a)
        right(60)
    left(60) #Posun nekreslící želvy do středu šestiúhleníku
    forward(a)
    right(15)
    if hrac1 == True:
        pendown()
        for _ in range (4): #Vykreslení křížku
            forward(a/2)
            left(180)
            forward(a/2)
            left(90)
        right(45)
        
    else: #Vykreslení kolečka
        right(135)
        forward(a/2)
        left(90)
        pendown()
        circle(a/2)
        
    penup()
    goto(0,0)    
    hrac1 = not hrac1 #Výměna hráčů
print("Konec hry!")  
exitonclick() #Nechá otevřené okno s želvou