# Description:

# Parent class for all the actors, tag will chagne in each child class

# OOP Principles Used:

# Polymorphism

# Reasoning:

# Tag is not useful here, but it will be modified in the child classes, actor.aFunctionInTheChildClass() can be called this way. 

class Actor:
    def __init__(self):
        self._tag = ''

    # Tag setter
    def set_tag(self, tag):
        self._tag = tag

    # Tag getter
    def get_tag(self): 
        return self._tag
    
