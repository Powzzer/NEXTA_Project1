import math

COORDINATES = {
    "Warehouse": (26.43, 50.11),
    "A": (26.39, 50.19),
    "B": (26.45, 50.05),
    "C": (26.30, 50.21),
    "D": (26.51, 50.04),
    "H": (26.40, 50.08)
}

def optimize_route(stops):
    unvisited = {s: COORDINATES[s] for s in set(stops) if s in COORDINATES}
    route = ["Warehouse"]
    curr = COORDINATES["Warehouse"]
    
    while unvisited:
        closest = min(unvisited, key=lambda s: math.dist(curr, unvisited[s]))
        route.append(closest)
        curr = unvisited.pop(closest)
        
    route.append("Warehouse")
    return " -> ".join(route)

if __name__ == "__main__":
    sample_stops = ["B", "D", "H", "A", "C"]
    print(optimize_route(sample_stops))