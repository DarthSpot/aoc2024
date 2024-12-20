from tasks.abstracttask import AbstractTask


class Task13(AbstractTask):
    def __init__(self):
        super().__init__(13)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task13()
