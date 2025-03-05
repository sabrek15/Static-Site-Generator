import os
import shutil

# from textnode import TextNode, TextType
from block_markdown import(markdown_to_html_node,)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith("# "):
            return line[2:].strip()
        
    raise ValueError("No H1 Header in the markdown")

def clear_directory(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def copy_directory_recursive(source, destination):
    if not os.path.exists(source):
        print("source directory doesnot exits")
        return
    
    if not os.path.exists(destination):
        os.mkdir(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_directory_recursive(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    # print(final_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print("Page generated successfull")

def generate_pages_recursive(dir_path, template_path, dest_dir_path):
    if not os.path.exists(dir_path):
        print("content directory doesnot exist")
        return
    
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        dest_item_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))

        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_item_path)
        elif item.endswith(".md"):
            generate_page(item_path, template_path, dest_item_path)

def sync_static_to_public():
    source_static = os.path.join(ROOT_DIR, "static")
    destination_public = os.path.join(ROOT_DIR, "public")
    content_md = os.path.join(ROOT_DIR, "content")
    template_path = os.path.join(ROOT_DIR, "template.html")
    # output_html = os.path.join(destination_public, "index.html")

    print("Clearing the public directory...")
    clear_directory(destination_public)

    print(f"Copying from {source_static} to {destination_public}...")
    copy_directory_recursive(source_static, destination_public)

    print(f"Generating the index page...")
    generate_pages_recursive(content_md, template_path, destination_public)


def main():
    sync_static_to_public()

if __name__ == "__main__":
    main()
