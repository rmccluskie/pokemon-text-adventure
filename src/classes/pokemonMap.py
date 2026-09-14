import random
from collections import deque
from enums.mapEnum import MapEnum

# Tile symbol -> probability weight, per map type
MAP_TILES = {
    MapEnum.Forest:   {'.': 0.6, 'T': 0.3, '~': 0.1},
    MapEnum.Cave:     {'.': 0.5, '#': 0.4, 'o': 0.1},
    MapEnum.Mountain: {'.': 0.4, '^': 0.4, '#': 0.2},
    MapEnum.Route:    {'.': 0.8, 'T': 0.1, '~': 0.1},
}

# Tile symbols that block movement, per map type
MAP_BLOCKING = {
    MapEnum.Forest:   {'~'},
    MapEnum.Cave:     {'#'},
    MapEnum.Mountain: {'#'},
    MapEnum.Route:    {'~'},
}

class PokemonMap:
    def __init__(self, map_type: MapEnum, width=10, height=10):
        self.map_type = map_type
        self.width = width
        self.height = height
        self.entrance = (0, 0)
        self.exit = (height - 1, width - 1)
        self.grid = self._generate_grid()
        self._ensure_path_exists()

    def _generate_grid(self):
        tiles = MAP_TILES[self.map_type]
        symbols = list(tiles.keys())
        weights = list(tiles.values())
        grid = [
            [random.choices(symbols, weights=weights)[0] for _ in range(self.width)]
            for _ in range(self.height)
        ]
        # Entrance and exit should always be walkable
        ex_r, ex_c = self.entrance
        xx_r, xx_c = self.exit
        grid[ex_r][ex_c] = '.'
        grid[xx_r][xx_c] = '.'
        return grid

    def _is_walkable(self, row, col):
        return self.grid[row][col] not in MAP_BLOCKING[self.map_type]

    def _has_path(self):
        """BFS from entrance to exit over walkable tiles."""
        visited = set()
        queue = deque([self.entrance])
        visited.add(self.entrance)

        while queue:
            row, col = queue.popleft()
            if (row, col) == self.exit:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < self.height and 0 <= nc < self.width
                        and (nr, nc) not in visited
                        and self._is_walkable(nr, nc)):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    def _carve_path(self):
        """Carve a guaranteed walkable path from entrance to exit.

        NOTE: this moves in straight row/col steps toward the exit, so when
        it triggers it can look like an obvious staircase cut through the
        map. A future improvement would be a "wiggle" (biased random walk
        that sometimes steps away from the goal before correcting) so the
        carved path blends in more naturally with the surrounding terrain.
        """
        row, col = self.entrance
        ex_row, ex_col = self.exit
        self.grid[row][col] = '.'

        while (row, col) != (ex_row, ex_col):
            moves = []
            if row != ex_row:
                moves.append('row')
            if col != ex_col:
                moves.append('col')
            move = random.choice(moves)
            if move == 'row':
                row += 1 if ex_row > row else -1
            else:
                col += 1 if ex_col > col else -1
            self.grid[row][col] = '.'

    def _ensure_path_exists(self):
        if not self._has_path():
            self._carve_path()

    def print_map(self):
        for row in self.grid:
            print(' '.join(row))
