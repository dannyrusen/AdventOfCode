import time

from intructions import input_data


def main():
    start_time = time.perf_counter()

    lines = list(input_data.splitlines())

    tachyon_beams = []
    for col_idx, col in enumerate(lines[0]):
        if lines[0][col_idx] == 'S':
            tachyon_beams.append((col_idx, 1))

    split_count = 0
    beam_radiating = True
    while beam_radiating:
        next_beams = []
        for beam_idx, (beam_x, beam_y) in enumerate(tachyon_beams):
            if beam_y == len(lines) - 1:
                beam_radiating = False
                continue
            if lines[beam_y + 1][beam_x] == '^':
                has_split = False
                if (beam_x - 1, beam_y + 1) not in next_beams:
                    next_beams.append((beam_x - 1, beam_y + 1))
                    has_split = True

                if (beam_x + 1, beam_y + 1) not in next_beams:
                    next_beams.append((beam_x + 1, beam_y + 1))
                    has_split = True

                if has_split:
                    split_count += 1
            else:
                next_beams.append((beam_x, beam_y + 1))

        if beam_radiating:
            tachyon_beams = next_beams

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Result: {split_count}")

    print(f"Total execution time: {end_time - start_time:.6f}s")


if __name__ == "__main__":
    main()
