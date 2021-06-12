file_name = input("Enter file: ")
if len(file_name) < 1:
    file_name = "mbox-short.txt"

handle = open(file_name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts[time[0]] = counts.get(time[0], 0) + 1

lst = [(key, value) for key, value in counts.items()]
lst.sort()

for hour, times in lst:
    print(hour, times)