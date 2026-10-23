# Jeg har kommentarer nederst i koden for å forklare litt bedre :)

import time # importerer time for å slippe å spamme terminalen din med valg og ord, så det blir mere i "lesende" tempo..

# Variabler:
start = ""
konflikt_1 = ""
konflikt_2 = ""
problem_3 = ""

# Start:
while True: # en while loop som går å går til den blir breaket
    start = input("Hei, Erling. Du har en del valg å ta, er du klar? ja/nei: ")
    if(start[0].islower()): # gjør svaret ja/nei til Ja/Nei om det er liten forbokstav
        start = start.capitalize()
    if start == "Ja":
        time.sleep(1) # gir 1 sek delay på printen så det ikke blir "spam" og mere ryddig.
        print("\nFlott! Da begynner vi.\n") # i koden min vil du se mye av \ og \n. \ er bare for å få koden mere ryddig mens jeg skriver så det ikke blir så lange setninger vannrett. og \n er for å få det mere ryddig i terminalen og alt ikke blir "stacka" oppå hverandre.
        time.sleep(4)
        print("Du har disse tre konfliktene, Erling:\n\
1. Silje & Elias sin uenighet om teknologi og UX-design.\n\
2. Hamdi og Hallgeir sin uenighet om  innbyggerinvolvering. \n\
3. Fallende motivasjon i teamet. \n")
        break # breaker loopen hvis JA = TRUE
    elif start == "Nei":
        time.sleep(1)
        print("\nNeivel Erling. Du har sparken!")
        exit() # blir kasta ut hvis man svarer nei
    else:
        time.sleep(1)
        print("\nError. System failure. System is rebooting. \n")

# Konflikt 1:
while True:
    time.sleep(9)
    print("Hvordan vil du løse konflikt 1. mellom Silje & Elias? ")
    konflikt_1 = input("A) Vil du snakke med Silje & Elias hver for seg? \n\
B) Eller vil du ta det opp i plenum? \n\
Skriv A for å snakke med de hver for seg, eller B for å ta det opp i plenum: (A/B) ")
    if(konflikt_1[0].islower()):
        konflikt_1 = konflikt_1.capitalize()
    if konflikt_1 == "A":
        time.sleep(2)
        print("\nDu snakker med de hver for seg, temperaturen blir lavere, men teknologivalg er enda uavklart! ")
        break
    elif konflikt_1 == "B":
        time.sleep(2)
        print("\nDu tar det opp i plenum, Elias sin løsning blir valgt, men det blir enda dårligere stemning i teamet! ")
        break
    else:
        time.sleep(1)
        print("\nError. System failure. System is rebooting. \n")

# Konflikt 2:
while True:
    time.sleep(6)
    print("\nHvordan vil du løse konflikt 2. mellom Hamdi & Hallgeir? ")
    konflikt_2 = input("A) Vil du initiativ til et felles møte med teamet? \n\
B) Vil du avvente å se? \n\
C) Eller vil du ta et felles møte med Hamdi, Hallgeir og HR-avdelingen? \n\
Skriv A for å invitere til et felles møte, eller B for å avvente å se, \
eller C for å invitere gutta og HR til et møte: (A/B/C) ")
    if(konflikt_2[0].islower()):
        konflikt_2 = konflikt_2.capitalize()
    if konflikt_2 == "A":
        time.sleep(2)
        print("\nDu inviterer de til et felles møte, Hamdi og Hallgeir inser at de bare har misforstått hverandre. \
Nå jobber de godt, men de har det travelt! ")
        break
    elif konflikt_2 == "B":
        time.sleep(2)
        print("\nDu avventer å ser, konflikten blir personlig og progresjonen stopper opp! ")
        break
    elif konflikt_2 == "C":
        time.sleep(2)
        print("\nDu tar et felles møte med gutta og HR, konflikten løser seg uten noe bortkastet tid! ")
        break
    else:
        time.sleep(1)
        print("\nError. System failure. System is rebooting. \n")

