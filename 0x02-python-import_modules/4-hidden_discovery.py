#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    count = len(names)
    for i in range(8, count):
        print("{:s}".format(names[i]))
