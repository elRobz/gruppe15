# Erling og teamkonflikten - interaktiv historie (IS-118, del 2)
# Programmet følger storylinen og beslutningstreet fra del 1:
#   Beslutning 1: Silje og Elias
#   Beslutning 2: Hamdi og Hallgeir
#   Beslutning 3: Motivasjonen i teamet
# Valgene lagres i variabler. Valg som bygger tillit gir 1 poeng og summen av poengene bestemmer utfallet.

# Poengsum: 3 poeng = utfall 1, 2 poeng = utfall 2, 0-1 poeng = utfall 3
poeng = 0

# Rammefortelling
print("= Erling og Teamet =")
print()
print("Du er Erling, prosjektleder for teamet som lager kommunens medborgerportal.")
print("Etter 6-8 uker er den gode stemningen fra starten borte.")
print("Teamet er i storming-fasen, og prototypen skal være klar om tre uker.")

# Beslutning 1: Silje og Elias
print()
print("- BESLUTNING 1: Silje og Elias -")
print("Silje (UX-design) og Elias (IT) er uenige om teknologi og design.")
print("Diskusjonen er blitt personlig, og begge har støtte fra andre i teamet.")
print()
print("A) Enesamtaler: du snakker med Silje og Elias hver for seg.")
print("B) Plenum: du tar konflikten opp med hele teamet.")

# .upper() gjør at både a og A godtas
# While-løkken spør på nytt til svaret er A eller B
svar = input("Ditt valg (A/B): ").upper()
while svar != "A" and svar != "B":
    print("Ugyldig valg. Skriv A eller B.")
    svar = input("Ditt valg (A/B): ").upper()

if svar == "A":
    valg1 = "enesamtaler"
    poeng = poeng + 1
    print()
    print("Begge får si sin mening uten publikum, og temperaturen synker.")
    print("Men teknologivalget er fortsatt uavklart, og teamet begynner å få dårlig tid.")
else:
    valg1 = "plenum"
    print()
    print("Teamet stemmer frem Elias sin løsning, og den passer bra.")
    print("Men flere tar parti i konflikten, og stemningen i hele teamet blir dårlig.")

# Beslutning 2: Hamdi og Hallgeir
print()
print("- BESLUTNING 2: Hamdi og Hallgeir -")
print("Hamdi (kulturavdelingen) og Hallgeir (brukerrepresentant) er uenige om")
print("hvordan innbyggerne skal involveres. Uenigheten er ennå saklig,")
print("men den kan vokse hvis ingen gjør noe.")
print()
print("A) Felles møte: du tar initiativ til et møte for å avklare uenigheten.")
print("B) Avvente: du venter og håper de finner en løsning selv.")

svar = input("Ditt valg (A/B): ").upper()
while svar != "A" and svar != "B":
    print("Ugyldig valg. Skriv A eller B.")
    svar = input("Ditt valg (A/B): ").upper()

if svar == "A":
    valg2 = "felles møte"
    poeng = poeng + 1
    print()
    print("Hamdi og Hallgeir innser at de bare har misforstått hverandre.")
    print("De jobber godt sammen igjen, men møtet kostet tid, og dere er")
    print("bekymret for om dere blir ferdige i tide.")
else:
    valg2 = "avvente"
    print()
    print("Uten avklaring bygger spenningen seg opp, og konflikten blir personlig.")
    print("Progresjonen stopper opp, og tiden dere sparte må tas igjen senere.")

# Beslutning 3: Motivasjonen i teamet
print()
print("- BESLUTNING 3: Motivasjonen i teamet -")

# Teksten avhenger av hvor mange poeng Erling har fått så langt
if poeng == 2:
    print("Begge konfliktene er dempet, men alle er slitne.")
elif poeng == 1:
    print("Én av konfliktene er løst, men stemningen er fortsatt ujevn.")
else:
    print("Ingen av konfliktene er løst, og motivasjonen i teamet er på bunn.")
print("Milepælen er om tre uker.")
print()
print("A) Relasjonsbygging: du setter av tid til sosiale aktiviteter og tillit.")
print("B) Fremdrift: du prioriterer leveranser og resultater.")

svar = input("Ditt valg (A/B): ").upper()
while svar != "A" and svar != "B":
    print("Ugyldig valg. Skriv A eller B.")
    svar = input("Ditt valg (A/B): ").upper()

if svar == "A":
    valg3 = "relasjonsbygging"
    poeng = poeng + 1
    print()
    print("Alle i teamet koser seg på laser-tag. Du er fornøyd,")
    print("men litt stresset over timene som ikke gikk til prosjektet.")
else:
    valg3 = "fremdrift"
    print()
    print("Alle sliter seg helt ut, men dere får gjort mye til tross for dårlig stemning.")

# Utfall, bestemt av poengsummen
print()
print("= UTFALL =")
if poeng == 3:
    print("UTFALL 1: Teamet gjenoppretter tillit.")
    print("Konfliktene er løst, stemningen er god, og teamet går videre til norming-fasen.")
elif poeng == 2:
    print("UTFALL 2: Konflikten løses delvis.")
    print("Det er roligere i teamet, men relasjonene er fortsatt sårbare.")
else:
    print("UTFALL 3: Prosjektet mister samhold.")
    print("Konfliktene har ikke blitt løst, og prosjektet forsinkes.")

# Oppsummering av valgene som ble lagret underveis
print()
print("Dine valg:", valg1, "-", valg2, "-", valg3)
print("Poengsum:", poeng, "av 3")