# Instalacija

## Grafički instalater (samo GUI, bez CLI)

Ako vam je teško da koristite terminal i ne treba vam CLI (rad sa aplikacijom kroz komandnu liniju),
preuzmite gotov instalater sa stranice izdanja:

**[https://github.com/andgineer/ibkr-porez-py/releases](https://github.com/andgineer/ibkr-porez-py/releases)**

Pošto instalater uključuje Python interpreter, veoma je veliki, a grafička aplikacija koju
instalira je takođe velika i spora.

Ako je moguće, razmotrite instalaciju pomoću `uv tool` (vidi ispod) — dobićete istu grafičku aplikaciju
ali mnogo lakšu. Sama instalacija će biti jednostavnija, mnogo brža i bez problema.

=== "macOS"
    Preuzmite najnoviji `.dmg` fajl.
    Pošto aplikacija nije potpisana Apple sertifikatom, macOS može da je blokira pri prvom otvaranju:

    > _"IBKR Porez" je oštećen i ne može da se otvori. Treba ga premestiti u smeće._

    **Ne premeštajte u smeće.** Umesto toga:

    1. Otvorite **System Settings -> Privacy & Security**
    2. Pri dnu odeljka Security pojaviće se poruka o blokiranoj aplikaciji — kliknite **Open Anyway**
    3. U sledećem dijalogu potvrdite otvaranje

    Možda će biti potrebno da ove korake ponovite **dva puta**:
    - prvo pri otvaranju preuzetog instalatera (`.dmg`)
    - a zatim pri prvom pokretanju instalirane aplikacije iz `/Applications`

    Nakon toga aplikacija bi trebalo da se pokreće bez upozorenja.

=== "Windows"
    Preuzmite najnoviji `.msi` fajl.
    Pošto instalater nije digitalno potpisan, Windows može prikazati bezbednosna upozorenja.

    Ako pregledač blokira preuzimanje (na primer u Microsoft Edge):
    1. Otvorite panel preuzimanja u pregledaču (`Ctrl+J`)
    2. Pronađite blokirano `.msi` preuzimanje
    3. Kliknite **Keep** -> **Show more** -> **Keep anyway**

    Pri pokretanju instalatera, Windows može prikazati poruku **Windows protected your PC**:
    1. Kliknite **More info**
    2. Kliknite **Run anyway**

    Može se pojaviti i User Account Control dijalog sa porukom **Unknown publisher**.
    Ako je fajl preuzet sa zvanične stranice izdanja, kliknite **Yes** za nastavak.

    Nakon instalacije, aplikacija bi trebalo da se pokreće normalno.

---

## Instalacija pomoću uv tool

Instalirajte Astral [uv tool](https://docs.astral.sh/uv/getting-started/installation/)

### Instalacija aplikacije

```bash
uv tool install ibkr-porez --python 3.12
```
