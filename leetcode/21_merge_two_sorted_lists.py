# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode(0, None)
      list = dummy

      print(list1)

      while list1 and list2:
        print("list: ", list)
        print("dummy:", dummy)
        print("list1: ", list1)
        print("list2: ", list2)
        print("")

        if list1.val <= list2.val:
          list.next = list1
          list1 = list1.next
        else:
          list.next = list2
          list2 = list2.next
        list = list.next

      list.next = list1 or list2

      print("list: ", list)

      return dummy.next
