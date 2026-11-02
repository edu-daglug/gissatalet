namn = input("Vad heter du? ")
print(f"Hej {namn} och välkomen till spelet!")


import random as rand

res = rand.randint(1, 10)
tal = 0
    
while res != tal:
    tal = int(input("Ange ett tal mellen 1 och 10 ->"))
    
    if tal != res:
        print("Fel svar")
             
print("Det var rätt svarat")
   

