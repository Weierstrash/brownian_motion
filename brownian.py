import random

motion_range = ["UP","DOWN","LEFT","RIGHT"]

class BrownianMotion:
    def __init__(self,_starting_position = (0,0)):
        self._current_position = _starting_position
        self._current_step = 0

    def current_position(self):
        return self._current_position
    
    def current_step(self):
        return self._current_step
    
    def update_position(self):
        self._current_step += 1
        action = random.choice(motion_range)
        if action == "UP":
            (x,y) = self._current_position
            X = x
            Y = y + 1
            self._current_position = (X,Y)
        
        if action == "DOWN":
            (x,y) = self._current_position
            X = x
            Y = y - 1
            self._current_position = (X,Y)

        if action == "LEFT":
            (x,y) = self._current_position
            X = x - 1
            Y = y 
            self._current_position = (X,Y)

        if action == "RIGHT":
            (x,y) = self._current_position
            X = x + 1
            Y = y 
            self._current_position = (X,Y)

    
        

if __name__ == "__main__":
    test_motion = BrownianMotion()
    for _ in range(10):
        print(test_motion.current_position())
        test_motion.update_position()

    




        