"""
Simulator of an  simple reactive agent.
"""

__author__ = 'Ernesto Costa'
__date__ = 'February 2014'

from pyprocessing import *
import random

CELLSIZE = 10

# What exist 

class Entity(object):
    def __init__(self,pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def get_pos_x(self):
        return self.pos_x  
    
    def get_pos_y(self):
        return self.pos_y
    
    def get_type(self):
        return self.type_e
    
        
    
    
class Agent(Entity):
    
    def __init__(self,pos_x, pos_y,sensors=None, color=color(0,255,0),rule_set=None):
        Entity.__init__(self,pos_x, pos_y,color)
        self.sensors = sensors
        self.rule_set = rule_set
        self.type_e = 1  
    
    def go(self, world):
        """ Implements the cycle perceptions - actions."""
        stop = False
        while not stop:
            perceptions = get_perceptions(world)
            action = find_action(perceptions)
            if not raction:
                stop = True
            else:
                do_action(action,world)
            
    def find_action(self,perceptions):
        pass
            
    def get_perceptions(self,world):
        x = self.pos_x
        y = self.pos_y
        return [world.get_world()[y+sensor[1]][x+sensor[0]].get_type() for sensor in  [(0,-1), (1,0), (0,1),(-1,0)]]
            
    def do_action(self,action,world):
        pass
   
    def display_agent(self,canvas):
        pos_x = self.get_pos_x() * canvas.get_cell_size()
        pos_y = self.get_pos_y() * canvas.get_cell_size()
        fill(self.color)
        cell_size = canvas.get_cell_size()
        ellipse(pos_x + cell_size//2, pos_y + cell_size//2, cell_size,cell_size)
   
 
class Obstacle(Entity):
    
    def __init__(self,pos_x, pos_y, color= color(0,0,0)):
        Entity.__init__(self,pos_x, pos_y,color)
        self.type_e = 2
       
    def display_obstacle(self,canvas):
        pos_x = self.get_pos_x() * canvas.get_cell_size()
        pos_y = self.get_pos_y() * canvas.get_cell_size()
        fill(self.color)
        rect(pos_x, pos_y, canvas.get_cell_size(),canvas.get_cell_size())
    
        
class Base(Entity):
    
    def __init__(self, pos_x, pos_y, color=color(128,128,128)):
        Entity.__init__(self,pos_x,pos_y,color)
        self.type_e = 0
        
    def display_base(self,canvas):
        """ Same as display_obstacle."""
        pos_x = self.get_pos_x() * canvas.get_cell_size()
        pos_y = self.get_pos_y() * canvas.get_cell_size()
        fill(self.color)
        rect(pos_x, pos_y, canvas.get_cell_size(),canvas.get_cell_size())    
           
    
# the world

class World:
    
    def __init__(self, width,heigth, entities= None, type_w='closed',value=0,):
        self.width = width
        self.heigth = heigth
        self.entities = entities
        self.type_w = type_w
        self.value =  value
        self.create_world()
        
        if entities:
            self.add_entities(entities)
        
    def create_world(self):
        self.world = [[Base(j,i) for j in  range(self.width) ]for i in range(self.heigth)]
        if self.type_w == 'closed':
            for col in range(self.width):
                """ Horizontal wall."""
                self.world[0][col] = Obstacle(col,0)
                self.world[self.heigth-1][col] = Obstacle(col,self.heigth-1)
            for line in range(self.heigth):
                """ Vertical wall."""
                self.world[line][0] = Obstacle(0,line)
                self.world[line][self.width-1] = Obstacle(self.width-1,line)               
                
        elif self.type_w == 'open':
            for col in range(self.width):
                self.world[0][col] = Base(col,0)
                self.world[self.heigth-1][col] = Base(col,self.heigth-1)
            for line in range(self.heigth):
                self.world[line][0] = Base(0,line)
                self.world[line][self.width-1] = Base(self.width-1,line)
        else:
            pass
        
    def get_width(self):
        return self.width
    
    def get_heigth(self):
        return self.heigth
    
    def get_world(self):
        return self.world
    
    def get_type(self):
        return self.type_w
            

    def get_entity(self, x,y):
        """For now just retrieves the type."""
        return self.world[y][x]
    
    def add_entity(self,entity):
        """For now just stores thetype."""
        self.world[entity.get_pos_y()][entity.get_pos_x()] = entity
    
    def add_entities(self,entities):
        for entity in entities:
            self.add_entity(entity)
        
        
    def display_world(self, canvas):
        for col in range(self.width):
            for line in range(self.heigth):
                entity = self.world[line][col]
                if entity.get_type() == 2:
                    entity.display_obstacle(canvas)
                elif entity.get_type() == 1:
                    entity.display_agent(canvas)
                else:
                    pass
    
    
class Canvas:
    """To see a world."""
    
    def __init__(self, width,height,color=color(128,128,128),cell_size=CELLSIZE):
        
        self.width = width
        self.height = height
        self.color = color
        self.cell_size = cell_size

        size(self.width,self.height)
        background(self.color)
        
    def set_color(self, color):
        self.color = color
        background(self.color)
              
    def get_color(self):
        return self.color
    
    def get_width(self):
        return self.width
    
    def set_width(self, width):
        self.width = width
        size(self.width, self.heigth)
        
    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height
        size(self.width, self.height)
        
    def get_cell_size(self):
        return self.cell_size
        
         
    
      
def setup():
    WORLD_WIDTH = 40
    WORLD_HEIGTH = 20
    
    
    entities = []
    for i in range(5,15):
        entities.append(Obstacle(i,i))
        
    agent_1 = Agent(8,12)
    agent_2 = Agent(9,12)
    
    obst_1= Obstacle(8,11)
        
    world = World(WORLD_WIDTH,WORLD_HEIGTH, entities)
    
    world.add_entities([agent_1,agent_2,obst_1])
    
    canvas = Canvas(world.get_width()*CELLSIZE, world.get_heigth()*CELLSIZE)
    
    print(agent_1.get_perceptions(world))
    
    world.display_world(canvas)
    
    
    """
    obst_1 = Obstacle(random.randint(1,world.get_width()-2),random.randint(1,world.get_heigth()-2))  
    obst_2 = Obstacle(random.randint(1,world.get_width()-2),random.randint(1,world.get_heigth()-2))
    obst_3 = Obstacle(random.randint(1,world.get_width()-2),random.randint(1,world.get_heigth()-2))
    agent_1 = Agent(random.randint(1,world.get_width()-2),random.randint(1,world.get_heigth()-2))
    world.add_entity(obst_1)
    world.add_entity(obst_2)
    world.add_entity(obst_3)
    world.add_entity(agent_1)
    obst_4 = Obstacle(WORLD_WIDTH//2, WORLD_HEIGTH//2)
    agent_2 = Agent(WORLD_WIDTH//2, WORLD_HEIGTH//2)
    world.add_entity(obst_4)
    world.add_entity(agent_2) 
    """
    
  
    
    #print(world.get_world())
    """
    result = world.get_world()
    for line in result:
        print(line)
    
    
    for i in range(size_w[1]):
        obst = Obstacle(0,i)
        #obst.display_obstacle(canvas)
        world.set_entity(obst)

    
 
    agent = Agent(1,0)
    world.set_entity(agent)
    world.print_world()    
    """
    
    


def draw():
    pass

def fire_rule(pattern, rule):
    pass

    
if __name__ == '__main__':
    run()
        
        