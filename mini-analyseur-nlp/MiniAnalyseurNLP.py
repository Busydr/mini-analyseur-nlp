class AnalyseTexte:

    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.mots = []
        self.contenu = ""
        self.nb_phrases = 0


    def lire_et_nettoyer(self):
        try:
            with open(self.nom_fichier, "r", encoding="utf-8") as f:
                self.contenu = f.read()

            # compter les phrases avant nettoyage
            self.nb_phrases = self.contenu.count(".")

            # nettoyer le texte
            for char in ".,!?:;":
                self.contenu = self.contenu.replace(char, "")

            self.contenu = self.contenu.lower()

            # transformer en liste de mots
            self.mots = self.contenu.split()

        except FileNotFoundError:
            print("Erreur : fichier introuvable")


    def nombre_total_mots(self):
        return len(self.mots)


    def nombre_mots_uniques(self):
        return len(set(self.mots))


    def mots_plus_frequents(self):
        frequences = {}

        for mot in self.mots:
            if mot in frequences:
                frequences[mot] += 1
            else:
                frequences[mot] = 1

        top3 = sorted(
            frequences,
            key=frequences.get,
            reverse=True
        )[:3]

        return top3, frequences


    def nombre_phrases(self):
        return self.nb_phrases


    def longueur_moyenne(self):

        if len(self.mots) == 0:
            return 0

        longueur = 0

        for mot in self.mots:
            longueur += len(mot)

        return round(longueur / len(self.mots), 2)


    def afficher_rapport(self):

        top3, frequences = self.mots_plus_frequents()

        print("=== RAPPORT D'ANALYSE ===")
        print("Nombre total de mots :", self.nombre_total_mots())
        print("Nombre de mots uniques :", self.nombre_mots_uniques())

        print("Top 3 mots les plus fréquents :")

        for mot in top3:
            print(" ", mot, ":", frequences[mot])

        print("Longueur moyenne des mots :", self.longueur_moyenne())
        print("Nombre de phrases :", self.nombre_phrases())


    def sauvegarder_rapport(self):

        top3, frequences = self.mots_plus_frequents()

        with open("rapport.txt", "w", encoding="utf-8") as f:

            f.write("=== RAPPORT D'ANALYSE ===\n")
            f.write("Nombre total de mots : " + str(self.nombre_total_mots()) + "\n")
            f.write("Nombre de mots uniques : " + str(self.nombre_mots_uniques()) + "\n")

            f.write("Top 3 mots les plus fréquents :\n")

            for mot in top3:
                f.write("  " + mot + " : " + str(frequences[mot]) + "\n")

            f.write("Longueur moyenne des mots : " + str(self.longueur_moyenne()) + "\n")
            f.write("Nombre de phrases : " + str(self.nombre_phrases()) + "\n")


        print("Rapport sauvegardé dans rapport.txt")



# PROGRAMME PRINCIPAL

nom = input("Entrez le nom du fichier : ")

analyseur = AnalyseTexte(nom)

analyseur.lire_et_nettoyer()

analyseur.afficher_rapport()

analyseur.sauvegarder_rapport()