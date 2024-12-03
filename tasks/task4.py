from tasks.abstracttask import AbstractTask


class Task4(AbstractTask):
    def __init__(self):
        super().__init__(4)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task4()
