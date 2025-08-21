
from collections import deque

class ChatMemory:
    def __init__(self, window_size: int = 5):
        self.window_size = window_size
        self.memory = deque(maxlen=window_size)

    def add_turn(self, speaker: str, text: str):
        self.memory.append(f"{speaker}: {text}")

    def get_context(self) -> str:
        return "\n".join(self.memory)
