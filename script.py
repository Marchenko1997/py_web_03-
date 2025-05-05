import os
import shutil
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def copy_file(file_path: Path, target_root: Path):
    ext = file_path.suffix.lower().lstrip(".")
    if not ext:
        return
    target_folder = target_root / ext
    target_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target_folder / file_path.name)


def process_directory(
    source_dir: Path, target_root: Path, executor: ThreadPoolExecutor
):
    for item in source_dir.iterdir():
        if item.is_dir():
            executor.submit(process_directory, item, target_root, executor)
        elif item.is_file():
            executor.submit(copy_file, item, target_root)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_folder> [target_folder]")
        sys.exit(1)

    source_folder = Path(sys.argv[1])
    if not source_folder.exists() or not source_folder.is_dir():
        print("Source folder does not exist or is not a directory.")
        sys.exit(1)

    target_folder = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")
    target_folder.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor(max_workers=10) as executor:
        process_directory(source_folder, target_folder, executor)
