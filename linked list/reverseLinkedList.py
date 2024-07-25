# This is an input class. Do not edit.
import json
from lib.LinedList import create_linked_list, print_linked_list
from lib.outPutPrint import outPutPrint


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3

    return p1


data = '''{
  "head": "0",
  "nodes": [
    {"id": "0", "next": "1", "value": 0},
    {"id": "1", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 2},
    {"id": "3", "next": "4", "value": 3},
    {"id": "4", "next": "5", "value": 4},
    {"id": "5", "next": null, "value": 5}
  ]
}'''
data = json.loads(data)
head = create_linked_list(data, LinkedList)
print("Original Linked List")
print_linked_list(head)
output = print_linked_list(reverseLinkedList(head))
# outPutPrint(data, output)
