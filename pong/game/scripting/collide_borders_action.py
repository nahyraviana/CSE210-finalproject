from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
        racket1 = cast.get_first_actor(RACKET_GROUP[0])
        racket2 = cast.get_first_actor(RACKET_GROUP[1])
        stats1 = cast.get_first_actor(STATS_GROUP1)
        stats2 = cast.get_first_actor(STATS_GROUP2)
        score1 = stats1.get_score()
        score2 =stats2.get_score()

        if y <= FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        if x >= (FIELD_RIGHT - BALL_WIDTH):
            points1 = racket1.get_points()
            stats1.add_points(points1)

            if score2 ==4 or score1 ==4:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN)

        if y >= (FIELD_BOTTOM - BALL_HEIGHT):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
        if x <= FIELD_LEFT:
            points2 = racket2.get_points()
            stats2.add_points(points2)


            if score1 == 4 or score2 == 4:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
            else:
                callback.on_next(TRY_AGAIN)