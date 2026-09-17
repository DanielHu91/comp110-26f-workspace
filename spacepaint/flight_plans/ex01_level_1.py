"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "730664641"


def main(aura: Ship) -> None:
    """Your Space Paint program's entrypoint."""
    # Your commands here
    aura.beam(on=True)
    square(ship=aura)
    square(ship=aura)
    square(ship=aura)
    square(ship=aura)
    return None


def square(ship: Ship) -> None:
    """Draw the shape here"""
    ship.forward(units=6)
    ship.turn(degrees=90)
    ship.forward(units=6)
    ship.turn(degrees=90)
    ship.forward(units=6)
    ship.turn(degrees=90)
    ship.forward(units=6)
    return None


if __name__ == "__main__":
    start_spacepaint()
