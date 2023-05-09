import pytest
from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_management import txt_importer


def test_basic_priority_queueing():
    file_paths = [
        "statics/arquivo_teste.txt",
        "statics/novo_paradigma_globalizado-min.txt",
    ]

    formated_dicts = [
        {
            "nome_do_arquivo": file_name,
            "qtd_linhas": len(txt_importer(file_name)),
        }
        for file_name in file_paths
    ]

    priority_queue = PriorityQueue()

    with pytest.raises(IndexError):
        priority_queue.search(11)

    for dict in formated_dicts:
        priority_queue.enqueue(dict)
    assert len(priority_queue.regular_priority.data) == 1
    assert len(priority_queue.high_priority.data) == 1

    first_in_queue = priority_queue.search(0)
    assert first_in_queue == formated_dicts[0]

    priority_queue.dequeue()
    assert len(priority_queue.high_priority.data) == 0
    assert len(priority_queue.regular_priority.data) == 1
