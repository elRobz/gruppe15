# IS-118 gruppeoppgave 2 - Del 2
# Interaktiv historie: Erling og prosjektteamet i storming-fasen

# Variabler
Relasjon = 0
Progresjon = 0
valg1 = ""
valg2 = ""
valg3 = ""

# Introduksjon
print("Hei Erling! Du har jo nå kommet godt i gang med prosjektet om kommunens")
print("nye digitale medborgerportal. Det har gått seks uker siden du og teamet")
print("møttes for første gang. Det hele startet bra, med god stemning og høy")
print("motivasjon. Men nå har dere gått inn i storming-fasen, og det er flere")
print("konflikter i teamet. Du må nå ta noe vanskelige valg for å få gjennomført")
print("prosjektet. Første prototype skal tross alt være klar om tre uker!")
print("=" * 75)
print("Du vil nå få presentert tre situasjoner du må ta stilling til. Valgene du")
print("tar vil påvirke relasjonen i teamet ditt, og progresjonen i prosjektet.")
print("LYKKE TIL!")
print("=" * 75)
# Beslutning 1: Silje og Elias
print("Konflikt 1: Silje og Elias er uenige om teknologi og design, og det har")
print("nå blitt personlig. Møtene ender stadig i krangel. Hva gjør du?")

print("A) Individuelle samtaler med Silje og Elias")
print("B) Ta konflikten opp i plenum")
valg1 = input("Skriv inn ditt valg (A eller B): ")

while valg1 != "A" and valg1 != "B":
    print("Ugyldig valg.")
    valg1 = input("Skriv inn ditt valg (A eller B): ")
if valg1 == "A":
    print("Du tar et møte med hver av dem. Begge får muligheten til å si")
    print("sin mening uten publikum, og temperaturen synker. Teknologivalget")
    print("er fortsatt uavkklart, og du begynner å få dårlig tid.")
elif valg1 == "B":
    print("Du tar det opp i plenum. Det blir en hard diskusjon,")
    print("og til slutt er det Elias sin løsning som blir stemt frem. Denne")
    print("løsningen viser seg å være god, men stemningen blir dårligere i")
    print("hele teamet, da flere mener at folk kun stemte på den personen")
    print("de likte best.")


print("=" * 75)
# Beslutning 2: Hamdi og Hallgeir
print("Konflikt 2: Hamdi og Hallgeir er uenige om hvordan kommunens innbyggere")
print("skal kunne delta i digitale folkemøter. Hamdi ønsker en kontrollert løsning")
print("gjennom kommunens eksisterende platform, mens Hallgeir ønsker et mer åpent")
print("dialogbasert system. Foreløpig er det ingen stor krangel. Likevel vet du at")
print("måten du håndterer dette er viktig for om teamet blir værende i stormen,")
print("eller om dere kommer dere videre til norming. Hva gjør du?")

print("A) Ta et felles møte med teamet")
print("B) Avvente")
print("C) Felles møte med HR")
valg2 = input("Skriv inn ditt valg (A, B eller C): ")

while valg2 != "A" and valg2 != "B" and valg2 != "C":
    print("Ugyldig valg.")
    valg2 = input("Skriv inn ditt valg (A, B eller C): ")
if valg2 == "A":
    print("Du tar et felles møte med teamet, og Hamdi og Hallgeier innser at de")
    print("egentlig bare har misforstått hverandre. Nå jobber de godt sammen, men")
    print("de har brukt mye tid på dette, og du begynner å få dårlig tid.")
elif valg2 == "B":
    print("Du velger å avvente, og la Hamdi og Hallgeir finne ut av det selv.")
    print("Dette fører til at spenningen mellom dem øker, frustrasjonen vokser,")
    print("og progresjonen stopper. Tiden du sparte på kort sikt, må du gjenbetale")
    print("dobbelt for å komme tilbake på rett spor.")
elif valg2 == "C":
    print("Du tar et felles møte med Hamdi, Hallgeir og HR. Konflikten løser seg")
    print("tidlig nok til at de kan fortsette der de slapp, uten å ha kastet bort")
    print("noe særlig tid.")


