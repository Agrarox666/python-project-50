def plain(diff) -> str:
    def walk(node, path=''):

        result = ''
        for key in node:

            normalized_key = key.replace('+', '').replace('-', '').strip()
            if path != '':
                new_path = f'{path}.{normalized_key}'
            else:
                new_path = normalized_key

            if isinstance(node[key], dict):
                if '+' in key or '-' in key:
                    result += plain_switch(key, new_path, node[key])
                else:
                    result += walk(node[key], new_path)
            else:
                result += (plain_switch(key, new_path, node[key]))

        return result

    return walk(diff)

# flake8: noqa: C901
def plain_switch(key, path, value) -> str:
    if isinstance(value, dict):
        value = '[complex value]'
    elif value != 'true' and value != 'false' and value != 'null':
        value = f'\'{value}\''

    if key[:3] == ' + ':
        return f'Property \'{path}\' was added with value: {value}\n'
    elif key[:3] == ' - ':
        return f'Property \'{path}\' was removed\n'
    elif key[:2] == '- ':
        return f'Property \'{path}\' was updated. From {value} to '
    elif key[:2] == '+ ':
        return f'{value}\n'
    else:
        return ''
