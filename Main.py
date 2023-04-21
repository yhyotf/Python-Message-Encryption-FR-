from methodes import rot13
from methodes import cesar
from methodes import vigenere
from methodes import polybe
from methodes import dechROT13
from methodes import dechCesar
message=str(input('Entrez le message que vous souhaitez chiffrer:' ))
methode=int(input('Choisissez la méthode de cryptage que vous souahitez utiliser: 1-ROT13 2-César 3-Vigenère 4-Polybe :'))
if methode==1:
    resultat=rot13(message)
elif methode==2:
    d=int(input('Entrez le décalage souhaité :' ))
    resultat=cesar(message,d)
elif methode==3:
    cle=str(input('Entrez la clé à utiliser en majuscule :' ))
    resultat=vigenere(message,cle)
elif methode==4:
    resultat=polybe(message)
print(resultat)

message2=str(input('Entrez le message que vous souhaitez déchiffrer :'))
methode2=int(input('Choissiez la méthode de cryptage utilisée pour chiffrer le message : 1-ROT13 2-César :'))
if methode2==1:
    resultat2=dechROT13(message2)
elif methode2==2:
    d2=int(input('Entrez le décalage utilisé :'))
    resultat2=dechCesar(message2,d2)
print(resultat2)
