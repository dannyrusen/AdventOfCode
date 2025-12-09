import time

from typing import List, Tuple, Set, Optional

from intructions import input_data

Point3D = Tuple[int, int, int]
Circuit = Set[Point3D]

def calculate_distance(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

def circuit_with_point(circuits: List[Circuit], p: Point3D) -> Optional[Circuit]:
    for circuit in circuits:
        if p in circuit:
            return circuit
    return None

def main():
    start_time = time.perf_counter()

    data_rows = input_data.splitlines()

    coordinates: List[Point3D] = []
    circuits: List[Circuit] = []
    distances = {}

    for row in data_rows:
        x, y, z = map(int, row.split(","))
        coordinates.append((x, y, z))

    for i, p1 in enumerate(coordinates):
        for p2 in coordinates[i + 1:]:
            dist = calculate_distance(p1, p2)
            distances[(p1, p2)] = dist

    sorted_distances = sorted(distances.items(), key=lambda item: item[1])

    for idx, ((p1, p2), dist) in enumerate(sorted_distances[:1000]):
        p1_circuit = circuit_with_point(circuits, p1)
        p2_circuit = circuit_with_point(circuits, p2)

        if p1_circuit is None and p2_circuit is None:
            circuits.append({p1, p2})
            continue

        if p1_circuit is not None and p2_circuit is not None and p1_circuit == p2_circuit:
            continue

        if p1_circuit is not None and p2_circuit is None:
            p1_circuit.add(p1)
            p1_circuit.add(p2)
            continue

        if p1_circuit is None and p2_circuit is not None:
            p2_circuit.add(p1)
            p2_circuit.add(p2)
            continue

        if p1_circuit is not None and p2_circuit is not None:
            new_circuit = p1_circuit.union(p2_circuit)
            circuits.append(new_circuit)
            circuits.remove(p1_circuit)
            circuits.remove(p2_circuit)
            continue

    sorted_circuit = sorted(circuits, key=len, reverse=True)
    circuit_score = 1
    for circuit in sorted_circuit[:3]:
        circuit_score *= len(circuit)

    end_time = time.perf_counter()

    print(f"Done")
    print(f"Result: {circuit_score}")

    print(f"Total execution time: {end_time - start_time:.6f}s")


if __name__ == "__main__":
    main()
