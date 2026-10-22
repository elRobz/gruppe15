# Interaktiv historie: Erling og stormen i prosjektteamet
# IS-118, gruppeoppgave 2, del 2

# Introduksjon
print("ERLING OG STORMEN")
print("Det har gått seks uker siden Erling samlet prosjektteamet.")
print("Teamet er nå i storming-fasen.")
print("Silje og Elias er i konflikt om teknologi og design.")
print("Hamdi og Hallgeir er uenige om innbyggerdeltakelse.")
print("Prototypen skal være klar om tre uker.")
print("Du er Erling. Dine valg avgjør hvordan det går.")
print()

# Poeng som lagrer hvor godt Erling håndterer situasjonen (maks 3)
poeng = 0

# Beslutning 1: Silje og Elias
print("BESLUTNING 1: Konflikten mellom Silje og Elias")
print("a) Ta enesamtaler med Silje og Elias hver for seg")
print("b) Ta konflikten opp i plenum")
valg1 = input("Ditt valg (a/b): ")

# Spør på nytt så lenge svaret er ugyldig
while valg1 != "a" and valg1 != "b":
    print("Ugyldig valg. Skriv a eller b.")
    valg1 = input("Ditt valg (a/b): ")

if valg1 == "a":
    poeng = poeng + 1
    print("Begge får snakke fritt uten publikum, og temperaturen synker.")
    print("Teknologivalget er fortsatt uavklart.")
else:
    print("Konflikten blir åpen, og teamet blir delt i to leire.")
print()

# Beslutning 2: Hamdi og Hallgeir
print("BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir")
print("a) Ta initiativ til et felles møte")
print("b) Avvente og håpe at de løser det selv")
valg2 = input("Ditt valg (a/b): ")

while valg2 != "a" and valg2 != "b":
    print("Ugyldig valg. Skriv a eller b.")
    valg2 = input("Ditt valg (a/b): ")

if valg2 == "a":
    poeng = poeng + 1
    print("Hamdi og Hallgeir blir hørt, og dere finner en mellomting.")
    print("Møtet tok tid like før prototypen.")
else:
    print("Du sparer tid nå, men frustrasjonen vokser.")
print()

# Beslutning 3: Motivasjon i teamet
print("BESLUTNING 3: Motivasjonen i teamet")
print("a) Sette av tid til relasjonsbygging og sosiale aktiviteter")
print("b) Prioritere fremdrift og leveranser")
valg3 = input("Ditt valg (a/b): ")

while valg3 != "a" and valg3 != "b":
    print("Ugyldig valg. Skriv a eller b.")
    valg3 = input("Ditt valg (a/b): ")

if valg3 == "a":
    poeng = poeng + 1
    print("Tilliten i teamet bygges opp igjen, men tiden er knapp.")
else:
    print("Teamet holder fokus på prototypen, men stemningen er spent.")
print()

# Avslutning: tre mulige utfall basert på poeng
print("UTFALL")

if poeng == 3:
    print("NORMING: Konfliktene er håndtert og tilliten er gjenopprettet.")
    print("Teamet går videre til norming-fasen.")
elif poeng == 2:
    print("DELVIS LØST: Konfliktene er dempet, men relasjonene er sårbare.")
    print("Nye uenigheter kan oppstå.")
else:
    print("FORSINKET: Konfliktene er ikke håndtert.")
    print("Teamet mister samhold, og prototypen blir forsinket.")

print("Du fikk " + str(poeng) + " av 3 poeng. Takk for at du spilte!")
