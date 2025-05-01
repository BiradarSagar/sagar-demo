class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    result = [None] * n  # To store result (sequence of jobs)
    slot = [False] * n   # To keep track of free time slots

    for job in jobs:
        # Find a free slot for this job (starting from its deadline)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job
                break

    # Print the result
    print("Scheduled Jobs:")
    total_profit = 0
    for job in result:
        if job:
            print(job.job_id, end=" ")
            total_profit += job.profit
    print(f"\nTotal Profit: {total_profit}")

# Taking input from user
jobs = []
n = int(input("Enter number of jobs: "))
print("Enter job details (job_id deadline profit):")
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append(Job(job_id, int(deadline), int(profit)))

job_scheduling(jobs)
