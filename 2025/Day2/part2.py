import time

from input import ids

def get_id_range(id_range: str) -> range:
    start, end = map(int, id_range.split("-"))
    return range(start, end + 1)

def check_valid_id(product_id: int) -> bool:
    s = str(product_id)
    n = len(s)

    for i in range(1, n // 2 + 1):
        if check_sequence(s, i):
            return False

    return True

def check_sequence(s: str, length: int) -> bool:
    if length == 0:
        return True

    if len(s) % length != 0:
        return False

    num_repeats = len(s) // length
    return s == s[:length] * num_repeats

def main():
    input_ids = ids.split(",")

    start_time = time.perf_counter()

    invalid_ids_sum = 0
    invalid_ids_count = 0

    for id_range_str in input_ids:
        for id_to_check in get_id_range(id_range_str):
            if not check_valid_id(id_to_check):
                invalid_ids_sum += id_to_check
                invalid_ids_count += 1

    end_time = time.perf_counter()

    print(f"Found {invalid_ids_count} invalid IDs.")
    print(f"Sum Failed IDs: {invalid_ids_sum}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()