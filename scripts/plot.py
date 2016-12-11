#!/usr/bin/env python2
import csv
import matplotlib.pylab as plt


QUADROTOR_ATTITUDE_CONTROLLER_OUTPUT = "/tmp/quadrotor_attitude_controller.dat"
QUADROTOR_POSITION_CONTROLLER_OUTPUT = "/tmp/quadrotor_position_controller.dat"
GIMBAL_ATTITUDE_CONTROLLER_OUTPUT = "/tmp/gimbal_attitude_controller.dat"


def plot_quadrotor_attitude_data():
    attitude_data = {
        "t": [],
        "roll": [],
        "pitch": [],
        "yaw": [],
        "z": []
    }

    attitude_output = open(QUADROTOR_ATTITUDE_CONTROLLER_OUTPUT, "r")
    attitude_reader = csv.reader(attitude_output, delimiter=",")
    next(attitude_reader)

    for row in attitude_reader:
        attitude_data["t"].append(float(row[0]))
        attitude_data["roll"].append(float(row[1]))
        attitude_data["pitch"].append(float(row[2]))
        attitude_data["yaw"].append(float(row[3]))
        attitude_data["z"].append(float(row[4]))

    plt.plot(attitude_data["t"], attitude_data["roll"], label="roll")
    plt.plot(attitude_data["t"], attitude_data["pitch"], label="pitch")
    plt.plot(attitude_data["t"], attitude_data["yaw"], label="yaw")
    plt.plot(attitude_data["t"], attitude_data["z"], label="z")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (degrees)")
    plt.legend(loc=0)
    plt.show()


def plot_quadrotor_position_data():
    position_data = {
        "t": [],
        "roll": [],
        "pitch": [],
        "yaw": [],
        "x": [],
        "y": [],
        "z": []
    }

    position_output = open(QUADROTOR_POSITION_CONTROLLER_OUTPUT, "r")
    position_reader = csv.reader(position_output, delimiter=",")
    next(position_reader)

    for row in position_reader:
        position_data["t"].append(float(row[0]))
        position_data["roll"].append(float(row[1]))
        position_data["pitch"].append(float(row[2]))
        position_data["yaw"].append(float(row[3]))
        position_data["x"].append(float(row[4]))
        position_data["y"].append(float(row[5]))
        position_data["z"].append(float(row[6]))

    plt.subplot(2, 1, 1)
    plt.plot(position_data["t"], position_data["roll"], label="roll")
    plt.plot(position_data["t"], position_data["pitch"], label="pitch")
    plt.plot(position_data["t"], position_data["yaw"], label="yaw")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (degrees)")
    plt.legend(loc=0)

    plt.subplot(2, 1, 2)
    plt.plot(position_data["t"], position_data["x"], label="x")
    plt.plot(position_data["t"], position_data["y"], label="y")
    plt.plot(position_data["t"], position_data["z"], label="z")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")
    plt.legend(loc=0)

    plt.show()


def plot_gimbal_attitude_data():
    attitude_data = {
        "t": [],
        "roll": [],
        "pitch": []
    }

    attitude_output = open(GIMBAL_ATTITUDE_CONTROLLER_OUTPUT, "r")
    attitude_reader = csv.reader(attitude_output, delimiter=",")
    next(attitude_reader)

    for row in attitude_reader:
        attitude_data["t"].append(float(row[0]))
        attitude_data["roll"].append(float(row[1]))
        attitude_data["pitch"].append(float(row[2]))

    plt.plot(attitude_data["t"], attitude_data["roll"], label="roll")
    plt.plot(attitude_data["t"], attitude_data["pitch"], label="pitch")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (degrees)")
    plt.legend(loc=0)
    plt.show()


if __name__ == "__main__":
    plot_quadrotor_attitude_data()
    plot_quadrotor_position_data()
    # plot_gimbal_attitude_data()
