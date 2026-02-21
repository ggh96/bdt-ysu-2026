import os
import multiprocessing as mp

def process_id(message):
    print(f"The current python process id is={os.getpid()} |\n{message}")

if __name__ == "__main__":
    process_id("This is the main program.")

    processes = []
    for n in range(3):
        p = mp.Process(target=process_id, args=(f"Hello from child # {n}",))
        p.start()
        processes.append(p)

    for p in processes:
        print(p)
        print(f"The process is running before join: {p.is_alive()}")
        p.join()
        print(f"The process is running after join: {p.is_alive()}")

    print("All child processes finished.")