import sys
import re

if __name__ == '__main__':
    text = []
    # curr_name = ""

    # read_name = False

    with open(sys.argv[1]) as data:
        for line in data:
            line = line.strip("\n")

            if line.strip() == "":
                continue

            temp = line.split(" ")
            if len(temp) > 0:
                if temp[0] == "START:":
                    read_name = True

                    if len(temp) == 1:
                        text.append(["", [line]])
                    else:
                        text.append([temp[1], []])
                    continue
                if temp[0] == "END:":
                    read_name = False
                    continue

            # if not read_name:
            #     # Narrator / action dialogue
            #     if len(text) == 0:
            #         text.append(["", [line]])
            #     else:
            #         if text[-1][0] == "":
            #             text[-1][1].append(line)
            #         else:
            #             text.append(["", [line]])
            # else:
                text[-1][1].append(line)
    
    # for x in text:
    #     print(x)


    for x in range(len(text) - 1, 0, -1):
        if text[x][0] == text[x - 1][0]:
            new = "".join(n for n in text[x][1])
            text[x - 1][1].append("<br/>" + new)

            text[x] = None

    text = [x for x in text if x]

    # Header:
    print("{{ Transcript | ")


    for x in range(0, len(text)):
        # Name changes:
        text[x][0] = text[x][0].replace("GET[username]", "(user)")
        text[x][0] = text[x][0].replace("&nbsp", " ")

        for n in range(0, len(text[x][1])):
            text[x][1][n] = text[x][1][n].replace("GET[username]", "(user)")

    for x in text:
        if len(x[0]) == 0:
            printed = " {{Transcript/Misc | " + "".join(n for n in x[1]) + "}}"
        else:
            printed = " {{{{Transcript/Character | {0} | ".format(x[0])

            for n in range(0, len(x[1])):
                if n == len(x[1]) - 1:
                    printed += x[1][n]
                else:
                    printed += x[1][n]

            printed += "}}"

        print(printed)

    print("}}")