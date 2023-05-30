import sys
import json


def add_desmos(content: str):
    for i, c in enumerate(content):
        print(i, c)
        if c == "`" and content[i:i+9] == "```desmos":
            print(i, "found start")
    return content


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)

    # for section in book["sections"]:
    #     for chapter in section.values():
    #         chapter["content"] = add_desmos(chapter["content"])

    print(json.dumps(book))
