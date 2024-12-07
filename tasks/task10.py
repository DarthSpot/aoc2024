from tasks.abstracttask import AbstractTask


class Task10(AbstractTask):
    def __init__(self):
        super().__init__(10)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task10()
