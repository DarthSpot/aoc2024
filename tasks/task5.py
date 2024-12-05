from collections import defaultdict

from tasks.abstracttask import AbstractTask


class Task5(AbstractTask):
    def __init__(self):
        super().__init__(5)

    def find_middle(self, data: list):
        middle = int(float(len(data)-1)/2)
        return data[middle]

    def simple_task(self):
        correct = []
        ordering = defaultdict(list)
        tmpx, tmpy = [x.split('\n') for x in self.read_file_string().split('\n\n')]
        production = [x.split(',') for x in tmpy]
        for before, after in [x.split('|') for x in tmpx]:
            ordering[after].append(before)
        for update in production:
            if not self.is_faulty(ordering, update):
                correct.append(update)
        return sum([int(self.find_middle(x)) for x in correct])
    
    def extended_task(self):
        ordering = defaultdict(list)
        faulty = []
        tmpx, tmpy = [x.split('\n') for x in self.read_file_string().split('\n\n')]
        production = [x.split(',') for x in tmpy]
        for before, after in [x.split('|') for x in tmpx]:
            ordering[after].append(before)

        for update in production:
            if self.is_faulty(ordering, update):
                faulty.append(update)

        result = 0
        for update in faulty:
            relevant_ordering = defaultdict(list)
            for a,b in [(a,b) for a,b in [x.split('|') for x in tmpx] if a in update and b in update]:
                relevant_ordering[b].append(a)
            fixed = [e for e in update if not e in relevant_ordering]
            for key in sorted(relevant_ordering.keys(), key=lambda x: len(relevant_ordering[x])):
                before = [e for e in fixed if e in relevant_ordering[key]]
                after = [e for e in fixed if e not in relevant_ordering[key]]
                fixed = before + [key] + after
            result += int(self.find_middle(fixed))
        return result

    def is_faulty(self, ordering, update):
        updatedict = {page: pos for pos, page in enumerate(update)}
        return not all(all(updatedict[p] < pos for p in ordering[page] if p in updatedict) for page, pos in updatedict.items())


Task5()
