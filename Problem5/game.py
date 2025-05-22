import os
from PIL import Image

def read_conf_field(filepath):
    """Read field configuration from a field state"""
    filepath = os.path.join(os.path.dirname(__file__), filepath) # full absolute path
    field = [] # field canvas
    
    with open(filepath, 'r') as f:
        for line in f:
            row = [int(cell) for cell in line.strip().split()] # convert values to generate rows of cells
            field.append(row)
    return field

# test
# field = read_conf_field("input_field.txt")
# for row in field:
#     print(row)

def read_conf_coordinates(filepath):
    """Read field configuration from a list of coordinates"""
    filepath = os.path.join(os.path.dirname(__file__), filepath)
    live_cells = [] # coordinates map
    
    with open(filepath, 'r') as f:
        for line in f:
            _x, _y = line.strip().split() # extract coordinates 
            x, y = int(_x), int(_y)
            live_cells.append((x, y))
    
    x_max = max(x for x, y in live_cells)
    y_max = max(y for x, y in live_cells)

    _width = x_max + 1
    _height = y_max + 1
    
    field = [ [ 0 for i in range(_width) ] for j in range(_height) ] # zeroed field
    for x, y in live_cells:
        field[y][x] = 1 # add newborn live cells 
    
    return field # complete field

# test
# field = read_conf_coordinates("input_coords.txt")
# for row in field:
#     print(row)

def count_live_neighbors(field, x, y):
    """Counts number of live neighbors around a cell"""
    height = len(field)
    width = len(field[0]) # get size
    count = 0             # live neighbors

    for dx in [-1, 0, 1]:           # check horizonal
        for dy in [-1, 0, 1]:       # check vertical
            if dx == 0 and dy == 0: # skip self
                continue
            nx, ny = x + dx, y + dy # neighbor coordinates
            if 0 < ny < height and 0 <= nx < width:
                if field[ny][nx] > 0: # neighbor is alive
                    count += 1
    return count
    
def next_generation(field):
    """Calculates the next generation for the entire field"""
    height = len(field)
    width = len(field[0])

    new_field =  [ [ 0 for i in range(width) ] for j in range(height) ]

    for y in range(height):
        for x in range(width):
            neighbors = count_live_neighbors(field, x, y) 
            current = field[y][x]                    # current cell state
            if current == 0 and neighbors == 3:      # dead cell with 3 neighbors gets birth
                new_field[y][x] = 1 
            elif current > 0 and neighbors in [2,3]: # live cell with 2 or 3 neighbors survives
                new_field[y][x] = current + 1 # lives
            else:                                    # other cells die or remain dead
                new_field[y][x] = 0 
    return new_field

# test
# field = read_conf_coordinates("input_coords.txt")
# print("Step 0:")
# for row in field:
#     print(row)
# for step in range(1, 4):
#     field = next_generation(field)
#     print(f"Step {step}:")
#     for row in field:
#         print(row)

def save_field_as_text(field, step):
    """Saves state of the field to a text file"""
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f"step_{step}.txt")
    
    with open(filename, "w") as f:
        for row in field:
            f.write(" ".join(str(cell) for cell in row) + "\n")

def get_color_from_age(base_color, age, max_age=10):
    """Returns color depending on age"""
    age_factor = max(0, 1 - (age - 1) / max_age) # make faded color
    
    base_colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }
    
    r, g, b = base_colors[base_color] # RGB values for the base color
    return (int(r * age_factor), int(g * age_factor), int(b * age_factor))

def save_field_as_image(field, step, base_color="red", scale=10):
    """Saves an image of the current state of the field"""
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)
    height = len(field)
    width = len(field[0])
    
    image = Image.new("RGB", (width, height)) # create RGB image
    pixels = image.load() # pixel access object
    
    for y in range(height):
        for x in range(width):
            age = field[y][x] # cell age defines color
            if age > 0:
                pixels[x, y] = get_color_from_age(base_color, age)
            else:
                pixels[x, y] = (0,0,0) # dead cells 
    
    if scale > 1:
        image = image.resize((width * scale, height * scale), resample=Image.NEAREST) # scaling
    
    image.save(os.path.join(out_dir, f"step_{step}.png")) # save RGB image

# main
if __name__ == "__main__":
    # field = read_conf_field("input_field.txt")
    field = read_conf_coordinates("input_coords.txt")

    for step in range(0, 100): # simulation for 100 generations cycles/pictures
        # print(f"Step {step}:")
        # for row in field:
            # print(row)
        
        save_field_as_text(field, step)
        
        # save_field_as_image(field, step, base_color="red")
        save_field_as_image(field, step, base_color="red", scale=10)

        field = next_generation(field)

