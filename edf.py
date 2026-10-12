import heapq


class Task:
    def __init__(self, pid, arrival, burst, deadline):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.deadline = deadline
        self.remaining = burst
        self.start = None
        self.finish = None


def edf(tasks):
    time = 0
    ready_queue = []
    completed = []
    gantt = []
    
    n = len(tasks)
    tasks_sorted = sorted(tasks, key=lambda t: t.arrival)
    i = 0
    
    while len(completed) < n:
        while i < n and tasks_sorted[i].arrival <= time:
            heapq.heappush(
                ready_queue,
                (tasks_sorted[i].deadline,
                 tasks_sorted[i].pid,
                 tasks_sorted[i])
            )
            i += 1
        
        if not ready_queue:
            time += 1
            continue
        
        _, _, current = heapq.heappop(ready_queue)
        
        if current.start is None:
            current.start = time
        
        current.remaining -= 1
        gantt.append(current.pid)
        time += 1
        
        if current.remaining == 0:
            current.finish = time
            completed.append(current)
        else:
            heapq.heappush(
                ready_queue,
                (current.deadline, current.pid, current)
            )
    
    return completed, gantt


def print_results(completed, gantt):
    print("=" * 50)
    print("        EDF Scheduling Results")
    print("=" * 50)
    
    print("\nGantt Chart:")
    print("   " + " -> ".join(gantt))
    
    print("\nTask Details:")
    print("-" * 75)
    print(f"{'Task':<6}{'Arrival':<10}{'Burst':<8}{'Deadline':<10}{'Finish':<8}{'WT':<6}{'TAT':<6}{'Status':<10}")
    print("-" * 75)
    
    total_wt = 0
    total_tat = 0
    
    for t in completed:
        wt = t.finish - t.arrival - t.burst
        tat = t.finish - t.arrival
        total_wt += wt
        total_tat += tat
        
        status = "OK" if t.finish <= t.deadline else "Missed"
        
        print(f"{t.pid:<6}{t.arrival:<10}{t.burst:<8}{t.deadline:<10}{t.finish:<8}{wt:<6}{tat:<6}{status:<10}")
    
    print("-" * 75)
    
    n = len(completed)
    print(f"\nAverage Waiting Time:     {total_wt / n:.2f}")
    print(f"Average Turnaround Time:  {total_tat / n:.2f}")
    
    max_deadline = max(t.deadline for t in completed)
    total_burst = sum(t.burst for t in completed)
    U = total_burst / max_deadline
    print(f"\nUtilization: {U:.2f}")
    
    if U <= 1:
        print("   Schedulable with EDF (U <= 1)")
    else:
        print("   Not schedulable (U > 1)")
    
    missed = [t.pid for t in completed if t.finish > t.deadline]
    if missed:
        print(f"\nMissed deadlines: {', '.join(missed)}")
    else:
        print("\nAll tasks completed before deadline!")


if __name__ == "__main__":
    
    tasks = [
        Task("T1", arrival=0, burst=3, deadline=7),
        Task("T2", arrival=1, burst=2, deadline=5),
        Task("T3", arrival=2, burst=1, deadline=4),
    ]
    
    print("Starting EDF Algorithm...\n")
    
    completed, gantt = edf(tasks)
    
    print_results(completed, gantt)
