from typing import Any


def flat(node: Any, flatten: list | None = None) -> list:
    match node:
        case [_, *_]:  # we iterate over one subsequence
            return flat(node[1:], flat(node[0], flatten))  # step in width(step in depth)
        case []:  # one subsequence is finished
            return flatten  # pop up step
        case Other:  # we add one item in the result sequence
            if type(flatten) is list:
                return flatten + [Other]
            return [Other]  # init step
