"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730664641"

RACING_NAME: str = "Level 3"
RACING_COLOR: str = "#FF0000"


def control(sensors: RobotSensors) -> RobotCommand:
    """This demo is all gas, no steering."""
    throttle: float = 0.0
    steer: float = 0.0
    # max_speed = 8.0
    # dist = 6.0

    steer = sensors.camera.heading_error_degrees / 10.0

    throttle = (15.0 - sensors.odometry.speed_mps) / 15.0

    return RobotCommand(throttle=throttle, steer=steer)
