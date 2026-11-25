import os
import shutil

# All this file does is hand the finished pickup line over: it takes
# entry.txt as it already stands and drops an exact copy where the
# grader looks for it, without touching a single word of the line.


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
