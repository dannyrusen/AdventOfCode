import time

from intructions import input_data

def col_to_int(col):
    # Strip whitespace and keep only non-empty entries
    cleaned = [c.strip() for c in col if c and c.strip()]
    if not cleaned:
        return 0
    return int("".join(cleaned))

def main():
    start_time = time.perf_counter()

    instructions_rows = input_data.splitlines()
    instructions_len = len(instructions_rows)
    operations = list(instructions_rows.pop(instructions_len - 1))
    len_operations = len(operations)

    for op_ix, op in enumerate(operations):
        if op == " ":
            try:
                if op_ix < len_operations - 1 and operations[op_ix + 1] != " ":
                    operations[op_ix] = operations[op_ix + 1]
                else:
                    operations[op_ix] = operations[op_ix - 1]
            except IndexError:
                pass

    total_result = 0
    multiply_set = []
    multiply_set_result = 0
    add_set = []
    add_set_result = 0
    for col_ix, col in reversed(list(enumerate(zip(*instructions_rows)))):
        col_op = operations[col_ix]
        col = list(col)
        col_value = col_to_int(col)

        if col_ix == 0:
            if col_op == "+":
                add_set.append(col_value)
            if col_op == "*":
                multiply_set.append(col_value)

        if col_value == 0 or col_ix == 0:
            add_set_result += sum(add_set)
            for n in multiply_set:
                if multiply_set_result == 0:
                    multiply_set_result = n
                else:
                    multiply_set_result *= n

            print(f"Adding {multiply_set_result + add_set_result} to result")
            total_result += multiply_set_result + add_set_result

            multiply_set_result = 0
            multiply_set.clear()
            add_set_result = 0
            add_set.clear()
        else:
            if col_op == "+":
                add_set.append(col_value)
            if col_op == "*":
                multiply_set.append(col_value)



    # add_result = sum(add)
    # multiply_result = 0
    # for n in multiply:
    #     if multiply_result == 0:
    #         multiply_result = n
    #     else:
    #         multiply_result *= n

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Result: {total_result}")

    print(f"Total execution time: {end_time - start_time:.6f}s")


if __name__ == "__main__":
    main()
