##refernce:

##https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python


import math
import timeit
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def time_stuff(fn):
    """
    Measure time of execution of a function
    """
    def wrapper(*args, **kwargs):
        t0 = timeit.default_timer()
        fn(*args, **kwargs)
        t1 = timeit.default_timer()
        print("{} seconds".format(t1 - t0))
    return wrapper

def find_primes_in(nmin, nmax):
    """
    Compute a list of prime numbers between the given minimum and maximum arguments
    """
    primes = []

    # Loop from minimum to maximum
    for current in range(nmin, nmax + 1):

        # Take the square root of the current number
        sqrt_n = int(math.sqrt(current))
        found = False

        # Check if the any number from 2 to the square root + 1 divides the current numnber under consideration
        for number in range(2, sqrt_n + 1):

            # If divisible we have found a factor, hence this is not a prime number, lets move to the next one
            if current % number == 0:
                found = True
                break

        # If not divisible, add this number to the list of primes that we have found so far
        if not found:
            primes.append(current)

    # I am merely printing the length of the array containing all the primes, but feel free to do what you want
    print(len(primes))

@time_stuff
def sequential_prime_finder(nmin, nmax):
    """
    Use the main process and main thread to compute everything in this case
    """
    find_primes_in(nmin, nmax)

@time_stuff
def threading_prime_finder(nmin, nmax):
    """
    If the minimum is 1000 and the maximum is 2000 and we have four workers,
    1000 - 1250 to worker 1
    1250 - 1500 to worker 2
    1500 - 1750 to worker 3
    1750 - 2000 to worker 4
    so let’s split the minimum and maximum values according to the number of workers
    """
    nrange = nmax - nmin
    threads = []
    for i in range(8):
        start = int(nmin + i * nrange/8)
        end = int(nmin + (i + 1) * nrange/8)

        # Start the thread with the minimum and maximum split up to compute
        # Parallel computation will not work here due to the GIL since this is a CPU-bound task
        t = threading.Thread(target = find_primes_in, args = (start, end))
        threads.append(t)
        t.start()

    # Don’t forget to wait for the threads to finish
    for t in threads:
        t.join()

@time_stuff
def processing_prime_finder(nmin, nmax):
    """
    Split the minimum, maximum interval similar to the threading method above, but use processes this time
    """
    nrange = nmax - nmin
    processes = []
    for i in range(8):
        start = int(nmin + i * nrange/8)
        end = int(nmin + (i + 1) * nrange/8)
        p = multiprocessing.Process(target = find_primes_in, args = (start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

@time_stuff
def thread_executor_prime_finder(nmin, nmax):
    """
    Split the min max interval similar to the threading method, but use a thread pool executor this time.
    This method is slightly faster than using pure threading as the pools manage threads more efficiently.
    This method is still slow due to the GIL limitations since we are doing a CPU-bound task.
    """
    nrange = nmax - nmin
    with ThreadPoolExecutor(max_workers = 8) as e:
        for i in range(8):
            start = int(nmin + i * nrange/8)
            end = int(nmin + (i + 1) * nrange/8)
            e.submit(find_primes_in, start, end)

@time_stuff
def process_executor_prime_finder(nmin, nmax):
    """
    Split the min max interval similar to the threading method, but use the process pool executor.
    This is the fastest method recorded so far as it manages process efficiently + overcomes GIL limitations.
    RECOMMENDED METHOD FOR CPU-BOUND TASKS
    """
    nrange = nmax - nmin
    with ProcessPoolExecutor(max_workers = 8) as e:
        for i in range(8):
            start = int(nmin + i * nrange/8)
            end = int(nmin + (i + 1) * nrange/8)
            e.submit(find_primes_in, start, end)

def main():
    nmin = int(1e7)
    nmax = int(1.05e7)
    print("Sequential Prime Finder Starting")
    sequential_prime_finder(nmin, nmax)
    print("Threading Prime Finder Starting")
    threading_prime_finder(nmin, nmax)
    print("Processing Prime Finder Starting")
    processing_prime_finder(nmin, nmax)
    print("Thread Executor Prime Finder Starting")
    thread_executor_prime_finder(nmin, nmax)
    print("Process Executor Finder Starting")
    process_executor_prime_finder(nmin, nmax)

main()