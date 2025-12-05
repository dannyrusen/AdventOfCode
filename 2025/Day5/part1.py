import time

from intructions import input_data

def main():

    start_time = time.perf_counter()
    
    fresh_ingredients_range = []
    ingredients = []
    importing_fresh_ingredients = True
    for row in input_data.splitlines():
        if importing_fresh_ingredients:
            if row == "":
                importing_fresh_ingredients = False
                continue
            else:
                fresh_ingredients_range.append([int(x) for x in row.split("-")])

        if not importing_fresh_ingredients:
            ingredients.append(int(row))
        pass

    fresh_ingredients_count = 0
    for ingredient_id in ingredients:
        for start_id, stop_id in fresh_ingredients_range:
            if start_id <= ingredient_id <= stop_id:
                fresh_ingredients_count += 1
                break

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Fresh ingredient count: {fresh_ingredients_count}")

    print(f"Total execution time: {end_time - start_time:.6f}s")

if __name__ == "__main__":
    main()