import time
import multiprocessing as mp


def task(n: int) -> int:
    """CPU-bound task: sum numbers from 0 to n-1."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


def run_sequential(numTasks: int, n: int):
    """Run tasks sequentially in a single process."""
    start = time.time()
    results = [task(n) for _ in range(numTasks)]
    elapsed = time.time() - start
    return elapsed, results


def run_parallel_pool(numTasks: int, n: int, workers: int = 4):
    """Run tasks in parallel using a multiprocessing Pool."""
    start = time.time()
    with mp.Pool(processes=workers) as pool:
        results = pool.map(task, [n] * numTasks)
    elapsed = time.time() - start
    return elapsed, results


if __name__ == "__main__":
    numTasks = 8
    nLarge = 4_000_000
    nSmall = 2
    runs = 5

    for run in range(1, runs):
        print(f"\n--- Run {run} ---")

        # Large task
        timeSeqLarge, resSeqLarge = run_sequential(numTasks, nLarge)
        print(f"Sequential (large task): {timeSeqLarge: .5f}")

        timeParLarge, resParLarge = run_parallel_pool(numTasks, nLarge, workers=4)
        print(f"Multiprocessing (large task): {timeParLarge: .5f}")

        # Very small task
        timeSeqSmall, resSeqSmall = run_sequential(numTasks, nSmall)
        print(f"Sequential (small task): {timeSeqSmall: .5f}")

        timeParSmall, resParSmall = run_parallel_pool(numTasks, nSmall, workers=4)
        print(f"Multiprocessing (small task): {timeParSmall: .5f}")
