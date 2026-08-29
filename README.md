# EDMD — Terminal Markdown Creator

Please note that AI was used to help with grammar and translation.

<div align="center">
  <img
    width="604"
    height="254"
    alt="EDMD terminal preview"
    src="https://github.com/user-attachments/assets/0355512f-739d-4371-8f6a-ee2120a009b4"
  />
</div>

EDMD is a small, terminal-based Markdown editor written in Python.

It is designed to be minimal and fast without interrupting your workflow. EDMD is especially useful for quickly creating Markdown notes and todo lists.

> EDMD is currently in early development. Bugs may occur.

## Features

- Create and save Markdown files
- Open files for viewing or editing
- Edit, insert and delete
- Search for text inside the current document
- Display the current document
- Choose a custom directory for saved files
- Switch between two color themes (more are coming soon)
- Turn off/on warning messages (for those who knows what they are doing)
- Interactive terminal menus powered by `prompt_toolkit`

## Available themes

- Default
- Tokyo Night

The selected theme and save directory will be stored in a local `data.json` configuration file.

## Requirements

- Python 3
- [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit)

Install the required dependency with:

```bash
python3 -m pip install prompt_toolkit
```

## Installation

Clone the repository:

```bash
git clone https://github.com/NoPoCo-Germany/edmd-Terminal-based-markdown-creator-.git
```

Open the project directory:

```bash
cd edmd-Terminal-based-markdown-creator-
```

Start EDMD:

```bash
python3 main.py
```

Keep `colors.py` in the same directory as `main.py`.

## Terminal shortcut

On macOS or Linux, you can make the script executable:

```bash
chmod +x main.py
```

You can then create a symbolic link (best for fast users):

```bash
mkdir -p ~/.local/bin
ln -s "$(pwd)/main.py" ~/.local/bin/edmd
```

If `~/.local/bin` is included in your `PATH`, you can start the editor from anywhere:

```bash
edmd
```

## Commands

| Command | Description |
|---|---|
| `:help` | Shows all available commands |
| `:save` | Saves the current document |
| `:exit` | Exits EDMD |
| `:new` | Starts a new document |
| `:open` | Opens an existing file |
| `:edit` | Edits an existing line |
| `:delete` | Deletes a line |
| `:insert` | Inserts a new line |
| `:search` | Searches the current document |
| `:show` | Displays the current document |
| `:pfad` | Changes the directory used for saved files |
| `:themes` | Opens the theme selection menu |
| `:warnings` | Enables or disables warnings for the current session |

## Language

The EDMD interface is currently available in German only. An English version is planned for the future. (pst. next update will be different languages)

## Preview

https://github.com/user-attachments/assets/a536b187-831d-43d3-af4d-bad92a07cbb8

## Development note

I am currently completing my German Abitur, so development and updates may slow down. EDMD is primarily a learning project, but I also want to turn it into a useful terminal Markdown editor.

Feedback, bug reports and suggestions are welcome.
