# Modules
import pygame as pg
import random as rd

# Screen
WIDTH, HEIGHT = 400, 400

# Cube class
class Cube:
    def __init__(self, x: float, y: float):
        """
        Cube class

        x: cube start x position
        y: cube start y position
        """
        self.id = 0
        self.status = True
        self.WIDTH, self.HEIGHT = 30, 30
        self.position = {'x': x, 'y': y}
        self.route = {'x': [], 'y': []}

        colors = ['blue', 'red', 'white', 'purple', 'yellow', 'orange', 'green', 'brown', 'gray']
        self.color = colors[rd.randint(0, len(colors) - 1)]
    
    
    def show(self, surface: 'pg.display') -> None:
        """
        Shows cube in the screen

        surface: pygame screen the cube will be shown
        """
        object = pg.Rect((self.position['x'], self.position['y']), (self.WIDTH, self.HEIGHT))
        pg.draw.rect(surface, self.color, object)


    def move(self, x: int, y: int) -> None:
        """
        Moves the cube x pixels and y pixels
        
        x: pixels to move in x
        y: pixels to move in y
        """
        if self.status == True:
            self.position['x'] += x
            self.position['y'] += y


    def random_move(self, velocity: float) -> None:
        """
        Makes cube move randomly 

        velocity: movement's velocity
        """
        if self.status == True:
            x = rd.randint(-velocity, velocity)
            y = rd.randint(-velocity, velocity)
            self.position['x'] += x
            self.position['y'] += y
            self.route['x'].append(x)
            self.route['y'].append(y)
            if self.position['x'] <= 0 or self.position['x'] >= WIDTH - self.WIDTH or self.position['y'] <= 0 or self.position['y'] >= HEIGHT - self.HEIGHT:
                self.status = False


    def touch_goal(self, goal: 'Goal') -> bool:
        """
        Verify if cube touchs goal

        goal: Goal object
        return: True || False
        """
        cube_object = pg.Rect((self.position['x'], self.position['y']), (self.WIDTH, self.HEIGHT))
        goal_object = pg.Rect((goal.position['x'], goal.position['y']), (goal.WIDTH, goal.HEIGHT))
        if cube_object.colliderect(goal_object) and self.status == True:
            return True
        return False
    

    def touch_wall(self, wall: 'Wall') -> bool:
        """
        Verify if wall touchs goal

        wall: Wall object
        return: True || False
        """
        cube_object = pg.Rect((self.position['x'], self.position['y']), (self.WIDTH, self.HEIGHT))
        wall_object = pg.draw.line(wall.surface, wall.color, wall.start, wall.end, wall.thickness)
        if cube_object.colliderect(wall_object) and self.status == True:
            return True
        return False
        


# Goal class
class Goal:
    def __init__(self, x: int, y: int) -> None:
        """
        Goal class

        x: goal start x position
        y: goal start y position
        """
        self.WIDTH, self.HEIGHT = 5, 5
        self.position = {'x': x, 'y': y}
        self.color = 'red'
    

    def show(self, surface: 'pg.display') -> None:
        """
        Shows goal in the screen

        surface: pygame screen the goal will be shown
        """
        object = pg.Rect((self.position['x'], self.position['y']), (self.WIDTH, self.HEIGHT))
        pg.draw.rect(surface, self.color, object)


# Wall clas
class Wall:
    def __init__(self, surface, start: tuple, end: tuple, thickness: int):
        """
        Wall class

        start: coordinate of the beggining point
        end: coordinate of the ending point
        thickness: wall thickness in pixels
        """
        self.surface = surface
        self.start = start
        self.end = end
        self.thickness = thickness
        self.color = 'white'