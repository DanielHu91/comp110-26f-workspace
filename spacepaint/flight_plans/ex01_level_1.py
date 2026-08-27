"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "730664641"


def main(aura: Ship) -> None:
    """Your Space Paint program's entrypoint."""
    # Your commands here
    aura.beam(on=False)
    aura.turn(degrees=45)
    aura.forward(units=4.2426)
    aura.turn(degrees=135)
    aura.beam(on=True)
    aura.forward(units=6)
    aura.turn(degrees=90)
    aura.beam(on=True)
    aura.forward(units=6)
    aura.turn(degrees=90)
    aura.beam(on=True)
    aura.forward(units=6)
    aura.turn(degrees=90)
    aura.beam(on=True)
    aura.forward(units=6)
    return None


if __name__ == "__main__":
    start_spacepaint()