# Problem 3:
while True:
    time.sleep(6)
    print("\nHvordan vil du løse problem 3. -> mangel på motivasjon i teamet? ")
    problem_3 = input("A) Vil du sette av tid til sosiale aktiviteter med teamet? \n\
B) Eller vil du prioritere leveranse og resultater? \n\
Skriv A for å invitere teamet til sosiale aktiviteter, eller B for prioritere resultater: (A/B) ")
    if(problem_3[0].islower()):
        problem_3 = problem_3.capitalize()
    if problem_3 == "A":
        time.sleep(2)
        print("\nDu inviterer til sosiale aktiviteter, alle koser seg med laser-tag men du stresser over lite tid! ")
        break
    elif problem_3 == "B":
        time.sleep(2)
        print("\nDu prioriterer resultater, alle team-medlemene sliter seg helt ut, \
men de får gjort mye selv om det er dårlig stemning! ")
        break
    else:
        time.sleep(1)
        print("\nError. System failure. System is rebooting. \n")

# Utfall 1:
if (konflikt_1 == "A" and konflikt_2 == "A" and problem_3 == "A") or \
   (konflikt_1 == "A" and konflikt_2 == "A" and problem_3 == "B") or \
   (konflikt_1 == "A" and konflikt_2 == "C" and problem_3 == "A"):
   time.sleep(6)
   print("\nGratulerer! Du har håndtert konfliktene på en god måte. \
Teamet har kommet seg gjennom storming-fasen og er nå videre til norming-fasen!")

# Utfall 2:
elif (konflikt_1 == "A" and konflikt_2 == "B" and problem_3 == "B") or \
     (konflikt_1 == "A" and konflikt_2 == "C" and problem_3 == "B") or \
     (konflikt_1 == "B" and konflikt_2 == "A" and problem_3 == "A") or \
     (konflikt_1 == "B" and konflikt_2 == "C" and problem_3 == "B"):
     time.sleep(6)
     print("\nDu har delvis løst konfliktene. Prototypen blir klart i tide, men teamet kan ikke lenger jobbe sammen.")

# Utfall 3:
elif (konflikt_1 == "A" and konflikt_2 == "B" and problem_3 == "A") or \
     (konflikt_1 == "B" and konflikt_2 == "A" and problem_3 == "B") or \
     (konflikt_1 == "B" and konflikt_2 == "B" and problem_3 == "A") or \
     (konflikt_1 == "B" and konflikt_2 == "B" and problem_3 == "B") or \
     (konflikt_1 == "B" and konflikt_2 == "C" and problem_3 == "A"):
     time.sleep(6)
     print("\nDine avgjørelser er fatale. Prosjektet mister samhold og blir dessverre forsinket. \
Prototypen levers ikke i tide.")

# Utfall 4:
else:
    time.sleep(1)
    print("\nError. System failure. System is rebooting. \n")
    exit()

# Mine kommentarer (Robin):
# \ = jeg bruker denne for å formatere ryddigere, spesielt når jeg sitter på en laptop med liten skjerm og har to ting oppe samtidig.
# \n = bruker denne for å få litt "pauserom" i terminalen, så ikke alt blir spamma med tekst men blir lagt ut som avsnitt, også et fint formateringsverktøy!
# import.time og time.sleep(x) = bruker også disse for å få litt ryddigere i terminalen, sånn så det blir mere timet å sendt ut i riktig hastighet
# if(start[0].islower()): = her sjekker jeg om inputet har liten forbokstav, altså ord 0, som er første bokstaven, pclogikk starter alltid å telle fra 0, og hvis den har det så gjør denne -> start = start.capitalize() så den blir stor forbokstav (endrer da permament variabelen i unputet til stor forbokstav)
# bruker en while loop så hvis de kommer til else-statement så vil de bare bli loopa tilbake til første spørsmål, mens hvis de kommer til if eller elif har jeg tatt en break som gjør at de breaker loopen å går videre til neste kodeblock.
# valgte også å bruke dictionary for utfallene istedet for poengsystem
