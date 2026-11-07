from gguf import GGUFReader, dequantize
from llama_cpp import Llama
import numpy as np
from abc import ABC

from pathlib import Path
HOME = Path(__file__).resolve().parents[2]
DIR = HOME / "control" / "llm"
MODEL = str(DIR / "fly-behavior-classifier.Q4_K_M.gguf")


class Drosophila(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__llm = Llama(
            model_path=MODEL,
            embedding=True,  # Obrigatório para modelos BERT/DistilBERT
            pooling_type=2,
            verbose=False
        )
        self.__reader = GGUFReader(self.__llm.model_path)
        self.__cls = {
            t.name: dequantize(t.data, t.tensor_type)
            for t in self.__reader.tensors
            if t.name.startswith("cls.")
        }

        self.__LABELS = [
            "move_forward",
            "fly",
            "turn_left",
            "turn_right",
            "spin_360",
            "evade_threat",
            "land_on_food",
        ]

    def chat(self, estimulo: str) -> str:
        emb = np.array(
            self.__llm.create_embedding(estimulo)["data"][0]["embedding"], dtype=np.float32
        )
        vec = (emb[0] if emb.ndim == 2 else emb) * np.sqrt(768.0)
        hidden = np.maximum(0, vec @ self.__cls["cls.weight"].T + self.__cls["cls.bias"])
        logits = hidden @ self.__cls["cls.output.weight"].T + self.__cls["cls.output.bias"]
        return self.__LABELS[int(np.argmax(logits))]


if __name__ == "__main__":
    # Teste rápido
    mosca = Drosophila()
    for t in [
        "clear path walk forward",
        "takeoff wings",
        "turn left",
        "sugar smell",
        "predator attack",
    ]:
        print(f"{t:<25} -> {mosca.chat(t)}")
