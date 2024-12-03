from tasks.abstracttask import AbstractTask


class Task5(AbstractTask):
    def __init__(self):
        super().__init__(5)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task5()
