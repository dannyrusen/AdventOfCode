import time

from intructions import input_data

def main():
    battery_rows = input_data.splitlines()

    start_time = time.perf_counter()

    battery_joltage = 0
    for row in battery_rows:
        index_first_cell = -1
        index_last_cell = -1
        for cell_index in range(len(row) - 2, -1, -1):
            if index_first_cell != -1:
                if row[cell_index] >= row[index_first_cell]:
                    index_first_cell = cell_index
            else:
                index_first_cell = cell_index

        for cell_index in range(index_first_cell + 1, len(row)):
            if index_last_cell != -1:
                if row[cell_index] >= row[index_last_cell]:
                    index_last_cell = cell_index
            else:
                index_last_cell = cell_index


        battery_joltage += int(row[index_first_cell] + row[index_last_cell])


    end_time = time.perf_counter()

    print(f"Done")
    print(f"Battery joltage: {battery_joltage}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()