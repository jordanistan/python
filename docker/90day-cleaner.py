import datetime
import subprocess

# Find the current time
current_time = datetime.datetime.now()

# Find all containers that are more than 90 days old
containers_to_remove = []
output = subprocess.run(["docker", "ps", "-a"], capture_output=True).stdout.decode("utf-8")
for line in output.split("\n"):
    if "Created" in line:
        created_date = datetime.datetime.strptime(line.split()[-1], "%Y-%m-%dT%H:%M:%S.%fZ")
        if (current_time - created_date).days > 90:
            containers_to_remove.append(line.split()[-2])

# Remove the old containers
for container in containers_to_remove:
    subprocess.run(["docker", "rm", container])

print("Done!")
