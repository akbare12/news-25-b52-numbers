"""news-25-b52-numbers entry point (stdlib only).

Copies the pre-rendered front page entry.png into the grader output
directory. No third-party imports: the grader image is stdlib-only,
so this file uses os, shutil and sys only.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("entry.png missing next to main.py\n")
        return 1
    shutil.copyfile(src, dst)
    # Byte-identical copy: the rendered front page is the entry itself.
    print("wrote " + dst + " (" + str(os.path.getsize(dst)) + " bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
