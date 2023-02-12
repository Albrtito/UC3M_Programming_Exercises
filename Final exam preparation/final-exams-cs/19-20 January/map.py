import random
class Map:
    def __init__(self, neighbourhood: int, matrix: list):
        self.neighbourhood = neighbourhood
        self.matrix = matrix

        # Both need property and setter


    def create_map_matrix(self,warehouse_name: str, rows : int, columns : int, house_number: int):
        # Create a blank matrix with the right magnitude
        for x in range(rows):
            self.matrix.append([])
            for y in range(columns):
                self.matrix[x].append(0)

        # We first create a random position for the warehouse:
        self.matrix[[random.randint(1,rows)][random.randint(1, columns)]] = warehouse_name
        # Create random positions for the houses: If a position is already occupied look for another position
        for i in range(house_number):
            random_x = random.randint(1, rows)
            random_y = random.randint(1, columns)
            while self.matrix[[random_x][random_y]] != 0:
                self.matrix[[random_x][random_y]] = f"h{i}"
                random_x = random.randint(1, rows)
                random_y = random.randint(1, columns)
        # fill the rest of the positions with streets
        for x in range(rows):
            for y in range(columns):
                if self.matrix[[x][y]] == 0:
                    self.matrix[[x][y]] = "s"


    def compute_distance(self,warehouse_id: str, address: str):
        ...