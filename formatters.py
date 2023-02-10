import sys


def helper():
    print("Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list")
    print("Special commands: !help !done")


def done(doc: str):
    output = open("output.md", "w", encoding="utf-8")
    output.writelines(doc)
    output.close()
    sys.exit()


def header(doc: str) -> str:
    while True:
        level: int = int(input("Level: "))
        if level not in range(1, 7):
            print("The level should be within the range of 1 to 6")
            continue
        else:
            break
    text: str = input("Text: ")
    head = ("#" * level) + " " + text
    if doc == "":
        doc += f"{head}\n"
    else:
        doc += f"\n{head}\n"
    print(doc)
    return doc


def plain(doc: str) -> str:
    text: str = input("Text: ")
    doc += text
    print(doc)
    return doc


def bold(doc: str) -> str:
    text: str = input("Text: ")
    text = f"**{text}**"
    doc += text
    print(doc)
    return doc


def italic(doc: str) -> str:
    text: str = input("Text: ")
    text = f"*{text}*"
    doc += text
    print(doc)
    return doc


def inline_code(doc: str) -> str:
    text: str = input("Text: ")
    text = f"`{text}`"
    doc += text
    print(doc)
    return doc


def new_line(doc: str) -> str:
    doc += "\n"
    print(doc)
    return doc


def link(doc: str) -> str:
    label: str = input("Label: ")
    url: str = input("URL: ")
    text: str = f"[{label}]({url})"
    doc += text
    print(doc)
    return doc


def make_list(doc: str, ordered=False) -> str:
    text = ""
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        else:
            print("The number of rows should be greater than zero")
            continue
    for row in range(1, rows + 1):
        inp_text = input(f"Row #{row}: ")
        if ordered:
            text += f"{row}. {inp_text}\n"
        else:
            text += f"* {inp_text}\n"
    doc += text
    print(doc)
    return doc
