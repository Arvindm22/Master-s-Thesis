import numpy as np
from matplotlib import pyplot as plt

# Program for simulation of Single vortex:

vortex_pos = (6, 6)
step = 1
duration = 10
color = "blue"  # default particle color
mu = 1

Boundary_range = 12


def calculate_new_position(pos_of_particle, vortex_pos, step, mu):
    (x, y) = pos_of_particle
    d = (x - vortex_pos[0]) ** 2 + (y - vortex_pos[1]) ** 2
    theta = (step * mu) / d
    x_new = np.cos(theta) * (x - vortex_pos[0]) - np.sin(theta) * (y - vortex_pos[1]) + vortex_pos[0]
    y_new = np.sin(
        theta) * (x - vortex_pos[0]) + np.cos(theta) * (y - vortex_pos[1]) + vortex_pos[1]
    return x_new, y_new


class Particle:
    def __init__(self, _pos_of_particle, _color=color):
        self.pos_of_particle = _pos_of_particle
        self.color = _color


class BlinkingVortex:
    def __init__(self, _vortex_pos=vortex_pos, _mu=mu, _step=step, _duration=duration):
        self.vortex_pos = _vortex_pos
        self.mu = _mu
        self.step = _step
        self.duration = _duration
        self.particle_list = []
        self.new_xpos_list = []
        self.new_ypos_list = []

    def initialize_particle(self, _pos_of_particle, _color=color):
        self.particle_list.append(Particle(_pos_of_particle, _color))

    def simulate(self):
        plt.xlim(0, Boundary_range)
        plt.ylim(0, Boundary_range)
        plt.grid()
        plt.plot(vortex_pos[0], vortex_pos[1], color='red', marker='o')
        for p in self.particle_list:
            self.new_xpos_list.append([p.pos_of_particle[0]])
            self.new_ypos_list.append([p.pos_of_particle[1]])
            plt.plot(
                p.pos_of_particle[0], p.pos_of_particle[1], marker='.', color=p.color)
        for t in range(duration):
            for i in range(len(self.particle_list)):
                (x, y) = calculate_new_position(self.particle_list[i].pos_of_particle, self.vortex_pos, self.step,
                                                self.mu)
                self.particle_list[i].pos_of_particle = (x, y)
                self.new_xpos_list[i].append(x)
                self.new_ypos_list[i].append(y)
                plt.plot(vortex_pos[0], vortex_pos[1], color='red', marker='o')
                plt.xlim(0, Boundary_range)
                plt.ylim(0, Boundary_range)
                plt.plot(x, y, marker='.', color=self.particle_list[i].color)
                plt.pause(0.01)
        plt.show()

    def plot_graph(self):
        plt.xlim(0, Boundary_range)
        plt.ylim(0, Boundary_range)
        for i in range(len(self.particle_list)):
            plt.plot(
                self.new_xpos_list[i], self.new_ypos_list[i], color=self.particle_list[i].color)
        for i in range(len(self.particle_list)):
            plt.plot(self.new_xpos_list[i][0], self.new_ypos_list[i]
            [0], marker='.', color=self.particle_list[i].color)
            plt.plot(self.new_xpos_list[i][-1], self.new_ypos_list[i][-1], marker='.',
                     color=self.particle_list[i].color)
        plt.grid()
        plt.plot(vortex_pos[0], vortex_pos[1], color='red', marker='o')
        plt.show()


blinking_vortex_system = BlinkingVortex()
blinking_vortex_system.initialize_particle((6, 7), "blue")
blinking_vortex_system.initialize_particle((6, 8), "green")
blinking_vortex_system.initialize_particle((6, 9), "indigo")
blinking_vortex_system.initialize_particle((6, 10), "crimson")
blinking_vortex_system.initialize_particle((6, 11), "teal")
blinking_vortex_system.simulate()
blinking_vortex_system.plot_graph()

# Program for Double Vortex:


right_vortex_pos = (5, 0)
left_vortex_pos = (-5, 0)
step = 1
duration = 80
color = "blue"
mu = 3
sp = 5  # Switching period

Boundary_range = 10
lim = Boundary_range
theta = 0

