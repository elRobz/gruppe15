# Variabler
valg_1 = ""
valg_2 = ""
valg_3 = ""
poeng = 0

# Introduksjon
print("Du spiller som Erling og er leder for et tverrfaglig team på 6 personer. Elias som er IT-rådgiver, Silje er ekstern UX/UI designer, Hamdi er representant fra kulturavdelingen, \n" \
      "Marcia er politisk rådgiver, Noa er sikkerhetsekspert og Hallgeir er brukerrepresentant fra en lokal innbyggerforening. \n"
      "Det er 6 uker siden du, prosjektlederen for utviklingen av kommunens nye digitale medborgerportal, samlet teamet for første gang. Det har vært \n"
      "en inspirerende oppstart med høy energi, men nå kommer de første prøvene for teamet.")

# Beslutning 1: Silje og Elias
print("Konflikt 1: Silje og Elias er uenige om teknologivalg og design, og det har nå blitt til en personkonflikt.")
print("Hva velger du å gjøre?")
print("A) Individuelle samtaler med problemskaperene.")
print("B) Ta konflikten opp i plenum.")

valg_1 = input("Skriv inn ditt valg A eller B: ").upper() # Bruker .upper() for å gi muligheten til at det er fleksibilitet for å skrive med stor og små bokstav
if valg_1 == "A":
    poeng = poeng + 1
    print("Du har et møte med Silje først og så Elias, teknologivalget er ikke valgt, men de kommer bedre overens. Du begynner nå å få dårlig tid.")
elif valg_1 == "B":
    print("Du har et felles møte hvor dere diskuterer teknologivalget og teamet bestemmer til slutt å bruke Elias sin løsning. \n"
          "Det er fremdeles dårlig steming mellom Elias og Silje.")
else:
    print("Ugyldig valg, spillet er ferdig.")
    exit() # Exit fordi jeg vil at koden skal fullføres om man velger noe annet svar alternativ som ikke står.

# Beslutning 2: Hamdi og Hallgeir
print("Konflikt 2: \n"
      "Samtidig som Elias og Silje sin konflikt holder på, har det oppstått spenning mellom Hallgeir og Hamdi. \n"
      "De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print("Hva velger du å gjøre? \n" 
      "A) Felles møte med teamet. \n"
      "B) Avvente og tro at de løser det mellom hverandre. \n"
      "C) Du tar initiativ og setter i gang et felles møte sammen med HR.")

valg_2 = input("Skriv inn valg A, B eller C: ").upper()
if valg_2 == "A":
    poeng = poeng + 1
    print("Uenighet håndteres tidlig, før den blir personlig, men kan føre til forsinkelser.")
elif valg_2 == "B":
    print("Du sparer tid på kort sikt, og de involverte kan finne en løsning selv. Dette fører til at frustrasjonen vokser siden problemet ikke er tatt grep i.")
elif valg_2 == "C":
    poeng = poeng + 1
    print("HR kommer inn som et nøytral tredjeparti og begge parter blir hørt uten at du oppleves som partisk. \n" \
    "HR involveringen kan også oppleves som opptrapping av situasjonen og at det blir til en formell sak.")
else:
    print("Feil valg, spillet er ferdig.")
    exit()

# Beslutning 3: Motivasjon i teamet
print("Du har valget mellom å velge om du vil at du skal ha fokus på fremdrift eller relasjonsbygging i teamet fremover. \n" 
      "Det har vært dårlig stemning mellom flere parter og du vil bestemme fremtiden av teamet ditt. \n"
      "Hva velger du å gjøre? \n" \
      "A) En gøy aktivitet som hele laget er med på? \n" \
      "B) Fokus på leveranser og resultat?")

valg_3 = input("Skriv inn valg A eller B: ").upper()
if valg_3 == "A":
    poeng = poeng + 1
    print("Teamet storkoste seg med aktiviteten og kommer godt overens med hverandre.")
elif valg_3 == "B":
    print("Du fikk i gang prototypen, men stemingen i teamet er elendigt.")
else:
    print("Feil valg, spillet er ferdig.")
    exit()

# Utfallene
if poeng == 3:
    print("Teamet gjenoppretter tillit og går videre til norming fasen.")
elif poeng == 2:
    print("Konfliktene løses delvis, men relasjonene er fortsett sårbare")
elif poeng == 1:
    print("Prosjektet mister samhold og forsinkes.")
else:
    print("Du feilet og er ikke egnet til å være gruppeleder.")