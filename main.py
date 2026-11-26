"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching a terrible pizza topping to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and prints it
to stdout. The entry is a fixed string; the program's only job is to
deliver it byte-identically. No network, no file reads, no secrets.
"""

ENTRY = (
    "Try our canned tuna and jelly pizza: it jiggles, it smells like "
    "a harbour, and the jelly insists it's dessert."
)


def main() -> None:
    import os
    import sys

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
