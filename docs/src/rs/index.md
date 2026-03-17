# Brzi start
Automatizovano generisanje poreske prijave PPDG-3R (porez na kapitalnu dobit) i PP OPO (porez na prihode od kapitala) za korisnike Interactive Brokers u Srbiji.
Program automatski preuzima podatke o transakcijama i kreira gotov XML fajl za otpremanje, konvertujući sve cene u dinare (RSD).

[Instalirajte ibkr-porez ↗](installation.md)

## Grafički interfejs

   > Ako ste instalirali preko `uv tool`, grafički interfejs se pokreće kao `ibkr-porez` bez parametara.

Ako koristite **grafički interfejs**, podesite svoje podatke (dugme `Config`) i za osvežavanje podataka i kreiranje prijava samo koristite dugme `Sync`.

Sve potrebne instrukcije su ugrađene u aplikaciju.

## Komandna linija

Ako je **terminal** vaše prirodno okruženje (AI agenti i hrabri ljudi).

   > ⚠️ Dok je grafički interfejs pokrenut, ne koristite komandnu liniju,
   > jer istovremeni rad može izazvati greške u bazi podataka.

- [Konfiguracija (config) ↗](usage.md#konfiguracija-config)
- [Uvoz istorijskih podataka (import) ↗](usage.md/#uvoz-istorijskih-podataka-import)

> ⚠️ **Uvoz je potreban samo ako imate više od godinu dana istorije transakcija u Interactive Brokers.** Flex Query omogućava preuzimanje podataka za najviše poslednju godinu, pa stariji podaci moraju biti učitani iz [punog izvoza u CSV fajl ↗](ibkr.md/#izvoz-pune-istorije-za-import-komandu).

=== "Brzo kreirati potrebnu prijavu"

    Ako želite brzo da kreirate konkretnu prijavu.

    [Preuzimanje najnovijih podataka (fetch) ↗](usage.md/#preuzimanje-podataka-fetch)

    [Kreiranje izveštaja (report) ↗](usage.md/#generisanje-poreskog-izvestaja-report)

    Otpremite kreirani XML na portal **ePorezi** (sekcija PPDG-3R).
        ![PPDG-3R](images/ppdg-3r.png)

=== "Automatsko kreiranje prijava"

    Ako želite automatski da dobijate sve potrebne prijave i pratite njihov status (podneta, plaćena).

    [Preuzimanje najnovijih podataka i kreiranje prijava (sync) ↗](usage.md/#sinhronizacija-podataka-i-kreiranje-prijava-sync)

    [Upravljanje prijavama ↗](usage.md/#upravljanje-prijavama)
