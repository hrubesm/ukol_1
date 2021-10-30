# DEADLINE: 6.11. v 23:59
# Vše najdeš na webu
from turtle import *

print("Zadej počet sloupců")
x = int(input())
print("Zadej počet řádků")
y = int(input())
for _ in range (x):   
    for _ in range(y):  
        for _ in range(6):
            forward(30) 
            left(60)
        left(120)
        forward(30)
        right(60)
        forward(30) 
        right(60) 
    forward(30)
    for _ in range(y):
        right(60)
        forward(30)
        right(60)
        forward(30)
        left(120)
    left(60)
    forward(30)
    right(60)    
penup()
goto(0,0)


print("Souřadnice zadávejte následujícím způsobem:")
print("číslo sloupce -> enter -> číslo řádku -> enter")
pocpol = y*x

hrac1 = True
while pocpol > 0 :
    if hrac1 == True:
        hraccis = 1
    else:
        hraccis = 2   
    print("Hráči",hraccis,"zadej souřadnice políčka.")
    sx = int(input())
    sy = int(input())
    while sx > x or sy > y:
        print("Tato souřadnice je mimo pole hry. Zadejte souřadnice znovu.")
        sx = int(input())
        sy = int(input())
    
    for _ in range (sx-1):
        forward(30)
        left(60)
        forward(30)
        right(60)
    for _ in range (sy-1):
        left(120)
        forward(30)
        right(60)
        forward(30)
        right(60)
    left(60)
    forward(30)
    right(15)
    if hrac1 == True:
        pendown()
        for _ in range (4):
            forward(15)
            left(180)
            forward(15)
            left(90)
        right(45)
        
    else:
        right(135)
        forward(15)
        left(90)
        pendown()
        circle(15)
        
    penup()
    goto(0,0)    
    pocpol -= 1
    hrac1 = not hrac1
print("Konec hry!")   











exitonclick()