"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "730664641"


def main(aura: Ship) -> None:
    """Your Space Paint program's entrypoint."""
    # Your commands here
    aura.beam(on=True)
    square(aura, 4)
    square(aura, 3)
    square(aura, 2)
    square(aura, 1)
    return None


def square(ship: Ship, side: float) -> None:
    """Draw the shape here"""
    ship.forward(units=side)
    ship.turn(degrees=90)
    ship.forward(units=side)
    ship.turn(degrees=90)
    ship.forward(units=side)
    ship.turn(degrees=90)
    ship.forward(units=side)

    return None


if __name__ == "__main__":
    start_spacepaint()
