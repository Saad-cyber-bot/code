import pandas as pd
import re

# Les Excel-filen
original_fil = (r"C:\Users\logent\Desktop\Tingstad\statnr_2025-03-24 Ntex bil 2   NTEX9132 - ENJ45G.xlsb")  # Endre til riktig filnavn
renset_fil = (r"C:\Users\logent\Desktop\Tingstad\statnr_2025-03-24 Ntex bil 2   NTEX9132 - ENJ45G_renset.xlsb")  # Endre til riktig filnavn
feillogg_fill = (r"C:\Users\logent\Desktop\Tingstad\statnr_2025-03-24 Ntex bil 2   NTEX9132 - ENJ45G_feillogg.txt")  # Endre til riktig filnavn

df = pd.read_excel(original_fil, engine="pyxlsb", dtype=str)

# Definer regex-mønster for spesialtegn (alt unntatt bokstaver, tall og mellomrom)
spesialtegn_mønster = r"[^a-zA-Z0-9æøåÆØÅ ]"

feillogg_fill

# Initialiser feillogg som en tom liste
feillogg = []

# Gå gjennom hver kolonne og sjekk hver rad for spesialtegn
for kolonne in df.columns:
    
    for indeks, verdi in df[kolonne].items():  # Går gjennom hver celle
        if isinstance(verdi, str):  # Sjekk om verdien er en streng
            spesialtegn = re.findall(spesialtegn_mønster, verdi)  # Finn spesialtegn
            if spesialtegn:  # Hvis spesialtegn finnes

                feillogg.append([kolonne, indeks + 2, "".join(spesialtegn), verdi])  # Legg til feil i loggen
                df.at[indeks, kolonne] = re.sub(spesialtegn_mønster, "",verdi)  # Fjern spesialtegn fra cellen


df.to_excel(renset_fil, index=False, engine="pyxlsb")
print(f"\n ny fil uten spesialtegn er lagret som '(renset_fil)'")

if feillogg:
    df_feillogg = pd.DataFrame(feillogg, columns=["kolonne", "Rad", "spesialtegn", "Opprinnelig Verdi"])
    df_feillogg.to_excel(feillogg_fill, index=False, engine="pyxlsb")
    print(f" Feillogg er lagret som '(feillogg_fill)'")
else:
    print("ingen spesialtegn ble funnet, ingen feillogg laget.")