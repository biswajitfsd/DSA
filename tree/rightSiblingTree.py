# This is the class of the input root. Do not edit it.
import json
from lib.BinaryTree import create_binary_tree, print_tree


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    # Write your code here.
    mutate(root, None, None)
    return root


def mutate(node, parent, isLeftChild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)


data = '''{
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "7", "left": "12", "right": "13", "value": 7},
    {"id": "13", "left": null, "right": null, "value": 13},
    {"id": "12", "left": null, "right": null, "value": 12},
    {"id": "6", "left": "11", "right": null, "value": 6},
    {"id": "11", "left": "14", "right": null, "value": 11},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "5", "left": null, "right": "10", "value": 5},
    {"id": "10", "left": null, "right": null, "value": 10},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "9", "left": null, "right": null, "value": 9},
    {"id": "8", "left": null, "right": null, "value": 8}
  ],
  "root": "1"
}'''

data = json.loads(data)
root = create_binary_tree(data, BinaryTree)
print_tree(root)
print_tree(rightSiblingTree(root))