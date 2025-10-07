# Importa os módulos necessários: 'random' para aleatoriedade e 'string' para ter acesso a listas de caracteres
import random
import string

def gerar_senha(tamanho):
    """
    Esta função gera uma senha segura com o tamanho especificado.
    Ela mistura letras maiúsculas, minúsculas, números e símbolos...
    """
    # Define o universo de caracteres possíveis para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo caracteres aleatórios do universo definido
    # A função 'join' é uma forma eficiente de construir a string final
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

# --- Bloco principal do programa ---
if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")
    
    try:
        # Pede ao usuário o tamanho desejado para a senha
        tamanho_da_senha = int(input("Digite o comprimento desejado para a senha (ex: 16): "))
        
        # Gera a senha chamando a função que criamos
        senha_gerada = gerar_senha(tamanho_da_senha)
        
        # Mostra a senha gerada para o usuário
        print(f"\nSua senha segura é: {senha_gerada}")

    except ValueError:
        # Captura o erro se o usuário não digitar um número
        print("\nErro: Por favor, digite um número válido.")