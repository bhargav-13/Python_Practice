from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(500000000,))
    a.start()

    b = Process(target=counter, args=(500000000,))
    b.start()

    a.join()
    b.join()

    print(f"Finished in {time.perf_counter()} seconds")

if __name__ == '__main__':
    main()
