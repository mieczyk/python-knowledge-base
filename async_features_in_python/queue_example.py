import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f'Task {name} has nothing to do.')
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0

            print(f'Task {name} is running...')

            for _ in range(count):
                total += 1
            print(f'Task {name} - total: {total}.')

def main():
    work_queue = queue.Queue() # FIFO data structure

    for i in [15, 10, 5, 2]:
        work_queue.put(i)

    # Define tasks tuples
    tasks = [
        (task, 'Task One', work_queue),
        (task, 'Task Two', work_queue),
    ]

    # Run the tasks synchronously
    for t, n, q in tasks:
        t(n, q)

if __name__ == '__main__':
    main()
