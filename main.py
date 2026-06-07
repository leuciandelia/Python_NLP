import re

class AnalizorText:
    def __init__(self):
        # Cuvinte ignorate (stop-words)
        self.cuvinte_ignorate = {'de', 'la', 'pe', 'cu', 'un', 'o', 'este', 'sunt', 'a', 'in', 'si', 'sa'}

        # Cuvinte cheie pentru domeniul tehnic
        self.termeni_tehnici = {'senzor', 'telemetrie', 'presiune', 'eroare', 'sistem', 'motor', 'date'}

    def curata_textul(self, text):
        # Litere mici pentru uniformitate
        text_mic = text.lower()

        # Pastram doar litere, cifre si operatori matematici
        text_fara_semne = re.sub(r'[^\w\s\+\-\=\*\/]', '', text_mic)

        # Spargem textul in cuvinte
        cuvinte = text_fara_semne.split()

        # Filtram cuvintele ignorate
        cuvinte_bune = []
        for cuvant in cuvinte:
            if cuvant not in self.cuvinte_ignorate:
                cuvinte_bune.append(cuvant)

        return cuvinte_bune

    def cauta_formule(self, text):
        # Cautam tipare de ecuatii (ex: x = y + 2)
        regula_ecuatie = r'[a-zA-Z0-9_]+\s*=\s*[a-zA-Z0-9_\s\+\-\*\/]+'
        rezultate = re.findall(regula_ecuatie, text)

        # Curatam spatiile inutile
        return [rezultat.strip() for rezultat in rezultate]

    def alege_categoria(self, text, cuvinte_curate):
        # Prioritate 1: verificam daca exista formule
        if self.cauta_formule(text):
            return "Formulă matematică"

        # Calculam scorul pentru termeni tehnici
        scor_tehnic = 0
        for cuvant in cuvinte_curate:
            if cuvant in self.termeni_tehnici:
                scor_tehnic += 1

        # Clasificare finala
        if scor_tehnic > 0:
            return "Problemă tehnică / Hardware"
        else:
            return "Text normal / Discuție"

    def proceseaza(self, text_utilizator):
        # Fluxul principal de executie
        print(f"\n--- Analizez: '{text_utilizator}' ---")

        cuvinte = self.curata_textul(text_utilizator)
        formule = self.cauta_formule(text_utilizator)
        rezultat = self.alege_categoria(text_utilizator, cuvinte)

        print(f"Cuvinte gasite: {cuvinte}")
        print(f"Formule gasite: {formule if formule else 'Nu exista'}")
        print(f"Concluzie: {rezultat}")


# --- Main / Bucla interactiva ---
if __name__ == "__main__":
    analizor = AnalizorText()
    print("Sistem pornit. Scrie 'exit' pentru oprire.")

    while True:
        # Citim de la tastatura
        text_primit = input("\nText: ")

        # Conditie de oprire
        if text_primit.lower() in ['exit', 'stop', 'gata']:
            print("Sistem oprit.")
            break

        # Ignoram inputul gol (doar Enter)
        if not text_primit.strip():
            continue

        # Rulam analiza
        analizor.proceseaza(text_primit)