# IS-118 gruppeoppgave 2 - Del 2
# Interaktiv historie: Erling og prosjektteamet

# Introduksjon
print("ERLING OG PROSJEKTTEAMET")
print("Det har gått seks uker siden prosjektet startet.")
print("Nå har det oppstått konflikter i teamet.")
print("Du er Erling, og må prøve å få teamet til å samarbeide.")
print("Prototypen skal være klar om tre uker.")
print("=" * 50)

poeng = 0

# Beslutning 1: Silje og Elias
print("Beslutning 1: Silje og Elias")
print("Silje og Elias krangler om teknologi og design.")
print("A) Snakke med dem hver for seg")
print("B) Ta diskusjonen med hele teamet")

valg1 = input("Hva velger du (A eller B)? ").upper()

while valg1 != "A" and valg1 != "B":
    print("Ugyldig valg.")
    valg1 = input("Skriv A eller B: ").upper()

if valg1 == "A":
    poeng = poeng + 1
    print("Begge får forklare seg, og stemningen blir litt bedre.")
    print("Dere må fortsatt finne ut hvilken løsning dere skal bruke.")
else:
    print("Diskusjonen blir opphetet, og flere velger side.")
    print("Det blir vanskeligere å samarbeide.")
print("=" * 50)

# Beslutning 2: Hamdi og Hallgeir
print("Beslutning 2: Hamdi og Hallgeir")
print("De er uenige om hvordan innbyggerne skal delta på nett.")
print("A) Arrangere et møte for å finne en løsning")
print("B) La dem prøve å løse problemet selv")

valg2 = input("Hva velger du (A eller B)? ").upper()

while valg2 != "A" and valg2 != "B":
    print("Ugyldig valg.")
    valg2 = input("Skriv A eller B: ").upper()

if valg2 == "A":
    poeng = poeng + 1
    print("De får forklart meningene sine og blir enige om en løsning.")
    print("Møtet tar litt tid fra arbeidet med prototypen.")
else:
    print("Du sparer tid, men uenigheten vokser.")
    print("Teamet bruker etter hvert mer tid på konflikten.")
print("=" * 50)

# Beslutning 3: Motivasjon i teamet
print("Beslutning 3: Hvordan skal du motivere teamet?")
print("Teamet er slitent, og fristen nærmer seg.")
print("A) Arrangere en sosial aktivitet for teamet")
print("B) Bruke all tiden på å ferdigstille prototypen")

valg3 = input("Hva velger du (A eller B)? ").upper()

while valg3 != "A" and valg3 != "B":
    print("Ugyldig valg.")
    valg3 = input("Skriv A eller B: ").upper()

if valg3 == "A":
    poeng = poeng + 1
    print("Teamet får en pause og blir bedre kjent.")
    print("Alle får mer lyst til å jobbe sammen.")
else:
    print("Teamet får gjort mye arbeid.")
    print("Flere er slitne, og stemningen er fortsatt dårlig.")
print("=" * 50)

# Avslutning
print("SLUTTEN PÅ HISTORIEN")

if poeng == 3:
    print("NORMING: Teamet samarbeider bedre.")
    print("Konfliktene er håndtert, og dere går videre til norming.")
elif poeng == 2:
    print("DELVIS LØST: Teamet har kommet et stykke videre.")
    print("Noen problemer gjenstår, og relasjonene er fortsatt sårbare.")
else:
    print("FORSINKET: Konfliktene har gjort samarbeidet vanskelig.")
    print("Teamet mister samhold, og prototypen blir forsinket.")

print("Du fikk", poeng, "av 3 poeng.")
print("Takk for at du spilte!")
