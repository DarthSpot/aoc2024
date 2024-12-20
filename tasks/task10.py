from collections import defaultdict

from tasks.abstracttask import AbstractTask


class Task10(AbstractTask):
    def __init__(self):
        super().__init__(10)

    def get_neighbors(self, map, x: int, y: int) -> list:
        results = []
        for nx, ny in [(0,1), (0,-1), (1,0), (-1,0)]:
            px, py = x + nx, y + ny
            if (px,py) in map:
                results.append((px, py))
        return results

    def find_trails(self):
        input = self.read_file_lines()
        zeros = defaultdict(list)
        tops = []
        trail_map = {}
        for idy, line in enumerate(input):
            for idx, c in enumerate(line):
                h = int(c)
                trail_map[(idx, idy)] = h
                if h == 9:
                    tops.append((idx, idy))
        for top in tops:
            trails = [top]
            while len(trails) > 0:
                trail, *trails = trails
                x, y = trail
                h = trail_map[(x, y)]
                if h > 0:
                    trails = trails + [(nx, ny) for nx, ny in self.get_neighbors(trail_map, x, y) if
                                       trail_map[(nx, ny)] == h - 1]
                else:
                    zeros[(x, y)].append(top)
        return zeros

    def simple_task(self):
        return sum([len(set(x)) for k,x in self.find_trails().items()])


    
    def extended_task(self):
        return sum([len(x) for k, x in self.find_trails().items()])


Task10()
