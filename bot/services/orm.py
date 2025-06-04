from typing import Dict
from pydantic import BaseModel

class OrmData(BaseModel):
    weight: float
    reps: int


def brzycki(data: OrmData) -> float:
    return data.weight * (36 / (37 - data.reps))


def epley(data: OrmData) -> float:
    return data.weight * (1 + data.reps / 30)


def lombardi(data: OrmData) -> float:
    return data.weight * (data.reps ** 0.10)


def calculate_all(data: OrmData) -> Dict[str, int]:
    return {
        "brzycki": round(brzycki(data)),
        "epley": round(epley(data)),
        "lombardi": round(lombardi(data)),
    }
