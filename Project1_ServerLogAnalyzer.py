"""
Mini Project 1: Server Log Analyzer
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, lists
- P1.1.3: String methods (split, strip), f-strings
- P1.1.4: Dictionaries, lists

Description:
Analyze server log files to categorize by severity and count errors.
"""

# Sample log data
log_data = """2026-02-03 10:15:23 INFO Server started
2026-02-03 10:16:45 ERROR Database connection failed
2026-02-03 10:17:12 WARNING Memory usage high
2026-02-03 10:18:33 ERROR Database connection failed
2026-02-03 10:19:01 INFO User logged in
2026-02-03 10:20:15 ERROR File not found
2026-02-03 10:21:48 WARNING Disk space low
2026-02-03 10:22:30 INFO User logged in
2026-02-03 10:23:17 ERROR Database connection failed
2026-02-03 10:24:55 CRITICAL System memory exhausted"""

print("=" * 50)
print("SERVER LOG ANALYZER")
print("=" * 50)

# Step 1: Parse logs into list of dictionaries
logs = []
for line in log_data.strip().split('\n'):
    parts = line.split(' ', 3)
    log_entry = {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }
    logs.append(log_entry)

print(f"\nTotal logs processed: {len(logs)}")

# Step 2: Count logs by level
level_counts = {}
for log in logs:
    level = log['level']
    if level in level_counts:
        level_counts[level] += 1
    else:
        level_counts[level] = 1

# Step 3: Display level breakdown
print("\nLog Level Breakdown:")
for level in ['CRITICAL', 'ERROR', 'WARNING', 'INFO']:
    count = level_counts.get(level, 0)
    print(f"  {level:10s}: {count}")

# Step 4: Find most common errors
error_messages = {}
for log in logs:
    if log['level'] == 'ERROR':
        msg = log['message']
        if msg in error_messages:
            error_messages[msg] += 1
        else:
            error_messages[msg] = 1

print("\nError Messages:")
for msg, count in error_messages.items():
    print(f"  [{count}x] {msg}")

# Step 5: Calculate severity score
severity_score = 0
severity_score += level_counts.get('CRITICAL', 0) * 10
severity_score += level_counts.get('ERROR', 0) * 5
severity_score += level_counts.get('WARNING', 0) * 2

print(f"\nSeverity Score: {severity_score}")
if severity_score > 30:
    print("Status: CRITICAL - Needs attention!")
elif severity_score > 10:
    print("Status: WARNING - Monitor system")
else:
    print("Status: HEALTHY")

print("=" * 50)
