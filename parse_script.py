import sys
import unicodedata

if __name__ == '__main__':
    read_header = False
    curr_name = ""

    last_print = ""

    with open(sys.argv[1]) as data:
        for line in data:
            line = line.split()

            if len(line) == 0:
                read_header = False

                next_print = "END: " + curr_name

                if next_print == last_print:
                    continue

                last_print = next_print
                print(unicodedata.normalize('NFKC', last_print))

                continue

            if line[0] == "name":
                curr_name = line[1]
                # print("START: " + curr_name)

            if line[0] == "namedel":
                # print("END: " + curr_name)
                # if curr_name != "":
                #     print("END: " + curr_name)
                # else:
                #     print("END: ")
                curr_name = ""

            if line[0] == "mes":
                read_header = True

                next_print = "START: " + curr_name
                if next_print == last_print:
                    continue

                last_print = next_print
                print(unicodedata.normalize('NFKC', last_print))

                continue

            if read_header:
                print("".join(x + " " for x in line))
