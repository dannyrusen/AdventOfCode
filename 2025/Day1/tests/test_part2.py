import pytest

from part2 import revolve_dial


# Contract:
# - Input dial_value in [0, 99]
# - instruction format: 'L<number>' or 'R<number>' where number >= 0
# - Output: (new_dial_value [0-99], laps [int])
# - Laps count the number of times the dial passes through 1->0 when turning left,
#   or 99->0 when turning right. Starting at 0 should not count as a lap for left.

@pytest.mark.parametrize(
    "dial, instr, expected_dial, expected_laps",
    [
        # No movement
        (0, "L0", 0, 0),
        (0, "R0", 0, 0),
        # Simple left without crossing
        (50, "L10", 40, 0),
        # Simple right without crossing
        (50, "R10", 60, 0),
        # Left crossing once: from 50, move 68 left crosses once (after 50 steps)
        (50, "L68", 82, 1),
        # Right crossing once: from 50, move 60 right crosses once (after 49 steps to 99, then next to 0)
        (50, "R60", 10, 1),
        # Starting at 0, removing 150: should count only actual crossing, i.e., 1
        (0, "L150", 50, 1),
        # Starting at 0, add 150 right: crosses once
        (0, "R150", 50, 1),
        # Large left moves: from 75, L230 -> net -230; crosses twice
        (75, "L230", (75 - 230) % 100, 2),
        # Large right moves: from 25, R230 -> net +230; crosses twice
        (25, "R230", (25 + 230) % 100, 2),
        # Exact crossing boundary left: from 10, L10 -> new 0, laps 0 (no passing through 1->0)
        (10, "L10", 0, 0),
        # Exact crossing boundary right: from 99, R1 -> new 0, laps 1 (passes 99->0)
        (99, "R1", 0, 1),
        # Multiple exact cycles left: from 1, L101 -> new 0, laps 1 (passes 1->0 once)
        (1, "L101", 0, 1),
        # Multiple exact cycles right: from 0, R200 -> new 0, laps 2 (passes 99->0 twice)
        (0, "R200", 0, 2),
        # From 0, L1 -> wrap to 99, laps 0 (starting at 0 doesn't count)
        (0, "L1", 99, 0),
        # From 0, L100 -> back to 0, laps 1
        (0, "L100", 0, 1),
        # From 0, L101 -> to 99, laps 1
        (0, "L101", 99, 1),
        # From 99, R100 -> back to 99, count 1 lap
        (99, "R100", 99, 1),
        # From 99, R101 -> to 0, count 2 laps (two wraps)
        (99, "R101", 0, 2),
        # After landing at 0 exactly, moving right without crossing should not count.
        (0, "R10", 10, 0),
    ],
)
def test_revolve_dial_cases(dial, instr, expected_dial, expected_laps):
    new_dial, laps = revolve_dial(dial, instr)
    assert new_dial == expected_dial
    assert laps == expected_laps
