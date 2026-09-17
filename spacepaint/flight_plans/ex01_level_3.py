"""Making art... in space!"""

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint

__author__: str = "730664641"


def main(aura: Ship) -> None:
    """Your Space Paint program's entrypoint."""
    # Your commands here
    aura.beam(on=True)
    square_at(aura, 0.0, 0.0, 5.0)
    square_at(aura, 0.0, 0.0, 4.0)
    square_at(aura, 0.0, 0.0, 3.0)
    square_at(aura, 0.0, 0.0, 2.0)
    square_at(aura, 0.0, 0.0, 1.0)
    return None


def square_at(
    ship: Ship,
    center_x: float,
    center_y: float,
    length: float,
) -> None:
    """Paint a square centered at an X/Y point."""
    ship.beam(on=False)
    move_to(ship, center_x + length / 2, center_y + length / 2)
    ship.beam(on=True)
    move_to(ship, center_x - length / 2, center_y + length / 2)
    move_to(ship, center_x - length / 2, center_y - length / 2)
    move_to(ship, center_x + length / 2, center_y - length / 2)
    move_to(ship, center_x + length / 2, center_y + length / 2)
    ship.beam(on=False)


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Compute the turn from the ship's heading toward an X/Y point."""
    heading = degrees(atan2(y - ship.y, x - ship.x))
    return heading - ship.heading_x_y


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((y - ship.y) ** 2 + (x - ship.x) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move the ship from its current position to an X/Y point."""
    ship.turn(angle_between(ship, x, y))
    ship.forward(distance_between(ship, x, y))


if __name__ == "__main__":
    start_spacepaint()
