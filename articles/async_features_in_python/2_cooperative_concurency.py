# Still synchronous but tasks are being executed in turns (context is being switched).
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
                yield # Turns the task() func into generator. The context is switched back to the caller.
            print(f'Task {name} - total: {total}.')

def main():
    work_queue = queue.Queue() # FIFO data structure

    for i in [15, 10, 5, 2]:
        work_queue.put(i)

    # Define tasks tuples
    tasks = [
        task('Task One', work_queue),
        task('Task Two', work_queue)
    ]

    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t) # Gives control back to task(). Continues the execution after the point where yield was called.
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

if __name__ == '__main__':
    main()
