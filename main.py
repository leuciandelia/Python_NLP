import re

class AnalizorText:
    def __init__(self):
        self.cuvinte_ignorate = {'de', 'la', 'pe', 'cu', 'un', 'o', 'este', 'sunt', 'a', 'in', 'si', 'sa'}

        # Stocam direct RADACINILE termenilor tehnici.
        # Ex: 'presiune' -> 'presiun', 'eroare' -> 'eroar', 'telemetrie' -> 'telemetri'
        self.radacini_tehnice = {'senzor', 'telemetri', 'presiun', 'eroar', 'sistem', 'motor', 'dat'}

    def curata_textul(self, text):
        text_mic = text.lower()
        text_fara_semne = re.sub(r'[^\w\s\+\-\=\*\/]', '', text_mic)
        cuvinte = text_fara_semne.split()

        cuvinte_bune = []
        for cuvant in cuvinte:
            if cuvant not in self.cuvinte_ignorate:
                cuvinte_bune.append(cuvant)

        return cuvinte_bune

    def cauta_formule(self, text):
        regula_ecuatie = r'[a-zA-Z0-9_]+\s*=\s*[a-zA-Z0-9_\s\+\-\*\/]+'
        rezultate = re.findall(regula_ecuatie, text)
        return [rezultat.strip() for rezultat in rezultate]

    def obtine_radacina(self, cuvant):
        # Taiem sufixele comune de la finalul cuvantului
        # Ordinea: incepem cu cele mai lungi ca sa nu taiem gresit
        sufixe = ['ului', 'ilor', 'ile', 'ul', 'le', 'ii', 'ea', 'i', 'e', 'a']

        for sufix in sufixe:
            if cuvant.endswith(sufix):
                # Taiem sufixul
                radacina = cuvant[:-len(sufix)]
                # Ne asiguram ca nu distrugem cuvinte prea scurte
                if len(radacina) >= 3:
                    return radacina
        return cuvant

    def alege_categoria(self, text, cuvinte_curate):
        if self.cauta_formule(text):
            return "Formulă matematică"

        scor_tehnic = 0
        for cuvant in cuvinte_curate:
            # 1. Extragem radacina (ex: 'senzorului' devine 'senzor')
            radacina = self.obtine_radacina(cuvant)

            # 2. Cautare INSTANTA
            if radacina in self.radacini_tehnice or cuvant in self.radacini_tehnice:
                scor_tehnic += 1

        if scor_tehnic > 0:
            return "Problemă tehnică"
        else:
            return "Text normal / Discuție"

    def proceseaza(self, text_utilizator):
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
        text_primit = input("\nText: ")

        if text_primit.lower() in ['exit', 'stop', 'gata']:
            print("Sistem oprit.")
            break

        if not text_primit.strip():
            continue

        analizor.proceseaza(text_primit)