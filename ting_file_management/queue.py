from collections import deque
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return not len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.popleft()

    def search(self, index):
        if index < 0 or index > len(self) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
