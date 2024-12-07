from tasks.abstracttask import AbstractTask


class Task7(AbstractTask):
    def __init__(self):
        super().__init__(7)

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x * y

    def try_resolve(self, test: int, current: int, remainder: list):
        if current > test:
            return False
        elif len(remainder) == 0:
            return test == current
        else:
            head, *tail = remainder
            mul_value = current * head
            add_value = current + head
            return self.try_resolve(test, add_value, tail) or self.try_resolve(test, mul_value, tail)

    def try_resolve_ex(self, test: int, current: int, remainder: list):
        if current > test:
            return False
        elif len(remainder) == 0:
            return test == current
        else:
            head, *tail = remainder
            mul_value = current * head
            add_value = current + head
            merge_value = int(''.join([str(current), str(head)]))
            return (self.try_resolve_ex(test, add_value, tail)
                    or self.try_resolve_ex(test, mul_value, tail)
                    or self.try_resolve_ex(test, merge_value, tail))

    def simple_task(self):
        result = 0
        for line in self.read_file_lines():
            test_value, remainder = line.split(':')
            test_value = int(test_value)
            values = list(map(int, remainder.strip().split(' ')))
            head, *tail = values
            if self.try_resolve(test_value, head, tail):
                result += test_value
        return result

    
    def extended_task(self):
        result = 0
        for line in self.read_file_lines():
            test_value, remainder = line.split(':')
            test_value = int(test_value)
            values = list(map(int, remainder.strip().split(' ')))
            head, *tail = values
            if self.try_resolve_ex(test_value, head, tail):
                result += test_value
        return result


Task7()
