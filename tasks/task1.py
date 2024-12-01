from tasks.abstracttask import AbstractTask


class Task1(AbstractTask):
    def __init__(self):
        super().__init__(1)
    
    def simple_task(self):
        l1, l2 = list(zip(*[list(map(int, x.split('   '))) for x in self.read_file_lines()]))
        return sum([abs(x-y) for x,y in zip(sorted(l1), sorted(l2))])

    
    def extended_task(self):
        l1, l2 = list(zip(*[list(map(int, x.split('   '))) for x in self.read_file_lines()]))
        return sum([x * l2.count(x) for x in l1])


Task1()
