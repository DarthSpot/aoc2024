from collections import defaultdict

from tasks.abstracttask import AbstractTask


class Task8(AbstractTask):
    def __init__(self):
        super().__init__(8)
    
    def simple_task(self):
        input = self.read_file_lines()
        antenna_map = defaultdict(list)
        height = len(input)
        width = len(input[0])
        for idy, line in enumerate(input):
            for idx, c in enumerate(line):
                if c != '.':
                    antenna_map[c].append((idx, idy))
        results = []
        for key, positions in antenna_map.items():
            while len(positions) > 1:
                (hx, hy), *tail = positions
                for tx, ty in tail:
                    dx, dy = tx - hx, ty - hx
                    for x,y in [(x,y) for x,y in [(tx + dx, ty + dy), (hx - dx, hy - dy)] if 0 <= x < width and 0 <= y < height]:
                        results.append((x,y))
                positions = tail

        return len(set(results))

    def extended_task(self):
        input = self.read_file_lines()
        antenna_map = defaultdict(list)
        height = len(input)
        width = len(input[0])
        for idy, line in enumerate(input):
            for idx, c in enumerate(line):
                if c != '.':
                    antenna_map[c].append((idx, idy))
        results = []
        for key, positions in antenna_map.items():
            while len(positions) > 1:
                (hx, hy), *tail = positions
                for tx, ty in tail:
                    dx, dy = tx - hx, ty - hx
                    harmonic = 0
                    hdx, hdy = hx, hy
                    tdx, tdy = tx, ty
                    all_in_map = True
                    while all_in_map:
                        h_in_map = 0 <= hdx < width and 0 <= hdy < height
                        t_in_map = 0 <= tdx < width and 0 <= tdy < height
                        if h_in_map:
                            hdx, hdy = hdx - dx * harmonic, hdy - dy * harmonic
                            results.append((hdx, hdy))
                        if t_in_map:
                            tdx, tdy = tdx + dx * harmonic, tdy + dy * harmonic
                            results.append((tdx, tdy))
                        all_in_map = h_in_map or t_in_map
                        harmonic += 1
                positions = tail

        return len(set(results))


Task8()
