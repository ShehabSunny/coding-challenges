# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        rl = result
        carry = 0
        while True:
            if l1 == None and l2 == None:
                if carry == 1:
                    rl.next = ListNode(1)
                return result.next
            
            n1 = l1.val if l1 != None else 0
            n2 = l2.val if l2 != None else 0
            n = n1 + n2 + carry
            if n < 10:
                rl.next = ListNode(n)
                carry = 0
            else:
                rl.next = ListNode(n - 10)
                carry = 1
                
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            rl = rl.next


# generate a ListNode
def genNodeList(*args):
    l = ListNode(args[0])
    a = l
    for i in args[1:]:
        a.next = ListNode(i)
        a = a.next
    return l

# prints a ListNode
def printNodeList(list: ListNode):
    while True:
        print(list.val, end=" ")
        if list.next != None:
            list = list.next  
        else:
            break

if __name__ == "__main__":
    s = Solution()
    res = s.addTwoNumbers(
        genNodeList(9, 9),
        genNodeList(9),
    )
    printNodeList(res)
    