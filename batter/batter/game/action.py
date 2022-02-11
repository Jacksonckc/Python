# A generic class for all the actions.
class Action:
   
    # does nothing but will be used in the sub classes to create polymorphism.
    def execute(self, cast):
       
        raise NotImplementedError("execute not implemented in superclass")