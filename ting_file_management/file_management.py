import sys


def txt_importer(path_file: str) -> list:
    if (path_file.endswith(".txt") is False):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# https://codare.aurelio.net/2007/01/30/python-imprimir-mensagens-de-erro-stderr/
# https://stackoverflow.com/questions/28633555/how-to-handle-filenotfounderror-when-try-except-ioerror-does-not-catch-it
