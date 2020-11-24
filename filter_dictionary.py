f = open('master.txt', 'r')
line = f.readline().replace('\n', '')
while line:
    line = line.lower()
    if 2 <= len(set(line)) <= 5 and '-' not in line:
        print(line)
    line = f.readline().replace('\n', '')
