
# filename = input("Please give me a filename")

lines = []

with open("mbox-short.txt", 'r') as file_object:
    for line in file_object:
        if "X-DSPAM-Confidence: " in line:
            lines.append(line.split())

float_sums = 0
count = 0

for line in lines:
    float_sums += float(line[1])
    count += 1

print(f"Total lines starting with 'X-DSPAM-Confidence' is {count} and the average of these totals is {round((float_sums/count),4)}")