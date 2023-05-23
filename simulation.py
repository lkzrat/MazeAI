# Modules
from structures import Cube, Goal, Wall
import pygame as pg
import random as rd
import sys

def main():
    while True:
        if simulate() == True:
            break 

def simulate():
    # Pygame setups
    pg.init()

    # Screen
    WIDTH, HEIGHT = 400, 400
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Simulation')

    # Clock
    clock = pg.time.Clock()

    # Cubes setups
    START = {'x': 20, 'y': HEIGHT/2}
    VELOCITY = 10
    N = 500
    cubes = create_population(START, N)
    route = None
    id = None
    goal_cube = None
    i = 0

    # Goal setups
    GOAL_POSITION = {'x': WIDTH/1.5, 'y': HEIGHT/2}
    goal = Goal(GOAL_POSITION['x'], GOAL_POSITION['y'])

    # Maze
    walls = [
        Wall(screen, (3, 20), (WIDTH/5, 20), 5),
        Wall(screen, (3, HEIGHT - 20), (WIDTH/5, HEIGHT - 20), 5),

        Wall(screen, (WIDTH/5, 20), (WIDTH/5, HEIGHT/3), 5),
        Wall(screen, (WIDTH/5, HEIGHT - 20), (WIDTH/5, HEIGHT/1.5), 5),

        Wall(screen, (WIDTH/5, HEIGHT/3), (WIDTH/1.4, HEIGHT/3), 5),
        Wall(screen, (WIDTH/5, HEIGHT/1.5), (WIDTH/1.4, HEIGHT/1.5), 5)
    ]

    # Simulation
    while True:
        # Events
        for event in pg.event.get():

            # Quit
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit('\033[1;31mSimulation Closed\033[m')  # Terminal

            # Keyboard
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and i == 0:
                    if route != None:

                        # Discarding other cubes
                        for cube in cubes:
                            cubes.remove(cube)

                        # Goal_cube creation
                        goal_cube = Cube(START['x'], START['y'])    
                        goal_cube.id = id
                    
                        print(f"\n\033[1mRoute:\033[m\n\n\033[1mx\033[m:{route['x']}\n\n\033[1my\033[m:{route['y']}")  # Terminal
                
                if event.key == pg.K_DOWN:
                    sys.exit('\033[1;31mSimulation Closed\033[m')  # Terminal

        # Background
        screen.fill('black')

        # Goal
        goal.show(screen)

        # Cubes
        for cube in cubes:

            # Population
            if goal_cube == None:
                cube.show(screen)  
             
            cube.random_move(VELOCITY)

            # Goal colision
            if cube.touch_goal(goal) and route == None:

                # Goal_cube data
                route = cube.route
                id = cube.id

                # Stopping all cubes
                for cube in cubes:
                    kill(cube)

            # Wall colision
            for wall in walls:
                if cube.touch_wall(wall):
                    kill(cube)
        
        # Goal_cube
        if goal_cube != None and goal_cube.status == True:
            goal_cube.show(screen)

            # Following route
            if goal_cube.touch_goal(goal) == False:
                goal_cube.move(route['x'][i], route['y'][i])
                i += 1
            else:
                i = 0

        # Simulating again
        count = 0
        for cube in cubes:
            if cube.status == False:
                count += 1
        if count == len(cubes) and route == None:
            pg.quit()
            return False

        pg.display.update()
        clock.tick(60)        



def create_population(start: dict, n: int) -> list:
    """
    Creates a cube population of n cubes

    start: dict object with start position 'x' and 'y'
    n: int value of population length
    return: list object of Cube objects
    """
    tmp = []
    for i in range(n):
        tmp.append(Cube(start['x'], start['y']))
        tmp[i].id = i
    return tmp


def kill(cube: 'Cube') -> None:
    """
    Sets cube.statut to False

    cube: Cube object
    """
    cube.status = False


if __name__ == '__main__':
    main()