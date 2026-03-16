# hash_generator.py
def generate_hash(input_string):
    """
    Função que deveria gerar uma hash simples de
    uma string
    """

    hash_value = 0
    for char in input_string:
        hash_value += ord(char)

    return hash_value