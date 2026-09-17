"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730664641"

RACING_NAME: str = "Level 0"
RACING_COLOR: str = "#FF0000"


def control(sensors: RobotSensors) -> RobotCommand:
    """This demo is all gas, no steering."""
    throttle: float = 0.15
    steer: float = 0.0

    if sensors.wall_lidar.front_left_m < 4.0:
        steer = 1.0

    if sensors.wall_lidar.front_right_m < 4:
        steer = -1.0

    return RobotCommand(throttle=throttle, steer=steer)
