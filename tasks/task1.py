from tasks.abstracttask import AbstractTask


class Task1(AbstractTask):
    def __init__(self):
        super().__init__(1)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task1()
