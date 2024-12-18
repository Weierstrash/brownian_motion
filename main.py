import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from brownian import BrownianMotion
import random

new_motion = BrownianMotion()

fps = 10
nSeconds = 5
axis_range  = 20

fig = plt.figure()
ax = plt.gca()
ax.set_aspect('equal')


point_history = []

def update(n):
    plt.cla() #clearing the screen everytime
    plt.grid(color="black",linewidth = 0.4)
    # Set the range of x-axis
    plt.xlim(-axis_range, axis_range)
    # Set the range of y-axis
    plt.ylim(-axis_range, axis_range)

    x,y = new_motion.current_position()
    plt.plot(x, y,"ro")#plotting the current position

    #plotting the point history
    if len(point_history) > 1:
        for index in range(0,len(point_history)-1):
            (x1,y1) = point_history[index]
            (x2,y2) = point_history[index+1]
            x_points = [x1,x2]
            y_points = [y1,y2]
            plt.plot(x_points,y_points,color = "blue")

    new_motion.update_position()
    point_history.append(new_motion.current_position())
    return fig

if __name__ == "__main__":
   
    ani = FuncAnimation(fig = fig, 
                        func = update, 
                        frames = nSeconds * fps,
                        interval = 1000 / fps ) #in ms
    plt.show()
    
