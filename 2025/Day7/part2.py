import time

from intructions import input_data

def main():
    start_time = time.perf_counter()

    lines = list(input_data.splitlines())

    tachyon_beams = {}
    for col_idx, col in enumerate(lines[0]):
        if lines[0][col_idx] == 'S':
            tachyon_beams[(col_idx, 1)] = 1

    for row_index in range(1, len(lines) - 1):
        copy_dict = tachyon_beams.copy()
        for index, (beam_x, beam_y) in enumerate(tachyon_beams):

            count = tachyon_beams[(beam_x, beam_y)]
            if count == 0:
                continue

            if lines[beam_y + 1][beam_x] == '^':
                # Split beam into two new beams
                copy_dict[(beam_x - 1, beam_y + 1)] = copy_dict.get((beam_x - 1, beam_y + 1), 0) + count
                copy_dict[(beam_x + 1, beam_y + 1)] = copy_dict.get((beam_x + 1, beam_y + 1), 0) + count

                # Decrease current beam pos
                copy_dict[(beam_x, beam_y)] = 0

            if lines[beam_y + 1][beam_x] == '.':
                # Increase beam new pos
                copy_dict[(beam_x, beam_y + 1)] = copy_dict.get((beam_x, beam_y + 1), 0) + count

                # Decrease current beam pos
                copy_dict[(beam_x, beam_y)] = 0

        # Cleanup dict
        for k in [k for k, v in copy_dict.items() if v == 0]:
            del copy_dict[k]

        tachyon_beams = copy_dict

    beam_count = 0
    for k in [k for k, v in tachyon_beams.items()]:
         beam_count += tachyon_beams[k]

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Result: {beam_count}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()
