import sys

result = sys.argv[1]

def parse_input(text):
    with open(text, "r") as f:
        content = f.read()
    lines = content.strip().splitlines()

    cpt = 50
    rslt = 0

    for line in lines:
        if line[0] == "R":
            cpt = (cpt + int(line[1:]))%100
        if line[0] == "L":
            cpt = (cpt - int(line[1:]))%100
        if cpt == 0:
            rslt += 1

    return rslt
            





print(parse_input(result))