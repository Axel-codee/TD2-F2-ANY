import sys

from corriges.chiffrement_decalage import chiffrer


def main():
	if len(sys.argv) != 2:
		print(f"Usage : {sys.argv[0]} chemin_du_fichier", file=sys.stderr)
		return 1

	chemin = sys.argv[1]
	try:
		with open(chemin, encoding="utf-8") as fichier:
			texte = fichier.read()
	except OSError as erreur:
		print(f"Impossible de lire {chemin} : {erreur}", file=sys.stderr)
		return 1

	for decalage in range(26):
		print(f"\nDécalage essayé : {decalage}")
		print(chiffrer(texte, -decalage), end="" if texte.endswith("\n") else "\n")
		if decalage < 25:
			input("Appuyez sur Entrée pour essayer le décalage suivant...")

	return 0


if __name__ == "__main__":
	sys.exit(main())

# On trouve le message concernant l'alunissage d'Apollo 11 avec un décalage de 11