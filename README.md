# Git Commenter

**Git Commenter** is a CLI to make your Git commit message **colorful**.

## Usage

Usage is so simple.  
Instead of `git commit`, all you have only to run `git-commenter`.

### Normal Mode

```sh
git-commenter
```

Normal mode is the simplest use.  
You only run `git-commenter`, all interactively create commit message.

### Clipboard Mode

```sh
git-commenter --clipboard
```

Clipboard mode paste created commit message to the clipboard, instead of committing.  
This is useful for example when you want to input commit message on the GitHub website.

### Message Mode

```sh
git-commenter --message MESSAGE
```

Message mode is the closest use to the actual `git commit -m`.  
You input message as an argument and select only emoji with the CLI.

### Template Mode

```sh
git-commenter --template
```

Template mode is the easiest way for creating commit message.  
You only select all message from the template at once, including emoji.

### Other Commands

| argument       | description        |
| -------------- | ------------------ |
| --clean        | Clean use history. |
| -v / --version | Show version.      |
| -h / --help    | Show help.         |

## Install

```sh
pip install git+https://github.com/skmatz/git-commenter.git [--user]
```
