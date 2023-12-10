# Lab 6 exercises(Individual) Merge Linked Lists
# Gupit, Shane Hazel S.
# BSCPE 2-4
# LAB 6


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_lists(list1, list2):
    list = ListNode()
    current = list

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return list.next

def linked_list(head):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Input
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_lists(list1, list2)

print("Merged List:")
linked_list(merged_list)
