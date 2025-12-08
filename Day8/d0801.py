from itertools import combinations
from math import prod

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def euclidean_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
def main(input_lines):
    points = [Point(*map(int, line.split(','))) for line in input_lines]
    pair_distances = [(a.euclidean_distance(b), {a,b}) for a, b in combinations(points, 2)]
    pds = sorted(pair_distances, key=lambda x: x[0])

    if len(input_lines) <= 20:
        # Test input requires only top 10 closest pairs for some reason
        pds = pds[:10]
    else:
        # Limit to top 1000 closest pairs for the real input
        pds = pds[:1000]

    clusters = []
    for _, pair in pds:
        found_clusters = [c for c in clusters if not c.isdisjoint(pair)]
        if not found_clusters:
            clusters.append(set(pair))
        elif len(found_clusters) == 1:
            found_clusters[0].update(pair)
        else:
            merged_cluster = set.union(*found_clusters, pair)
            clusters = [c for c in clusters if c.isdisjoint(pair)]
            clusters.append(merged_cluster)
    a = sorted([len(c) for c in clusters])
    return prod(a[-3:])

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
