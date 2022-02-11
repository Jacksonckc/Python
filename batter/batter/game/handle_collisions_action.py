import random
import sys
from game import constants
from game.action import Action
from game.point import Point

# change the states of the actors when collisions happen
class HandleCollisionsAction(Action):
    

    # ball collides with the bricks, ball collides with the paddles, 
    # this function changes the states of the ball and the bricks according to 
    # the collisions and the current states of the actors.
    def execute(self, cast):
        
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball.get_velocity()
        bricks = cast["brick"]

        # make sure the ball will bounce with hits the walls or the boundaries.
        if ball.get_position_x() == 76:
            ball.set_velocity_x(ball, -1)
        elif ball.get_position_x() == 4:
            ball.set_velocity_x(ball, 1)
        if ball.get_position_y() == 1:
            ball.set_velocity_y(ball, 1)

        # when the paddle fails to catch the ball, the game is over.
        elif ball.get_position_y() == 19:
            sys.exit()            

        # Get the whole paddle.
        paddle_head_x = paddle.get_position_x()
        paddle_body_x = []
        for i in range(len(paddle.get_text())):
            paddle_body_x.append(paddle_head_x + i)

        # Loop through the whole paddle and compare each with the current position of the ball.
        for one_segment in paddle_body_x:
            if ball.get_position_y() == paddle.get_position_y() -1:
                if ball.get_position_x() == one_segment:
                    ball.set_velocity_y(ball, -1)

        # Loop through all the bricks and compare their position with the ball.
        for brick in bricks:
      
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                if ball.get_velocity_y() == -1:
                    ball.set_velocity_y(ball, 1)
                elif ball.get_velocity_y() == 1:
                    ball.set_velocity_y(ball, -1)
            