def rangMaj(c):
    '''
    Cette fonction renvoie le rang d'une lettre dans l'alphabet si celle-ci est en majuscule
    '''
    assert type(c)==str
    return ord(c)-65
def rangMin(c):
    '''
    Cette fonction renvoie le rang d'une lettre dans l'alphabet si celle-ci est en minuscule
    '''
    assert type(c)==str
    return ord(c)-97

def cesar(M,D):
    '''
    Cette fonction permet de chiffrer un message en utilisant la méthode du chiffre de césar
    Prend en paramètre le message ainsi que le décalage souhaité
    Renvoie le message chiffré avec la méthode de césar
    '''
    assert type(M)==str
    assert type(D)==int
    R=''
    for c in M:
        if ('A'<=c<='Z'):
            R=R+chr(((rangMaj(c)+D)%26)+65)
        elif 'a'<=c<='z':
            R=R+chr(((rangMin(c)+D)%26)+97)
        else:
            R=R+c
    return R


def dechCesar(M,D):
    '''
    Cette fonction permet de déchiffrer un message chiffré avec la méthode du chiffre de césar
    Prend en paramètre le message chiffré et le décalage utilisé
    Renvoie le message déchiffré
    '''
    assert type(M)==str
    assert type(D)==int
    R=''
    for c in M:
        if ('A'<=c<='Z'):
            R=R+chr(((rangMaj(c)+26-D)%26)+65)
        elif 'a'<=c<='z':
            R=R+chr(((rangMin(c)+26-D)%26)+97)
    return R


def rot13(M):
    '''
    Cette fonction permet de chiffrer un message en utilisant la méthode rot13
    Prend en paramètre le message
    Renvoie le message chiffré avec la méthode rot13
    '''
    assert type(M)==str
    R=''
    for c in M:
        if ('A'<=c<='Z'):
            R=R+chr(((rangMaj(c)+13)%26)+65)
        elif 'a'<=c<='z':
            R=R+chr(((rangMin(c)+13)%26)+97)
        else:
            R=R+c
    return R

def dechROT13(M):
    '''
    Cette fonction permet de déchiffrer un message chiffré avec la méthode rot13
    Prend en paramètre le message chiffré
    Renvoie le message déchiffré
    '''
    assert type(M)==str
    R=''
    for c in M:
        if ('A'<=c<='Z'):
            R=R+chr(((rangMaj(c)+26-13)%26)+65)
        elif 'a'<=c<='z':
            R=R+chr(((rangMin(c)+26-13)%26)+97)
    return R


def vigenere(message,cle):
    '''
    Cette fonction permet de chiffrer un message en utilisant le chiffre de vigenère
    Prend en paramètre le message et la clé 
    Renvoie le message chiffré avec la méthode de vigenère
    '''
    assert type(message)==str
    assert type(cle)==str
    R=''
    j=0
    cle=cle.upper()
    for i in message:
        if ('A'<=i<='Z'):
            decalage=rangMaj(cle[j])
            R=R+chr(((rangMaj(i)+decalage)%26)+65)
            if j<=len(cle)-2:
                j+=1
            else:
                j=0
        elif 'a'<=i<='z':
            decalage=rangMaj(cle[j])
            R=R+chr(((rangMin(i)+decalage)%26)+97)
            if j<=len(cle)-2:
                j+=1
            else:
                j=0
        else:
            R=R+i
    return R








def polybe(message):
    '''
    Cette fonction permet de chiffrer un message en utilisant le Carré de Polybe
    Prend en paramètre le message 
    Renvoie le message chiffré avec le Carré de Polybe en utilisant l'alphabet usuelle
    '''
    assert type(message)==str
    resultat = ''
    carre=[['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
    for chr in message.upper():
        if chr == 'J':
            chr = 'I' 
        if chr == ' ':
            resultat += '  '
        else:
            for i in range(5):
                for j in range(5):
                    if carre[i][j] == chr:
                        x=i+1
                        y=j+1
                        resultat += str(x) + str(y) + " "
    return resultat
