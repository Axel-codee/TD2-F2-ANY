import subprocess
import sys

def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte à décoder (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()
    


def decoder(s): 
    """Réalise un déchiffrement de César à l'aide de la commande tr."""
    resultat = subprocess.run(
        ["tr", "D-ZABCd-zabc", "a-zA-Z"],
        input=s,
        capture_output=True,
        text=True
    )

    return resultat.stdout

    
if __name__ == "__main__":
    # tuto()
    s = lire_stdin()
    print("Chaine à traiter : " + s)
    s2 = decoder(s)
    print("Déchiffrement : " + s2)

# La pionière en questioin est Margaret Hamilton