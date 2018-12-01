#!/usr/bin/env python3

import numpy
import cozmo
import time
import asyncio
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import color_finder
import functools
import sys


async def test_cozmo_program(robot: cozmo.robot.Robot):
    playerOne = None
    playerTwo = None
    searching = True

# Determine number of players between 1 and 2

    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart

    '''
    cube1 = robot.world.wait_for_observed_light_cube(timeout=60)
    cube2 = robot.world.wait_for_observed_light_cube(timeout=60)
'''


    cube1.set_lights(cozmo.lights.red_light)


    cube1.set_lights(cozmo.lights.red_light)
    cube2.set_lights(cozmo.lights.green_light)

    while(searching):

        try:
            if ((await cube1.wait_for_tap(timeout=3)) and (await cube2.wait_for_tap(timeout=3))):
                playerOne = True
                playerTwo = True

        except asyncio.TimeoutError:
            playerOne = True
            playerTwo = False
            searching = False

        if playerOne and playerTwo:
            searching = False

    print(playerOne)
    print(playerTwo)



# Cozmo to introduce himself and ask for children's names (Stretch Goal)

# Cozmo speaks a color
    await robot.say_text("Purple").wait_for_completed()

# Cozmo waits and looks for 1 of 2 colors
    colorFinder1 = color_finder.ColorFinder(robot, 'red')


    await colorFinder1.run()
    print("returning to main")
    await robot.say_text("I found red").wait_for_completed()



    colorFinder2 = color_finder.ColorFinder(robot, 'yellow')
    await colorFinder2.run()

    print("returning to main")
    await robot.say_text("I found yellow").wait_for_completed()


# modify color_finder to search for specific colors

# If Cozmo cannot find a color in a specified period of time, begin speaking clues


# When correct color detected, deliver a cube to the child with correct color
# When both colors are detected, Cozmo congratulates the players, speaks their names and preforms a dance

cozmo.run_program(test_cozmo_program, use_viewer = True)