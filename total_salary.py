import logging
from pathlib import Path
from typing import Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def total_salary(path: str) -> Tuple[float, float]:
    """
    Read a text file where each line is "Full Name,salary" and return (total, average).
    Handles missing files and malformed lines gracefully:
    - If the file cannot be opened, returns (0.0, 0.0) and logs an error.
    - Malformed lines (missing comma or non-numeric salary) are skipped with a warning.

    Args:
        path: Path to the text file.

    Returns:
        (total, average)
    """
    total = 0.0
    count = 0
    file_path = Path(path)

    if not file_path.exists():
        logger.error("File not found: %s", path)
        return 0.0, 0.0
    if not file_path.is_file():
        logger.error("Path is not a file: %s", path)
        return 0.0, 0.0

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                if "," not in line:
                    logger.warning("Skipping malformed line %d: %r (no comma)", lineno, line)
                    continue
                name, salary_str = line.split(",", 1)
                salary_str = salary_str.strip()
                try:
                    salary = float(salary_str)
                except ValueError:
                    logger.warning("Skipping line %d: invalid salary %r", lineno, salary_str)
                    continue
                total += salary
                count += 1
    except OSError as exc:
        logger.error("Error reading file %s: %s", path, exc)
        return 0.0, 0.0

    average = total / count if count else 0.0
    return total, average


if __name__ == "__main__":
    # Basic CLI for quick manual testing
    import sys

    if len(sys.argv) < 2:
        print("Usage: python total_salary.py <path_to_salary_file>")
        sys.exit(1)

    total, avg = total_salary(sys.argv[1])
    print(f"Total salary: {total}, Average salary: {avg}")
