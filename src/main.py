from file import sync_dir
from blocks import generate_page

def main():
    sync_dir("./static", "./public")
    generate_page("./content/index.md", "./template.html", "public/index.html")

if __name__ == "__main__":
    main()
