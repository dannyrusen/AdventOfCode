import time

from intructions import input_data

import re

def main():
    start_time = time.perf_counter()

    trimmed_input_data = re.sub(r'[^\S\r\n]{2,}', ' ', input_data)

    instructions_rows = trimmed_input_data.splitlines()
    instructions_rows = [row.strip() for row in instructions_rows if row]
    instructions_len = len(instructions_rows)
    operations = instructions_rows.pop(instructions_len - 1).split(" ")

    column_result = [0] * len(operations)
    for row_ix, row in enumerate(instructions_rows):
        for col_ix, col in enumerate(row.split(" ")):
            if operations[col_ix] == "+":
                column_result[col_ix] += int(col)
            if operations[col_ix] == "*":
                if column_result[col_ix] == 0:
                    column_result[col_ix] = int(col)
                else:
                    column_result[col_ix] *= int(col)


    sum_column_result = sum(column_result)
    end_time = time.perf_counter()

    print(f"Done")
    print(f"Result: {sum_column_result}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()
