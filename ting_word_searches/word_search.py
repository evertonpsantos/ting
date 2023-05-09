from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    for file in instance.data:
        found_results = [{
            "arquivo": file["nome_do_arquivo"],
            "palavra": word,
            "ocorrencias": [
                {"linha": index + 1}
                for index, line in enumerate(file["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }]

        if len(found_results[0]['ocorrencias']) == 0:
            return []
        return found_results


def search_by_word(word, instance):
    """Aqui irá sua implementação."""
