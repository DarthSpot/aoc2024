from tasks.abstracttask import AbstractTask


class Task15(AbstractTask):
    def __init__(self):
        super().__init__(15)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task15()
