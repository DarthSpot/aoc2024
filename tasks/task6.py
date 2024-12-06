from collections import defaultdict

from tasks.abstracttask import AbstractTask


class Task6(AbstractTask):
    def __init__(self):
        super().__init__(6)
        self.map = None

    def get_char_at_pos(self, x, y):
        return self.map.get((x,y), '')

    def turn_right(self, dx, dy):
        return -1 * dy, dx

    def simple_task(self):
        input = self.read_file_lines()
        self.map = defaultdict(str)
        cx, cy = 0, 0
        dx, dy = 0, -1
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '^':
                    cx, cy = x, y
                    self.map[(x, y)] = '.'
                else:
                    self.map[(x, y)] = c
        start = []


        while True:
            nx, ny = cx + dx, cy + dy
            look_ahead = self.get_char_at_pos(nx, ny)
            if look_ahead == '#':
                dx, dy = self.turn_right(dx, dy)
            elif look_ahead == '':
                break
            else:
                cx, cy = nx, ny
            start.append(((cx, cy), (dx, dy)))

        return len(set([(cx, cy) for cx, cy in [cp for cp, cd in start]]))


    
    def extended_task(self):
        input = self.read_file_lines()
        self.map = defaultdict(str)
        sx, sy = 0, 0
        dx, dy = 0, -1
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '^':
                    sx, sy = x, y
                    self.map[(x, y)] = '.'
                else:
                    self.map[(x, y)] = c
        cx, cy = sx, sy
        start = []

        while True:
            nx, ny = cx + dx, cy + dy
            look_ahead = self.get_char_at_pos(nx, ny)
            if look_ahead == '#':
                dx, dy = self.turn_right(dx, dy)
            elif look_ahead == '':
                break
            else:
                cx, cy = nx, ny
            start.append(((cx, cy), (dx, dy)))

        result = []
        progress = 0
        visited = set([(cx, cy) for cx, cy in [cp for cp, cd in start]])
        pmax = len(visited)
        for idx, (bx, by) in enumerate(list(visited)):
            if bx == sx and by == sy:
                continue
            cx, cy = sx, sy
            dx, dy = 0, -1
            loop = []
            while True:
                nx, ny = cx + dx, cy + dy
                look_ahead = '#' if nx == bx and ny == by else self.get_char_at_pos(nx, ny)
                if look_ahead == '#':
                    dx, dy = self.turn_right(dx, dy)
                elif look_ahead == '':
                    break
                else:
                    cx, cy = nx, ny
                if ((cx, cy), (dx, dy)) in loop:
                    result.append((bx, by))
                    break
                else:
                    loop.append(((cx, cy), (dx, dy)))
            print("{:3.2f}".format(progress*100/pmax))
            progress += 1


        return len(set(result))



Task6()
