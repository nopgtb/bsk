from numba.cpython.numbers import bool_negate_impl
from sympy import false

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) >= 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i < 0 or i >= len(self.frames):
            raise BowlingError
        return self.frames[i]

    def calculate_score(self) -> int:
        score = 0
        bonus_throw = False
        bonus_strike = 0
        for frame in self.frames:
            if bonus_strike > 0:
                score = score + frame.score()
                bonus_strike = bonus_strike - 1
            if bonus_throw:
                score = score + frame.get_first_throw()
            if frame.get_first_throw() == 10:
                bonus_strike = 1
            bonus_throw = frame.score() == 10 and not frame.get_first_throw() == 10
            score = score + frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
