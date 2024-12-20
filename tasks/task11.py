from collections import defaultdict

from tasks.abstracttask import AbstractTask


class Task11(AbstractTask):
    def __init__(self):
        super().__init__(11)

    def blink_at_stones(self, times):
        stones = defaultdict(int)
        for stone in [int(v) for v in self.read_file_string().split()]:
            stones[stone] += 1
        for i in range(times):
            n = defaultdict(int)
            for stone, count in stones.items():
                if stone == 0:
                    n[1] += count
                else:
                    s_stone = str(stone)
                    stone_len = len(s_stone)
                    if not stone_len % 2:
                        s1 = int(s_stone[0:stone_len // 2])
                        s2 = int(s_stone[stone_len // 2:])
                        n[s1] += count
                        n[s2] += count
                    else:
                        n[stone * 2024] += count
            stones = n
        return sum([v for k, v in stones.items()])

    def simple_task(self):
        return self.blink_at_stones(25)

    
    def extended_task(self):
        return self.blink_at_stones(75)


Task11()
