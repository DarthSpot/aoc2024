from tasks.abstracttask import AbstractTask


class Task12(AbstractTask):
    def __init__(self):
        super().__init__(12)
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


Task12()
