from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    found_results = list()

    for file in instance.data:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if len(occurrences) > 0:
            found_results.append(
                {
                    "arquivo": file["nome_do_arquivo"],
                    "palavra": word,
                    "ocorrencias": occurrences,
                }
            )

    return found_results


def search_by_word(word, instance: Queue):
    found_results = list()

    for file in instance.data:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1, "conteudo": line})

        if len(occurrences) > 0:
            found_results.append(
                {
                    "arquivo": file["nome_do_arquivo"],
                    "palavra": word,
                    "ocorrencias": occurrences,
                }
            )

    return found_results
