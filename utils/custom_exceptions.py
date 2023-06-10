# Criando exceção para opções inválidas
class InvalidChoiceError(Exception):
    def __init__(self, message='Opção inválida, tente novamente.'):
        super().__init__(message)

# Criando exceção para tentativas de login esgotadas
class LoginError(Exception):
    def __init__(self, message='Impossível realizar login.'):
        super().__init__(message)

# Criando exceção para falha de permissão em realização de funções
class PermissionError(Exception):
    def __init__(self, message='Você não possue permissão para realizar esta ação.'):
        super().__init__(message)

class RoomTypeError(Exception):
    def __init___(self, message='Tipo inválido para quarto.'):
        super().__init__(message)
