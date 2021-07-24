import multiprocessing
import time
import os

def some_task():
    time.sleep(1)
    print('Done')
    
def some_task_with_params(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print('Done')


def no_mp():
    print('Synchronous')
    start = time.perf_counter()

    some_task()
    some_task()

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")
    print()

def mp():
    print('Asynchronous')
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=some_task)
    p2 = multiprocessing.Process(target=some_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f"Finished in {round(end-start, 2)} second(s)")
    print()
    
def loop_mp():
    print('Asynchronous with more processes')
    start = time.perf_counter()
    
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=some_task)
        p.start()
        processes.append(p)
        
    for process in processes:
        process.join()
        
    end = time.perf_counter()
    
    print(f"Finished in {round(end-start, 2)} second(s)")
    print()
    
def loop_mp_with_params():
    print('Asynchronous with more processes')
    start = time.perf_counter()
    
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=some_task_with_params, args=(1.5, ))
        p.start()
        processes.append(p)
        
    for process in processes:
        process.join()
        
    end = time.perf_counter()
    
    print(f"Finished in {round(end-start, 2)} second(s)")
    print()

def mp_pool():
    print('Pool')
    start = time.perf_counter()
    
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        params = [1, 2, 3, 4, 5]
        result = pool.map(some_task_with_params, params)
    
    end = time.perf_counter()
    print(f"Finished in {round(end-start, 2)} second(s)")
    print()

if __name__ == "__main__":
    no_mp()
    mp()
    loop_mp()
    loop_mp_with_params()
    mp_pool()