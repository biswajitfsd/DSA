# This is the class of the input root. Do not edit it.
import json
from lib.BinaryTree import create_binary_tree, print_tree


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal_sol1(tree1, tree2):
    # Write your code here.
    treeTraStack1 = [tree1]
    treeTraStack2 = [tree2]
    while len(treeTraStack1) > 0 and len(treeTraStack2) > 0:
        tree1leaf = getNextLeafNode(treeTraStack1)
        tree2leaf = getNextLeafNode(treeTraStack2)
        if tree1leaf.value != tree2leaf.value:
            return False

    return len(treeTraStack1) == 0 and len(treeTraStack2) == 0


def compareLeafTraversal_sol2(tree1, tree2):
    tree1LeafNodesLinkList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkList, _ = connectLeafNodes(tree2)

    while tree1LeafNodesLinkList is not None and tree2LeafNodesLinkList is not None:
        if tree1LeafNodesLinkList.value != tree2LeafNodesLinkList.value:
            return False

        tree1LeafNodesLinkList = tree1LeafNodesLinkList.right
        tree2LeafNodesLinkList = tree2LeafNodesLinkList.right

    return tree1LeafNodesLinkList is None and tree2LeafNodesLinkList is None


def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode

    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode

        previousNode = currentNode

    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)


def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop()
    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)
        if currentNode.left is not None:
            traversalStack.append(currentNode.right)

        currentNode = traversalStack.pop()

    return currentNode


def isLeafNode(node):
    return node.left is None and node.right is None


tree1 = '''{
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": null, "right": "6", "value": 3},
    {"id": "4", "left": null, "right": null, "value": 4},
    {"id": "5", "left": "7", "right": "8", "value": 5},
    {"id": "6", "left": null, "right": null, "value": 6},
    {"id": "7", "left": null, "right": null, "value": 7},
    {"id": "8", "left": null, "right": null, "value": 8}
  ],
  "root": "1"
}'''
tree2 = '''{
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "7", "value": 2},
    {"id": "3", "left": null, "right": "5", "value": 3},
    {"id": "4", "left": null, "right": null, "value": 4},
    {"id": "5", "left": "8", "right": "6", "value": 5},
    {"id": "6", "left": null, "right": null, "value": 6},
    {"id": "7", "left": null, "right": null, "value": 7},
    {"id": "8", "left": null, "right": null, "value": 8}
  ],
  "root": "1"
}'''

data1 = json.loads(tree1)
data2 = json.loads(tree2)

node1 = create_binary_tree(data1, BinaryTree)
node2 = create_binary_tree(data2, BinaryTree)
print(compareLeafTraversal_sol2(node1, node2))
