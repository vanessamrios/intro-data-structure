import sys

from ting_file_management.file_management import txt_importer


def file_exists(path_file, instance) -> bool:
    for index in range(0, len(instance)):
        if (instance.search(index) == path_file):
            return True
    return False


def process(path_file, instance):
    if file_exists(path_file, instance):
        return

    file = txt_importer(path_file)
    instance.enqueue(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
