import sys

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1]) as data:
        for line in data:
            line = line.strip("\n")
            lines.append(line)

    for x in range(0, len(lines)):
        if lines[x] == "END: " or lines[x] == "START: ":
            if x < len(lines) - 1:
                if lines[x + 1] == "END: ":
                    lines[x] = None

    lines = [x for x in lines if x]

    # Remove all leading "END"s:
    for x in range(0, len(lines)):
        if lines[x] == "END: ":
            lines[x] = None
        else:
            break

    lines = [x for x in lines if x]


    # Go and mark all consecutives:
    for x in range(len(lines) - 1, 0, -1):
        if "END:" in lines[x] and ("END:" in lines[x - 1] or "START:" in lines[x - 1]):
            lines[x] = None
        else:
            if "START:" in lines[x] and "START:" in lines[x-1]:
                lines[x] = None

    lines = [x for x in lines if x]

    # Remove unneeded empty lines:
    for x in range(0, len(lines)):
        if lines[x] == "END: ":
            if x > 0:
                if "END:" in lines[x - 1]:
                    lines[x] = None

    # Remove trailing:
    for x in range(len(lines) - 1, 0, -1):
        if "START:" in lines[x]:
            lines[x] = None
        else:
            break

    lines = [x for x in lines if x]

    # Remove END at beginning:
    for x in range(0, len(lines)):
        if "END:" in lines[x]:
            lines[x] = None
        else:
            break

    lines = [x for x in lines if x]

    for line in lines:
        if line:
            print(line)