# Static Site Generator

This is a simple static site generator that converts Markdown files into HTML using a template system. The site can be deployed to GitHub Pages.

## Features
- Converts Markdown files into HTML using a template.
- Recursively processes all Markdown files in the `content/` directory.
- Copies static assets from the `static/` directory to the output folder.
- Supports configurable base paths for deployment.

## Installation
Ensure you have Python installed (preferably Python 3). Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

## Usage
To generate the site locally:

```sh
python3 src/main.py
```

To build the site for GitHub Pages with a custom base path:

```sh
sh build.sh
```

## Directory Structure
```
YOUR_REPO/
│── src/
│   ├── main.py       # Main script for generating the site
│   ├── block_markdown.py  # Markdown processing logic
│── content/          # Markdown files (input)
│── static/           # Static assets (CSS, JS, images)
│── docs/             # Generated site (output, served by GitHub Pages)
│── template.html     # HTML template
│── build.sh          # Build script for production
│── README.md         # Documentation
```