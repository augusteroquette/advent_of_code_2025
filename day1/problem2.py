import sys

result = sys.argv[1]

def parse_input(text):
    with open(text, "r") as f:
        content = f.read()
    lines = content.strip().splitlines()

    cpt = 50
    rslt = 0

    for line in lines:
        rotation = int(line[1:])
        if line[0] == "R":
            rslt+= (rotation + cpt)//100
            cpt = (cpt + rotation)%100
        elif line[0] == "L":
            if cpt == 0:
                # Si on part de 0, on compte un passage tous les 100 clics
                rslt += rotation // 100
            elif rotation >= cpt:
                # Si on part d'ailleurs, on compte le 1er passage, puis tous les 100 clics
                rslt += 1 + (rotation - cpt) // 100
                
            cpt = (cpt - rotation) % 100

    return rslt
            





print(parse_input(result))