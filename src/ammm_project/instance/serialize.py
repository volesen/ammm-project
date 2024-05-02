from typing import TypedDict


class Instance(TypedDict):
    x: int
    y: int
    n: int
    c: int
    w: list[int]
    p: list[int]
    s: list[int]


def serialize_list(values: list[int]) -> str:
    return "[" + " ".join(str(value) for value in values) + "]"


def serialize(instance: Instance) -> str:
    return f"""
x = {instance['x']};
y = {instance['y']};
c = {instance['c']};
n = {instance['n']};
w = {serialize_list(instance['w'])};
p = {serialize_list(instance['p'])};
s = {serialize_list(instance['s'])};
"""
