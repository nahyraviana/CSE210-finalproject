from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        stat1 = cast.get_first_actor(STATS_GROUP1)
        stat2 = cast.get_first_actor(STATS_GROUP2)
        self._draw_label(cast, SCORE_GROUP[0], SCORE_FORMAT[0], stat1.get_score())
        self._draw_label(cast, SCORE_GROUP[1], SCORE_FORMAT[1], stat2.get_score())

    def _draw_label(self, cast, group, format_str, data):

        label1= cast.get_first_actor(group)
        text1 = label1.get_text()
        text1.set_value(format_str.format(data))
        label2= cast.get_first_actor(group)
        text2 = label2.get_text()
        text2.set_value(format_str.format(data))

        position1 = label1.get_position()
        position2 = label2.get_position()

        self._video_service.draw_text(text1, position1)
        self._video_service.draw_text(text2, position2)

