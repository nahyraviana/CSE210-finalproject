from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP[0])

        if self._keyboard_service.is_key_down(UP[0]):
            racket1.swing_up()
        elif self._keyboard_service.is_key_down(DOWN[0]):
            racket1.swing_down()
        else:
            racket1.stop_moving()

        racket2 = cast.get_first_actor(RACKET_GROUP[1])

        if self._keyboard_service.is_key_down(UP[1]):
            racket2.swing_up()
        elif self._keyboard_service.is_key_down(DOWN[1]):
            racket2.swing_down()
        else:
            racket2.stop_moving()