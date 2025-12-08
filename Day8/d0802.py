from itertools import combinations

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def euclidean_distance_squared(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

def main(input_lines):
    points = [Point(*map(int, line.split(','))) for line in input_lines]
    pair_distances = [(a.euclidean_distance_squared(b), {a,b}) for a, b in combinations(points, 2)]
    pair_distances.sort(key=lambda x: x[0])

    clusters = []
    for _, pair in pair_distances:
        found_clusters = [c for c in clusters if not c.isdisjoint(pair)]
        
        if not found_clusters:
            clusters.append(set(pair))
        elif len(found_clusters) == 1:
            found_clusters[0].update(pair)
        else:
            merged_cluster = set.union(*found_clusters, pair)
            clusters = [c for c in clusters if c.isdisjoint(pair)]
            clusters.append(merged_cluster)
        
        if len(clusters) == 1 and len(clusters[0]) == len(points):
            # All points are in one cluster, return product of the last pair's x coordinates
            return pair.pop().x * pair.pop().x

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
