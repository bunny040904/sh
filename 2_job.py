#Implement job sequencing with deadlines using a greedy method., Write a program to implement Huffman Encoding using a greedy strategy.
def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort jobs by profit
    result = [-1] * n  # To store result of jobs
    total_profit = 0

    for job in jobs:
        for j in range(min(n, job[1]) - 1, -1, -1):  # Find a free slot
            if result[j] == -1:
                result[j] = job[0]  # Assign job to the slot
                total_profit += job[2]
                break

    return [r for r in result if r != -1], total_profit
# Example usage: (job_id, deadline, profit)
jobs = [('Job1', 2, 100), ('Job2', 1, 19), ('Job3', 2, 27), ('Job4', 1, 25), ('Job5', 3, 15)]
scheduled_jobs, max_profit = job_sequencing(jobs, 3)

print(f"Scheduled jobs: {scheduled_jobs}")
print(f"Total profit: {max_profit}")