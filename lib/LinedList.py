def create_linked_list(data, LinkedList):
    # Create a dictionary to map node ids to LinkedList objects
    nodes = {}
    for node_data in data['nodes']:
        node_id = node_data['id']
        node_value = node_data['value']
        nodes[node_id] = LinkedList(node_value)

    # Link the nodes together
    for node_data in data['nodes']:
        node_id = node_data['id']
        next_id = node_data['next']
        if next_id is not None:
            nodes[node_id].next = nodes[next_id]

    # Return the head of the linked list
    head_id = data['head']
    return nodes[head_id]


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
