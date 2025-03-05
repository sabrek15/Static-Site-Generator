import os
import sys
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

def generate_page(from_path, template_path, dest_path, basepath="/"):
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

    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print("Page generated successfull")

def generate_pages_recursive(dir_path, template_path, dest_dir_path, basepath):
    if not os.path.exists(dir_path):
        print("content directory doesnot exist")
        return
    
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        dest_item_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))

        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_item_path, basepath)
        elif item.endswith(".md"):
            generate_page(item_path, template_path, dest_item_path, basepath)

def sync_static_to_public(basepath):
    source_static = os.path.join(ROOT_DIR, "static")
    destination_docs = os.path.join(ROOT_DIR, "docs")
    content_md = os.path.join(ROOT_DIR, "content")
    template_path = os.path.join(ROOT_DIR, "template.html")
    # output_html = os.path.join(destination_public, "index.html")

    print("Clearing the public directory...")
    clear_directory(destination_docs)

    print(f"Copying from {source_static} to {destination_docs}...")
    copy_directory_recursive(source_static, destination_docs)

    print(f"Generating the site pages...")
    generate_pages_recursive(content_md, template_path, destination_docs, basepath)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    print(basepath)
    sync_static_to_public(basepath)

if __name__ == "__main__":
    main()
