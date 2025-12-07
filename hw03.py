import sys
from pathlib import Path
from typing import List

from colorama import init as colorama_init, Fore, Style

colorama_init(autoreset=True)


def _print_tree_dir(path: Path, prefix: str = ""):
    """
    Helper that prints a tree view for a single directory.
    Uses ├── and └── connectors and colors directories vs files.
    """
    try:
        entries: List[Path] = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "[Permission Denied]" + Style.RESET_ALL)
        return

    count = len(entries)
    for idx, entry in enumerate(entries):
        connector = "└── " if idx == count - 1 else "├── "
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + entry.name + "/" + Style.RESET_ALL)
            new_prefix = prefix + ("    " if idx == count - 1 else "│   ")
            _print_tree_dir(entry, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + entry.name + Style.RESET_ALL)


def print_tree(path: Path):
    if not path.exists():
        print(f"Error: path does not exist: {path}")
        return
    if not path.is_dir():
        print(f"Error: path is not a directory: {path}")
        return

    print(Fore.BLUE + str(path) + "/" + Style.RESET_ALL)
    _print_tree_dir(path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python hw03.py /path/to/directory")
        sys.exit(1)
    target = Path(sys.argv[1])
    print_tree(target)


if __name__ == "__main__":
    main()
