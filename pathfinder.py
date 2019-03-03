import random
from PIL import ImageColor, Image, ImageDraw

class Map:
    """
    the class map Represents a map
    """

    def __init__(self, file, map_drawer, path_finder, ):
        """
        Parameters:
        - file -- elevation data file to be read in
        - map_drawer -- represents MapDrawer object
        - path_finder -- represents PathFinder object
        """
        self.file = elevation_small.txt
        self.map_drawer = map_drawer
        self.path_finder = path_finder
        self.y_coord = y_coord
        self.elevations = self.convert_to_list()
        
    def convert_to_list(self):
        """
        the self.elevation_small.txt will be turned into a list. 
        """
        elevations = []
        with open(self.elevation_small.txt) as file:
            for line in file:
                elevations.append([int(e) for e in line.split(" ")])
        return elevations

