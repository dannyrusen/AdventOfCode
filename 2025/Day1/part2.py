import time
from intructions import instructions


dialValue: int = 50
code: int = 0

def revolve_dial(dial_value: int, instruction: str) -> tuple[int, int]:
    turnDirection: int = -1 if instruction[0] == "L" else 1
    turn_value = int(instruction[1:])
    turn_points = turn_value * turnDirection
    new_dial_value = (dial_value + turn_points)

    laps = 0
    while new_dial_value < 0:
        new_dial_value += 100
        laps += 1

    while new_dial_value > 99:
        new_dial_value -= 100
        laps += 1

    if turnDirection == -1 and new_dial_value == 0:
        laps += 1

    if turnDirection == -1 and dial_value == 0:
        laps -= 1

    return new_dial_value, laps



dial_instructions = instructions.split("\n")

start_time = time.perf_counter()

for instruction in dial_instructions:
    inputDialValue = dialValue
    dialValue, laps = revolve_dial(inputDialValue, instruction)
    code = code + laps
    # print(f"instruction {instruction} inputDial: {inputDialValue}, outputDial: {dialValue} laps: {laps} code: {code}")

end_time = time.perf_counter()

print(f"Final code: {code}")
print(f"Total execution time: {end_time - start_time:.6f}s")

