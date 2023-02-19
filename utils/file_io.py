import json
from utils.gen_gcp import draw, gen
from csp.gcp_csp import gcp_csp

def gen_gcp(num_points = 10, file_path = 'gcp.json'):
    print("Generating a planar graph with {} points...".format(num_points))
    (x, lines) = gen(num_points=num_points)
    draw(x, lines)

    print("Writing to '{}'...".format(file_path))
    with open(file_path, 'w') as f:
        f.write(json.dumps({
            'num_points': len(x),
            'points': { p.id: (p.x, p.y) for p in x },
            'edges': [ (line.p1.id, line.p2.id) for line in lines ]
        }, indent=2))
    print("""Done! You can now import the results into a Python script with the code:

import json

with open('{}', r) as f:
    data = json.load(f)
""".format(file_path))

def load_gcp(file_path = 'gcp.json'):
    with open('gcp.json', 'r') as f:
        data = json.load(f)
        return gcp_csp(data)


