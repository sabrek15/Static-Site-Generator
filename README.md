# Static Site Generator

This is a simple static site generator that converts Markdown files into HTML using a predefined template. The generated site is placed inside the `docs/` directory, making it easy to deploy on GitHub Pages.

## Features
- Converts Markdown files into HTML using a template.
- Recursively processes all Markdown files in the `content/` directory.
- Copies static assets from the `static/` directory to the output folder.
- Supports configurable base paths for deployment.

## Project Purpose
This project was developed to learn and apply concepts of functional programming and object-oriented programming (OOP).


## Project Structure

```
Static-Site-Generator/
│── content/            # Contains markdown files to be converted into HTML
│── docs/               # Output directory where the generated site is stored
│── src/                # Source code for the static site generator
│   │── block_markdown.py       # Handles block-level markdown parsing
│   │── htmlnode.py             # Defines HTML node structures
│   │── inline_markdown.py       # Handles inline markdown parsing
│   │── main.py                  # Entry point for generating the site
│   │── test_block_markdown.py   # Unit tests for block markdown parsing
│   │── test_htmlnode.py         # Unit tests for HTML node structures
│   │── test_inline_markdown.py  # Unit tests for inline markdown parsing
│   │── test_textnode.py         # Unit tests for text node handling
│   │── textnode.py              # Defines structures for markdown text nodes
│── static/             # Contains static assets (CSS, images, etc.)
│── template.html       # HTML template used to render markdown content
│── .gitignore          # Specifies files and directories to ignore in git
│── build.sh            # Script to build the site for deployment
│── main.sh             # Script to run the generator locally
│── test.sh             # Script to run all unit tests
│── README.md           # Project documentation
```

## Installation & Usage

### Prerequisites
- Python 3.x installed

### Running Locally
To generate the static site locally, run:
```sh
python3 src/main.py
```
This will generate HTML pages from Markdown files inside the `content/` directory and store them in the `docs/` directory.

## Testing
To run unit tests:
```sh
bash test.sh
```

## Additional Information
- `inline_markdown.py` processes inline Markdown elements such as bold, italic, and links.
- `block_markdown.py` handles block-level elements like paragraphs and lists.
- `htmlnode.py` provides utilities for structuring HTML elements.
- `textnode.py` defines text-based structures for Markdown parsing.
- `template.html` is the core template used for rendering Markdown to HTML.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.