print("=" * 75)
# Beslutning 3: Progresjon eller relasjonsbygging
print("Nå har du fått håndtert de to konfliktene i teamet. Likevel gjenstår det")
print("en viktig avgjørelse: Skal du sette av tid til sosiale aktiviteter og")
print("relasjonsbygging, eller skal du fokusere på å få ferdig første prototype?")

print("A) Sosiale aktiviteter og relasjonsbygging")
print("B) Fokus på første prototype")
valg3 = input("Skriv inn ditt valg (A eller B): ")
while valg3 != "A" and valg3 != "B":
    print("Ugyldig valg.")
    valg3 = input("Skriv inn ditt valg (A eller B): ")
if valg3 == "A":
    print("Du kommer med en gladnyhet til teamet: Alle skal på Laser tag!.")
    print("Alle koser seg masse, og setter stor pris på en pause fra prosjektet.")
    print("Selv om det ble brukt en del tid som kunne vært brukt på prototypen,")
    print("føler du at dette var det rette valget. Teamet er mer sammensveiset, og")
    print("mer motiverte enn noen gang")
elif valg3 == "B":
    print("Du velger å fokusere på prototypen, og setter opp en streng arbeidsplan.")
    print("Teamet jobber hardt, og får mye gjort. Men flere føler seg både utslitt")
    print("og utbrent. Du har fått mye gjort, men er redd for at dette kan gå utover")
    print("fremtidig arbeid i teamet.")


print("=" * 75)
# Avslutning med 3 mulig utfall
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("Gratulerer! Du har håndtert konfliktene på en god måte, og teamet")
    print("har kommet seg gjennom storming-fasen. Dere går nå videre til norming!")
elif valg1 == "A" and valg2 == "A" and valg3 == "B":
    print("Gratulerer! Du har håndtert konfliktene på en god måte, og teamet")
    print("har kommet seg gjennom storming-fasen. Dere går nå videre til norming!")
elif valg1 == "A" and valg2 == "B" and valg3 == "A":
    print("Summen av avgjørelsene din gjorde at prosjektet mister samhold")
    print("og blir forsinket. Prototypen leveres ikke i tide.")
elif valg1 == "A" and valg2 == "B" and valg3 == "B":
    print("Du har løst konfliktene delvis. Prototypen blir klar i tide, men")
    print("relasjonene i teamet er sårbare.")
elif valg1 == "A" and valg2 == "C" and valg3 == "A":
    print("Gratulerer! Du har håndtert konfliktene på en god måte, og teamet")
    print("har kommet seg gjennom storming-fasen. Dere går nå videre til norming!")
elif valg1 == "A" and valg2 == "C" and valg3 == "B":
    print("Du har løst konfliktene delvis. Prototypen blir klar i tide, men")
    print("relasjonene i teamet er sårbare.")
elif valg1 == "B" and valg2 == "A" and valg3 == "A":
    print("Du har løst konfliktene delvis. Prototypen blir klar i tide, men")
    print("relasjonene i teamet er sårbare.")
elif valg1 == "B" and valg2 == "A" and valg3 == "B":
    print("Summen av avgjørelsene din gjorde at prosjektet mister samhold")
    print("og blir forsinket. Prototypen leveres ikke i tide.")
elif valg1 == "B" and valg2 == "B" and valg3 == "A":
    print("Summen av avgjørelsene din gjorde at prosjektet mister samhold")
    print("og blir forsinket. Prototypen leveres ikke i tide.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Summen av avgjørelsene din gjorde at prosjektet mister samhold")
    print("og blir forsinket. Prototypen leveres ikke i tide.")
elif valg1 == "B" and valg2 == "C" and valg3 == "A":
    print("Summen av avgjørelsene din gjorde at prosjektet mister samhold")
    print("og blir forsinket. Prototypen leveres ikke i tide.")
elif valg1 == "B" and valg2 == "C" and valg3 == "B":
    print("Du har løst konfliktene delvis. Prototypen blir klar i tide, men")
    print("relasjonene i teamet er sårbare.")
