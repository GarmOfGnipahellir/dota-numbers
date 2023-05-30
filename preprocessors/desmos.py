import sys
import json
import uuid


def replace(content: str, s: int, e: int, data: dict) -> str:
    before = content[:s]
    after = content[e:]

    id = uuid.uuid4()
    desmos = f'<div id="{id}" style="width: 600px; height: 400px; margin: auto"></div>'
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
        desmos += f'\ncalc.setExpression({{ latex: "{data["expr"]}" }});'
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
    # print(content)
    return content


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)

    for section in book["sections"]:
        for chapter in section.values():
            chapter["content"] = add_desmos(chapter["content"])

    print(json.dumps(book))
