import sys
import json
import uuid


def replace(content: str, s: int, e: int, data: dict) -> str:
    before = content[:s]
    after = content[e:]

    id = uuid.uuid4()
    desmos = f'<div id="{id}" style="height: 400px; margin: auto"></div>'
    desmos += "\n<script>"

    desmos += f'\nvar elt = document.getElementById("{id}");'
    desmos += "\nvar calc = Desmos.GraphingCalculator(elt, {"
    desmos += "\nexpressionsCollapsed: true,"
    desmos += "\npasteGraphLink: true,"
    try:
        desmos += f'xAxisLabel: "{data["xLabel"]}",'
    except:
        pass
    try:
        desmos += f'yAxisLabel: "{data["yLabel"]}",'
    except:
        pass
    desmos += "\n});"

    try:
        for expr in data["expr"]:
            desmos += f'\ncalc.setExpression({json.dumps(expr)});'
    except:
        pass

    try:
        l, r, b, t = data["bounds"]
        desmos += f'\ncalc.setMathBounds({{ left: {l}, right: {r}, bottom: {b}, top: {t} }});'
    except:
        pass

    desmos += "\ncalc.setDefaultState(calc.getState());"

    desmos += "\n</script>"

    return f"{before}{desmos}{after}"


def add_desmos(content: str):
    while True:
        s = content.find("```desmos")
        if s == -1:
            break

        e = content.find("```", s+9)
        if e == -1:
            break

        data = content[s+9:e]
        content = replace(content, s, e+3, json.loads(data))
    return content


def chapter_walk(chapters: list) -> list:
    for chapter in chapters:
        chapter["Chapter"]["content"] = add_desmos(
            chapter["Chapter"]["content"])
        chapter_walk(chapter["Chapter"]["sub_items"])
    return chapters


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)

    chapter_walk(book["sections"])

    # book["sections"].append({"Chapter": {
    #     "name": "Debug",
    #     "content": json.dumps(book, indent=2),
    #     "number": [666],
    #     "sub_items": [],
    #     "path": "debug.md",
    #     "source_path": "debug.md",
    #     "parent_names": [],
    # }})

    print(json.dumps(book))
