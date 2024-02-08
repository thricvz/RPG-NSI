import math
from p5 import *
class Map:
    def __init__(self):
        self.map_data = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.map_width = len(self.map_data)
        self.map_height = len(self.map_data[0])
        self.cell_size = 10

    def build_screen(self):
        #CreateCanvas(self.cell_size*self.map_width,self.cell_size*self.map_height)
        pass
    def display(self):
        for i in range(self.map_width):
            for j in range(self.map_height):
                rect(i,j,self.cell_size,self.cell_size)
        pass
    
    def get_point_coordinate_on_map(self,coord,axis_size):
        coord_common_wall_block= []
        ##if the point is on two squares
        if coord == 0:
            coord_common_wall_block.append(0)
        elif coord-(int(coord))==0 and coord != 0 and coord!= axis_size:
            coord_common_wall_block.append(coord)
            coord_common_wall_block.append(coord-1)
        elif coord == axis_size:
            coord_common_wall_block.append(coord-1)
        else:
            coord_common_wall_block.append(int(coord))
        
        return coord_common_wall_block
    
    def is_wall(self, point):
        x, y = point
        x_square = self.get_point_coordinate_on_map(x,self.map_width)
        y_square = self.get_point_coordinate_on_map(y,self.map_height)
        cell_content =[]
        for i in x_square:
            for j in y_square:
                cell_content.append(self.map_data[j][i])
        return 1 in cell_content

    
    def distance(self,player,angle):
        inter_point = player.copy()
        direction_vector =  [math.cos(angle),math.sin(angle)]
        slope = direction_vector[1]/direction_vector[0]
        #first iteration 
        while not self.is_wall(inter_point):
            if 0 in direction_vector:
                inter_point[direction_vector.index(0)]+=1
            elif abs(slope) <= 1:
                inter_point[0]+= 1
                inter_point[1]+= slope
            elif slope==1:
                inter_point[0]+= 1
                inter_point[1]+= 1
            else:
                inter_point[0]+= 1/slope
                inter_point[1]+= 1

        return inter_point,math.sqrt(pow(player[0]-inter_point[0],2)+pow(player[1]-inter_point[1],2))

    def draw_rays(self,player):
        ray_distance = []
        for angle in range(0,360,5):
            dest_point,distance = self.distance(player,angle)
            #draw line from player to dest point 
            ray_distance.append(distance)

        
