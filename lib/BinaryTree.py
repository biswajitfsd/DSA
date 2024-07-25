def create_binary_tree(data, BinaryTree):
    # Create a dictionary to map node ids to BinaryTree objects
    nodes = {node_data['id']: BinaryTree(node_data['value']) for node_data in data['nodes']}

    # Link the nodes together
    for node_data in data['nodes']:
        node_id = node_data['id']
        left_id = node_data['left']
        right_id = node_data['right']
        if left_id is not None:
            nodes[node_id].left = nodes[left_id]
        if right_id is not None:
            nodes[node_id].right = nodes[right_id]

    # Return the root of the binary tree
    root_id = data['root']
    return nodes[root_id]


def print_tree(node, level=0, side="root"):
    if node is not None:
        print(" " * 4 * level + f"{side}: {node.value}")
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")
