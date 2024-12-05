import re

from tasks.abstracttask import AbstractTask


class Task4(AbstractTask):
    def __init__(self):
        super().__init__(4)
        self.input = None

    def get_char_on_post(self, x, y):
        if x < 0 or x >= len(self.input[0]) or y < 0 or y >= len(self.input):
            return '.'

        return self.input[y][x]

    def simple_task(self):
        self.input = self.read_file_lines()
        starts = []
        for h, str in enumerate(self.input):
            for w, c in enumerate(str):
                if c == 'X':
                   starts.append((w,h))
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        result = 0
        for x,y in starts:
            for dirx, diry in dirs:
                cx, cy = x, y
                res = []
                for i in range(3):
                    cx,cy = cx + dirx, cy + diry
                    res.append(self.get_char_on_post(cx, cy))
                if ''.join(res) == 'MAS':
                    result += 1
        return result
    
    def extended_task(self):
        self.input = self.read_file_lines()
        starts = []
        for h, str in enumerate(self.input):
            for w, c in enumerate(str):
                if c == 'A':
                    starts.append((w, h))
        cross_pairs = [((1,1), (-1,-1)), ((1,-1), (-1,1))]
        result = 0
        for x, y in starts:
            res = []
            for pair in cross_pairs:
                subres = []
                for dir_x, dir_y in pair:
                    cx, cy = x + dir_x, y + dir_y
                    subres.append(self.get_char_on_post(cx, cy))
                res.append(''.join(sorted(subres)))
            if res.count('MS') == 2:
                result += 1
        return result


Task4()
