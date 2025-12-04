def parse_coords(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    v = []
    
    for line in lines:
        if line.startswith('v'):
            v.append((int(line.split()[1]), int(line.split()[2]), int(line.split()[3])))

    return v

def parse_arcs(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    a = []
    
    for line in lines:
        if line.startswith('a'):
            parts = line.split()
            a.append((int(parts[1]), int(parts[2]), int(parts[3])))

    return a

