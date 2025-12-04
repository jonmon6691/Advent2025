class InfiniteList(list):
    def __init__(self, *args, default_value, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_value = default_value

    def __getitem__(self, idx):
        if idx < 0 or idx >= len(self):
            return self.default_value
        return super().__getitem__(idx)

def new_infinite_grid(grid, default_value):
    return InfiniteList([InfiniteList(row, default_value=default_value) for row in grid], default_value=InfiniteList(default_value=default_value))

def main(input_lines):
    answer = 0
    grid = [[0 if cell == '.' else 1 for cell in line] for line in input_lines]
    grid = new_infinite_grid(grid, default_value=0)

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == 0:
                continue
            rolls = 0
            rolls += grid[i - 1][j - 1]
            rolls += grid[i - 1][j - 0]
            rolls += grid[i - 1][j + 1]
            rolls += grid[i + 0][j - 1]
            rolls += grid[i + 0][j + 1]
            rolls += grid[i + 1][j - 1]
            rolls += grid[i + 1][j + 0]
            rolls += grid[i + 1][j + 1]
            if rolls < 4:
                answer += 1
    return answer

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
