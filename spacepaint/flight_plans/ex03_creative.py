"""Making art... in space!"""

"""This program draws an observatory on the ground, Jupiter in the sky, and a constellation further away."""

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint

__author__: str = "730664641"


def main(aura: Ship) -> None:
    """Arrange the components of my scene"""
    # Call your scene procedures heres

    draw_observatory(aura, -5, 0)
    draw_planet(aura, 20, 20, 4, "#8B4513")
    draw_planet(aura, 10, 20, 3, "#ADD8E6")
    draw_planet(aura, 20, 10, 2, "#FAE5BF")
    draw_constellation(aura, 50, 50)
    return None

    # Define your navigation helpers and scene procedures outside of main.

    # def square_at(
    # ship: Ship,
    # center_x: float,
    # center_y: float,
    # length: float,
    # ) -> None:
    """Paint a square centered at an X/Y point."""


#    ship.beam(on=False)
#    move_to(ship, center_x + length / 2, center_y + length / 2)
#    ship.beam(on=True)
#    move_to(ship, center_x - length / 2, center_y + length / 2
#   move_to(ship, center_x - length / 2, center_y - length / 2)
#   move_to(ship, center_x + length / 2, center_y - length / 2)
#    move_to(ship, center_x + length / 2, center_y + length / 2)
#    ship.beam(on=False)


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Return the shortest signed turn toward an X/Y waypoint"""

    if x == ship.x and y == ship.y:
        return 0.0

    destination_heading = degrees(atan2(y - ship.y, x - ship.x))
    turn = destination_heading - ship.heading_x_y

    if turn > 180.0:
        return turn - 360.0

    elif turn < -180.0:
        return turn + 360.0

    else:
        return turn


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((y - ship.y) ** 2 + (x - ship.x) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move the ship from its current position to an X/Y point."""
    ship.turn(angle_between(ship, x, y))
    ship.forward(distance_between(ship, x, y))


def turn_to(ship: Ship, heading: float) -> None:
    """Rotate the ship to face an absolute heading, regardless of its current heading."""
    ship.turn(heading - ship.heading_x_y)


def draw_observatory(ship: Ship, x: float, y: float) -> None:
    """Draw a rectangle with a domed roof, anchored at its bottom-left corner (x, y)."""
    width = 8.0
    height = 4.0

    ship.beam_color(value="#808080")

    ship.beam(on=False)
    move_to(ship, x, y)

    ship.beam(on=True)
    move_to(ship, x, y + height)
    move_to(ship, x + width, y + height)
    move_to(ship, x + width, y)
    move_to(ship, x, y)
    ship.beam(on=False)

    move_to(ship, x + width / 2, y + height)
    turn_to(ship, 0.0)
    ship.beam(on=True)
    draw_dome(ship, radius=width / 4)
    ship.beam(on=False)
    return None


def draw_dome(ship: Ship, radius: float) -> None:
    """Paint a half-circle dome, assuming the ship sits at the roofline midpoint."""
    turn_to(ship, 90.0)
    ship.arc(radius=radius, degrees=180.0)
    return None


def draw_planet(ship: Ship, x: float, y: float, radius: float, color: str) -> None:
    """Draw a Jupiter-like planet at (x, y) with the given radius and a Great Red Spot."""
    spot_radius = radius * 0.27
    spot_offset = radius * 0.15

    ship.beam(on=False)
    move_to(ship, x, y)
    turn_to(ship, 0.0)
    ship.beam(on=True)
    ship.beam_color(value=color)
    ship.fill(on=True, opacity=0.8)
    ship.arc(radius=radius, degrees=360.0)
    ship.beam(on=False)

    move_to(ship, x + spot_offset, y + spot_offset)
    turn_to(ship, 0.0)
    ship.beam(on=True)
    ship.beam_color(value="#D2691E")
    ship.fill(on=True, opacity=0.8)
    ship.arc(radius=spot_radius, degrees=360.0)
    ship.fill(on=False)
    ship.beam(on=False)
    return None


def draw_constellation(ship: Ship, x: float, y: float) -> None:
    """Draw the Big Dipper as stars placed relative to (x, y)."""
    star_offsets: list[tuple[float, float]] = [
        (3.0, -3.6),
        (-6.0, -2.5),
        (-6.6, 3.0),
        (5.4, 2.1),
        (-15.0, 9.0),
        (-20.4, 15.0),
        (-30.0, 15.6),
    ]

    ship.beam(on=False)
    index = 0
    while index < len(star_offsets):
        dx, dy = star_offsets[index]
        move_to(ship, x + dx, y + dy)
        turn_to(ship, 0.0)
        ship.beam(on=True)
        ship.beam_color(value="white")
        ship.fill(on=True, opacity=0.9)
        ship.arc(radius=0.3, degrees=360.0)
        ship.beam(on=False)
        index += 1

    return None


if __name__ == "__main__":
    start_spacepaint()
