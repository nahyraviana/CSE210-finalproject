from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP[0])
        body1 = racket1.get_body()

        if racket1.is_debug():
            rectangle1 = body1.get_rectangle()
            self._video_service.draw_rectangle(rectangle1, PURPLE)

        animation1 = racket1.get_animation()
        image1 = animation1.next_image()
        position1 = body1.get_position()
        self._video_service.draw_image(image1, position1)

        racket2 = cast.get_first_actor(RACKET_GROUP[1])
        body2 = racket2.get_body()

        if racket2.is_debug():
            rectangle2 = body1.get_rectangle()
            self._video_service.draw_rectangle(rectangle2, PURPLE)

        animation2 = racket2.get_animation()
        image2 = animation2.next_image()
        position2 = body2.get_position()
        self._video_service.draw_image(image2, position2)