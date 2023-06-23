def stylish(diff, replacer=' ', spacesCount=4) -> str:
    def walk(node, depth):

        result = '{\n'
        for key in node:
            if isinstance(node[key], dict):
                add = walk(node[key], depth + 1)
            else:
                add = str(node[key])

            space = ((spacesCount * depth) - 2) * replacer

            if '+' in key or '-' in key:
                result = f'{result}{space}{str(key).strip()}: {add}\n'
            else:
                result = f'{result}{space}  {str(key)}: {add}\n'

        result += replacer * (spacesCount * (depth - 1)) + '}'

        return result

    return walk(diff, 1)
