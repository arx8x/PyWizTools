from dataclasses import dataclass
from enum import Enum


class PatternState(Enum):
    TURN_OFF = 0
    DO_NOTHING = 1


@dataclass
class PatternEntry:
    color: tuple[int, int, int]
    duration: float
    brightness: int 
    after: PatternState = PatternState.TURN_OFF

    @property
    def int8_brightness(self):
        brightness = min(100, self.brightness)
        return int((brightness / 100) * 255)

@dataclass
class Pattern:
    entries: list[PatternEntry]
    delimit_seconds: float = 0
    repeat_count: int = 1
    after: PatternState = PatternState.TURN_OFF


