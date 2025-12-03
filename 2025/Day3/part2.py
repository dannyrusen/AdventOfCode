import time

from intructions import input_data

def find_highest_voltage_cell_index(row: str, min_index: int, max_index: int) -> int:
    index_highest_cell = -1
    for cell_index in range(min_index, max_index + 1):
        if index_highest_cell != -1:
            if row[cell_index] > row[index_highest_cell]:
                index_highest_cell = cell_index
        else:
            index_highest_cell = cell_index

    return index_highest_cell

def main():
    battery_rows = input_data.splitlines()

    start_time = time.perf_counter()

    battery_joltage = 0
    for row in battery_rows:
        battery_joltage_row_indexes = []
        min_index = 0
        max_index = len(row) - 1
        for cell_index in range(12, 0, -1):
            max_joltage_index = find_highest_voltage_cell_index(row, min_index, max_index - cell_index + 1)
            battery_joltage_row_indexes.append(max_joltage_index)
            min_index = max_joltage_index + 1

        battery_joltage_string = ""
        for battery_cell_index in battery_joltage_row_indexes:
            battery_joltage_string += row[battery_cell_index]

        battery_joltage += int(battery_joltage_string)


    end_time = time.perf_counter()

    print(f"Done")
    print(f"Battery joltage: {battery_joltage}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()