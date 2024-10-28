from numba.cpython.numbers import bool_negate_impl
from sympy import false

from bowling_error import BowlingError
from frame import Frame
import math


class BowlingGame:

    def __init__(self):
        self.frames = []
        self.first_bonus_throw = 0
        self.second_bonus_throw = 0
    
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
                num_of_affected_strikes = math.ceil(bonus_strike / 2)
                score = score + frame.get_first_throw() * num_of_affected_strikes
                bonus_strike = bonus_strike - (1 * num_of_affected_strikes)
                if frame.get_second_throw():
                    num_of_affected_strikes = math.ceil(bonus_strike / 2)
                    score = score + frame.get_second_throw() * num_of_affected_strikes
                    bonus_strike = bonus_strike - (1 * num_of_affected_strikes)
            if bonus_throw:
                score = score + frame.get_first_throw()
            if frame.get_first_throw() == 10:
                bonus_strike = bonus_strike + 2
            bonus_throw = frame.is_spare()
            score = score + frame.score()
        score = score + self.first_bonus_throw + self.second_bonus_throw
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        if self.first_bonus_throw:
            raise BowlingError
        self.first_bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        if self.second_bonus_throw or not self.first_bonus_throw:
            raise BowlingError
        self.second_bonus_throw = bonus_throw
