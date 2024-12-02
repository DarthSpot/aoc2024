from tasks.abstracttask import AbstractTask


class Task2(AbstractTask):
    def __init__(self):
        super().__init__(2)

    def is_safe(self, report: list):
        sort = sorted(report)
        if report != sort[::-1] and report != sort:
            return False
        return all(1 <= d <= 3 for d in [abs(x-y) for x,y in list(zip(report[1:], report[:-1]))])

    def is_safe_with_damper(self, report: list):
        if self.is_safe(report):
            return True
        for idx, x in enumerate(report):
            subreport = report.copy()
            subreport.pop(idx)
            if self.is_safe(subreport):
                return True
        return False

    def simple_task(self):
        return len(list(filter(lambda report: self.is_safe(list(map(int, report.split()))), self.read_file_lines())))

    
    def extended_task(self):
        return len(list(filter(lambda report: self.is_safe_with_damper(list(map(int, report.split()))), self.read_file_lines())))



Task2()
