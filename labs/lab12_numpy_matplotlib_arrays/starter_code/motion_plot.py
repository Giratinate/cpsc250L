import numpy as np
import matplotlib.pyplot as plt

def position(t, x0, v0, a):
    return x0 + v0 * t + 0.5 * a * np.square(t)

def velocity(t, v0, a):
    return v0 + (a * t)

def main():
    # Consider a projectile launched at a speed of 50 m/s and an angle of 45 degrees.
    #
    # Goal: create plots of x vs. t, y vs. t, v_x vs. t, and v_y vs. t
    #       for 0 < t < 10 seconds
    #
    # TODO: create time array using np.linspace
    time = np.arange(0, 10, 1)
    v0 = 50.0
    angle = 30.0
    ay = -9.805
    ax = 0.0
    x0 = 0.0
    y0 = 0.0
    # TODO: compute position and velocity arrays
    v0x = v0 * np.cos(angle * np.pi/180)
    v0y = v0 * np.sin(angle * np.pi/180)
    # TODO: make and save plots
    pass


main()