def calculate_new_position(pos_of_particle, vortex_pos, step, mu):
    (x, y) = pos_of_particle
    d = (x - vortex_pos[0]) ** 2 + (y - vortex_pos[1]) ** 2
    theta = (step * mu) / d
    x_new = np.cos(theta) * (x - vortex_pos[0]) - np.sin(theta) * (y - vortex_pos[1]) + vortex_pos[0]
    y_new = np.sin(
        theta) * (x - vortex_pos[0]) + np.cos(theta) * (y - vortex_pos[1]) + vortex_pos[1]
    return x_new, y_new

class Particle:
    def __init__(self, _pos_of_particle, _color=color):
        self.pos_of_particle = _pos_of_particle
        self.color = _color


class BlinkingVortex:
    def __init__(self, _right_vortex_pos=right_vortex_pos, _left_vortex_pos=left_vortex_pos, _mu=mu, _step=step,
                 _duration=duration):
        self.right_vortex_pos = _right_vortex_pos
        self.left_vortex_pos = _left_vortex_pos
        self.mu = _mu
        self.step = _step
        self.duration = _duration
        self.particle_list = []
        self.new_xpos_list = []
        self.new_ypos_list = []

    def initialize_particle(self, _pos_of_particle, _color=color):
        self.particle_list.append(Particle(_pos_of_particle, _color))

    def simulate(self):
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)
        plt.grid()
        for p in self.particle_list:
            self.new_xpos_list.append([p.pos_of_particle[0]])
            self.new_ypos_list.append([p.pos_of_particle[1]])
            plt.plot(p.pos_of_particle[0], p.pos_of_particle[1], marker='.', color=p.color)
        for t in range(duration // sp):
            for i in range(len(self.particle_list)):
                if t % 2 != 0:
                    for j in range(sp):
                        (x, y) = calculate_new_position(self.particle_list[i].pos_of_particle, self.right_vortex_pos,
                                                        self.step, self.mu)
                        self.particle_list[i].pos_of_particle = (x, y)
                        self.new_xpos_list[i].append(x)
                        self.new_ypos_list[i].append(y)
                        plt.plot(right_vortex_pos[0], right_vortex_pos[1], color='green', marker='o')
                        plt.plot(left_vortex_pos[0], left_vortex_pos[1], color='red', marker='o')
                        plt.plot(x, y, marker='.', color=self.particle_list[i].color)
                else:
                    for j in range(sp):
                        (x, y) = calculate_new_position(self.particle_list[i].pos_of_particle, self.left_vortex_pos,
                                                        self.step, self.mu)
                        self.particle_list[i].pos_of_particle = (x, y)
                        self.new_xpos_list[i].append(x)
                        self.new_ypos_list[i].append(y)
                        plt.plot(right_vortex_pos[0], right_vortex_pos[1], color='red', marker='o')
                        plt.plot(left_vortex_pos[0], left_vortex_pos[1], color='green', marker='o')
                        plt.plot(x, y, marker='.', color=self.particle_list[i].color)
                plt.xlim(-lim, lim)
                plt.ylim(-lim, lim)
                plt.pause(0.01)
                plt.show()

    def plot_graph(self):
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)
        for i in range(len(self.particle_list)):
            plt.plot(
                self.new_xpos_list[i], self.new_ypos_list[i], color=self.particle_list[i].color)
        for i in range(len(self.particle_list)):
            plt.plot(self.new_xpos_list[i][0], self.new_ypos_list[i]
            [0], marker='.', color=self.particle_list[i].color)
            plt.plot(self.new_xpos_list[i][-1], self.new_ypos_list[i][-1], marker='.',
                     color=self.particle_list[i].color)
        plt.grid()
        plt.show()


blinking_vortex_system = BlinkingVortex()
blinking_vortex_system.initialize_particle((0, 1), "blue")
blinking_vortex_system.initialize_particle((0, 2), "green")
blinking_vortex_system.initialize_particle((0, 3), "indigo")
blinking_vortex_system.initialize_particle((0, 4), "crimson")
blinking_vortex_system.initialize_particle((0, 5), "teal")
blinking_vortex_system.simulate()
blinking_vortex_system.plot_graph()
