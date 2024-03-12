import numpy as np
import math

Xs = 0.8 # starting point x
Ys = 1.5 # starting point y
Zs = 0.2 # starting point z
R = 0.7 # spiral radius
H = 1.8 # end height
T = 40 # sec
S = 4 # number of spirals
omega = 2*S/T*math.pi #rad/sec


with open("timed_waypoints_yaw.csv", "w") as f:
    f.write("t,x,y,z,yaw\n")

    for t in np.linspace(0, T, (T*10+1)):
        f.write("{},{},{},{},{}\n".format(t, Xs+R-R*math.cos(2*S/T*math.pi*t),Ys+R*math.sin(2*S/T*math.pi*t), Zs+(H-Zs)/T*t, -omega*t))
