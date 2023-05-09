import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    if len(instance.data) != 0:
        for dict in instance.data:
            if dict['nome_do_arquivo'] == path_file:
                return None

    imported_txt_list = txt_importer(path_file)

    dict_format = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(imported_txt_list),
        'linhas_do_arquivo': imported_txt_list
    }

    instance.enqueue(dict_format)

    print(dict_format, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
