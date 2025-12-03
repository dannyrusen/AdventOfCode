import time

from input import ids

def get_id_range(id_range: str) -> list[int]:
    start, end = map(int, id_range.split("-"))
    return list(range(start, end + 1))

def check_valid_id(product_id: int) -> bool:
    s = str(product_id)
    n = len(s)

    is_false = False
    for i in range(1, n + 1):
        if not check_sequence(s, i):
            is_false = True
            break

    if is_false:
        return False

    return True

def check_sequence(s: str, length: int) -> bool:
    str_part = s[0:length]

    if str_part == s:
        return True

    for i in range(length, len(s), length ):
        if str_part != s[i:i+length]:
            return True

    return False

def main():
    input_ids = ids.split(",")

    start_time = time.perf_counter()

    all_ids = [id_to_check
               for input_id in input_ids
               for id_to_check in get_id_range(input_id)]

    invalid_ids = [id for id in all_ids if not check_valid_id(id)]

    end_time = time.perf_counter()

    print(f"Failed IDs: {invalid_ids}")
    print(f"Sum Failed IDs: {sum(invalid_ids)}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()