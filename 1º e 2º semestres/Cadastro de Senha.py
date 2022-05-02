def validaSenhaT(senha):
    if len(senha) == 8:
        return True
    return False

def validaSenhaL(senha):
    for i in range(len(senha)):
        if senha[i].isupper():
            return True
    return False

def validaSenhaN(senha):
    for i in range(len(senha)):
        if senha[i].isdigit():
            return True
    return False

def validaSenhaC(senha):
    import string
    c = string.punctuation
    for i in range(len(senha)):
        if senha[i] in c:
            return True
    return False


def sugestaoSenha():
    from random import randint, choice, sample
    import string
    lM = choice(string.ascii_uppercase)
    n = randint(1,9)
    nS = str(n)
    c = choice(string.punctuation)
    lm = ''

    for i in range(5):
         l = choice(string.ascii_letters.lower())
         lm += l
    s = lM + nS + c + lm
    geraSenha = sample(s, 8)
    sugestSenha = ''.join(geraSenha)
    return sugestSenha


print('Cadastre uma senha com exatamente 8 caracteres, contendo pelo menos 1 letra maiúscula, 1 número e 1 caractere especial.\n')
senha = input('Senha: ')


if validaSenhaT(senha) and validaSenhaL(senha) and validaSenhaN(senha) and validaSenhaC(senha):
    print('Senha cadastrada com sucesso!')
else:
    if not validaSenhaT(senha):
        print('Senha inválida! O tamanho da senha precisa ser de 8 caracteres.')
    elif not validaSenhaL(senha) and validaSenhaN(senha) and not validaSenhaC(senha):
        print('Senha inválida! A senha precisa ter pelo menos uma letra maiúscula e um caractere especial.')
    elif not validaSenhaN(senha) and validaSenhaL(senha) and not validaSenhaC(senha):
        print('Senha inválida! A senha precisa ter pelo menos um número e um caractere especial.')
    elif validaSenhaC(senha) and not validaSenhaL(senha) and not validaSenhaN(senha):
        print('Senha inválida! A senha precisa ter pelo menos um número e uma letra maiúscula.')
    elif not validaSenhaL(senha) and not validaSenhaN(senha) and not validaSenhaC(senha):
        print('Senha inválida! A senha precisa ter pelo menos uma letra maiúscula, um número e um caractere especial.')
    elif validaSenhaN(senha) and validaSenhaL(senha) and not validaSenhaC(senha):
        print('Senha inválida! A senha precisa ter pelo menos um caractere especial.')
    elif validaSenhaN(senha) and validaSenhaC(senha) and not validaSenhaL(senha):
        print('Senha inválida! A senha precisa ter pelo menos uma letra maiúscula.')
    elif validaSenhaL(senha) and not validaSenhaN(senha) and validaSenhaC(senha):
        print('Senha inválida! A senha precisa ter pelo menos um número.')
    s = sugestaoSenha()
    print(f'Sugestão de senha: {s}')

