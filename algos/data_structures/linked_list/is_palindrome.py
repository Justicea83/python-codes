from . import Node


def is_palindrome(head: Node) -> bool:
    if not head:
        return True

    fast, slow = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None

    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt

    while node:
        if node.item != head.item:
            return False
        node = node.next
        head = head.next
    return True
