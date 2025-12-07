import logging
from pathlib import Path
from typing import List, Dict

logger = logging.getLogger(__name__)


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Read a file where each line contains "id,name,age" and return a list of dicts:
    [{"id": id, "name": name, "age": age}, ...]
    Uses UTF-8 encoding. Malformed lines are skipped with a warning.
    If the file cannot be read, returns an empty list and logs an error.

    Args:
        path: Path to the cats info file.

    Returns:
        List of dictionaries with keys "id", "name", "age".
    """
    cats = []
    file_path = Path(path)

    if not file_path.exists():
        logger.error("File not found: %s", path)
        return cats
    if not file_path.is_file():
        logger.error("Path is not a file: %s", path)
        return cats

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    logger.warning("Skipping malformed line %d: %r", lineno, line)
                    continue
                cat_id, name, age = [p.strip() for p in parts]
                cats.append({"id": cat_id, "name": name, "age": age})
    except OSError as exc:
        logger.error("Error reading file %s: %s", path, exc)
        return []

    return cats


if __name__ == "__main__":
    # Configure logging for CLI usage; callers can configure logging themselves.
    logging.basicConfig(level=logging.INFO)
    import sys
    if len(sys.argv) < 2:
        print("Usage: python cats_info.py <path_to_cats_file>")
        sys.exit(1)

    cats = get_cats_info(sys.argv[1])
    for c in cats:
        print(c)
