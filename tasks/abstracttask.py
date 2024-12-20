from abc import ABC, abstractmethod

INPUT_PATH='./input/'

class AbstractTask(ABC):
    instances = {}
    
    def __init__(self, number):
        self.number = number
        AbstractTask.instances[self.number] = self
    
    def read_file_lines(self):
        f = open(INPUT_PATH + str(self.number), "r")
        return [x.strip() for x in f.readlines()]
    
    def read_file_string(self):
        f = open(INPUT_PATH + str(self.number), "r")
        return f.read()
    
    @abstractmethod
    def simple_task(self):
        pass
    
    @abstractmethod
    def extended_task(self):
        pass
    
    