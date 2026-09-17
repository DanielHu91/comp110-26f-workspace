"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730664641"

RACING_NAME: str = "Level 1"
RACING_COLOR: str = "#FF0000"


def control(sensors: RobotSensors) -> RobotCommand:
    """This demo is all gas, no steering."""
    throttle: float = 0.25
    steer: float = 0.0
    max_speed = 8.0
    dist = 6.0

    if sensors.wall_lidar.front_left_m < dist:
        steer = 1.0

    if sensors.wall_lidar.front_right_m < dist:
        steer = -1.0

    if sensors.odometry.speed_mps > max_speed:
        throttle = 0.15

    return RobotCommand(throttle=throttle, steer=steer)
