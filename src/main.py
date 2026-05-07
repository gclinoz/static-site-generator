from file import sync_dir
from blocks import generate_pages_recursive
import sys

basepath = sys.argv[1] or "/"

def main():
    sync_dir("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()
