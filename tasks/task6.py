from tasks.abstracttask import AbstractTask


class Task6(AbstractTask):
    def __init__(self):
        super().__init__(6)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task6()
