# flake8: noqa: C901


def create_diff(file1: dict, file2: dict):
    def walk(node1: dict, node2: dict, depth=0):

        keys = set(node1.keys())
        keys.update(node2.keys())
        keys = sorted(keys)
        diff = {}

        for key in keys:
            if key in node1 and key in node2:
                if node1[key] == node2[key]:
                    diff[f'{key}'] = node1[key]
                else:
                    if isinstance(node1[key], dict) and \
                            isinstance(node2[key], dict):
                        diff[f'{key}'] = walk(node1[key], node2[key], depth + 1)
                    else:
                        diff[f'- {key}'] = node1[key]
                        diff[f'+ {key}'] = node2[key]
            elif key in node1:
                diff[f' - {key}'] = node1[key]
            else:
                diff[f' + {key}'] = node2[key]
        return diff

    return walk(file1, file2, 1)
