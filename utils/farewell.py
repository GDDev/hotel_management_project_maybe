import random

# Criando opções de despedidas
def random_farewell():
    # Criando lista com possíveis despedidas
    goodbyes = [
        'Isso é tudo pe-pessoal!',
        'Hasta la vista, baby!',
        'Que a força esteja com você!',
        'Ao infinito e além!',
        'Obrigado por utilizar de nossos serviços, volte sempre!!!',
        'Ficamos grato em ter feito parte disso com voce, volte sempre :)!',
        'Obrigado seu Zé Ruela, agora pague-nos!'
    ] 
    # Retornando uma despedida aleatória
    return random.choice(goodbyes)
