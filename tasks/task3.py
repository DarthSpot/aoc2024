import re

from tasks.abstracttask import AbstractTask


class Task3(AbstractTask):
    def __init__(self):
        super().__init__(3)
    
    def simple_task(self):
        return sum([int(x) * int(y) for x,y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', self.read_file_string())])


    def extended_task(self):
        enabled = True
        result = 0
        for do,dont,x,y in re.findall(r'(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)', self.read_file_string()):
            if enabled and x != '' and y != '':
                result += int(x)*int(y)
            elif do != '':
                enabled = True
            elif dont != '':
                enabled = False
        return result


Task3()
