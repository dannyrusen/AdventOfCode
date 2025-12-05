import time

import itertools
from intructions import input_data

def main():
    start_time = time.perf_counter()
    
    original_fresh_ingredients_range = []
    for row in input_data.splitlines():
        if row == "":
            break
        else:
            original_fresh_ingredients_range.append([int(x) for x in row.split("-")])

    original_fresh_ingredients_range.sort(key=lambda interval: interval[0])

    merged_ranges = [original_fresh_ingredients_range[0]]
    for i in range(1, len(original_fresh_ingredients_range)):
        current_start, current_stop = original_fresh_ingredients_range[i]
        last_merged_start, last_merged_stop = merged_ranges[-1]

        if current_start <= last_merged_stop:
            merged_ranges[-1][1] = max(last_merged_stop, current_stop)
        else:
            merged_ranges.append([current_start, current_stop])

    number_of_fresh_ingredients = 0
    for start_id, stop_id in merged_ranges:
        number_of_fresh_ingredients += stop_id - start_id + 1

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Fresh ingredient count: {number_of_fresh_ingredients}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()