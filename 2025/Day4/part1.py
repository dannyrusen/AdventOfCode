import time

from intructions import input_data

def can_be_accessed_by_forklift(paper_roll_rows, row_index, col_index) -> bool:
    paper_count = 0

    # row over
    if paper_roll_rows[row_index - 1][col_index -1] == '@':
        paper_count += 1
    if paper_roll_rows[row_index - 1][col_index] == '@':
        paper_count += 1
    if paper_roll_rows[row_index - 1][col_index +1] == '@':
        paper_count += 1

    # same row
    if paper_roll_rows[row_index][col_index - 1] == '@':
        paper_count += 1
    if paper_roll_rows[row_index][col_index + 1] == '@':
        paper_count += 1

    # row under
    if paper_roll_rows[row_index + 1][col_index - 1] == '@':
        paper_count += 1
    if paper_roll_rows[row_index + 1][col_index] == '@':
        paper_count += 1
    if paper_roll_rows[row_index + 1][col_index + 1] == '@':
        paper_count += 1

    if paper_count < 4:
        return True
    return False

def main():
    paper_roll_rows = [f".{row}." for row in input_data.splitlines()]

    start_time = time.perf_counter()

    paper_roll_len = len(paper_roll_rows[0])
    paper_row_empty_row = "." * paper_roll_len
    paper_roll_rows.insert(0, paper_row_empty_row)
    paper_roll_rows.append(paper_row_empty_row)


    number_of_accessible_papers = 0
    for row_index in range(1, len(paper_row_empty_row) - 1):
        for col_index in range(1, len(paper_roll_rows[row_index]) - 1):
            if paper_roll_rows[row_index][col_index] == "@":
                if can_be_accessed_by_forklift(paper_roll_rows, row_index, col_index):
                    number_of_accessible_papers += 1

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Number of accessible papers: {number_of_accessible_papers}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()