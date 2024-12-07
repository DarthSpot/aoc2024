from tasks.abstracttask import AbstractTask


class Task9(AbstractTask):
    def __init__(self):
        super().__init__(9)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task9()
