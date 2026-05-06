from file import sync_dir
from blocks import generate_pages_recursive

def main():
    sync_dir("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()
