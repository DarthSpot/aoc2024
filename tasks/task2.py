from tasks.abstracttask import AbstractTask


class Task2(AbstractTask):
    def __init__(self):
        super().__init__(2)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task2()