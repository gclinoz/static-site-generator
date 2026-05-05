from pathlib import Path
import shutil

def sync_dir(src_dir, dest_dir, nest=False):
    dest = Path(dest_dir)
    if not dest.exists():
        print(f"Creating {dest}...")
        dest.mkdir()

    src = Path(src_dir)
    if not src.exists():
        raise Exception("Source dir not exist")

    # delete contents of the destination directory
    # at the very start
    if not nest:
        for i in dest.iterdir():
            if i.is_dir():
                print(f"Remove dir {i}")
                shutil.rmtree(i)
            else:
                print(f"Remove file {i}")
                i.unlink()

    # copy all contents to destination recursively
    for i in src.iterdir():
        if i.is_dir():
            sync_dir(str(i), str(dest / i.stem), nest=True)
        else:
            print(f"Copy {i}")
            shutil.copy(i, dest)
