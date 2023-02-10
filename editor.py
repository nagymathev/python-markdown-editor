import formatters

commands = ["plain", "bold", "italic", "header", "link", "inline-code",
            "new-line", "ordered-list", "unordered-list"]


document: str = ""

while True:
    inp: str = input("Choose a formatter: ")
    inp = inp.strip()
    if inp.startswith("!"):
        inp = inp.lstrip("!")
        if inp == "help":
            formatters.helper()
        elif inp == "done":
            formatters.done(document)
        else:
            formatters.helper()
    elif inp not in commands:
        print("Unknown formatting type or command")
    else:
        if inp == "header":
            document = formatters.header(document)
        elif inp == "plain":
            document = formatters.plain(document)
        elif inp == "bold":
            document = formatters.bold(document)
        elif inp == "italic":
            document = formatters.italic(document)
        elif inp == "inline-code":
            document = formatters.inline_code(document)
        elif inp == "new-line":
            document = formatters.new_line(document)
        elif inp == "link":
            document = formatters.link(document)
        elif inp == "ordered-list":
            document = formatters.make_list(document, ordered=True)
        elif inp == "unordered-list":
            document = formatters.make_list(document, ordered=False)
