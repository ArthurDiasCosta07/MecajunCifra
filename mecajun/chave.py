import random
def getKey():
    i = random.randint(0,99)
    with open("Chaves.txt","r") as c:
        for _ in range(i):
            c.readline()
        s = c.readline()
    s = list(s)
    for i in range(len(s)):
        upper = random.randint(0,1)
        if upper:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    print(f"SUA NOVA SENHA É: ",end="")
    for i in s:
        print(i,end="")
    print("Guarde esta inforação com sua vida.")
    return s
def encrypt(s,n):
    ls = list(s)
    ls = ls[0:-1]
    for i in range(len(ls)):
        if ls[i].isalpha():
            aux = ord(ls[i]) + n
            if ls[i].islower():
                while aux > 122:
                    aux -= 26
                while aux < 97:
                    aux += 26
            if ls[i].isupper():
                while aux > 90:
                    aux -= 26
                while aux < 41:
                    aux += 65
        else:
            aux = ord(ls[i])
        ls[i] = chr(aux)
    print(f"A SENHA ENCRIPTADA COM A CHAVE {n} É : ",end="")
    for i in ls:
        print(i,end="")
print("Olá engenheiro de defesa, se você está lendo isso a senha de hoje deve ser atualizada...\nLembre-se de atualizar o banco de dados (Chaves.txt) de tempos em tempos.")
s = getKey()
print("Vamos encriptar esta senha com a chave compartilhada com a equipe hoje, lembre-se que múltiplos de 26 não alteram a chave original.")
c = input("ENSIRA A CHAVE DO DIA -> ")
if not c.isdigit():
    c = input("Não erre novamente. ENSIRA A CHAVE DO DIA ->")
if not c.isdigit():
    print("Você foi avisado... Sua localização foi reportada para seus superiores e o programa irá fechar automaticamente. Permaneça onde você está.")
c = int(c)
encrypt(s,c)
print("\nOs jogos devem continuar, retorne amanhã.")