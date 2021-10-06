import linkedlist as linkl
class Solution:
    def mergeTwoLists(self, l1, l2):
        if(l1==None): return l2
        if(l2==None): return l1
        
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoList2(self, l1, l2):
        r = current = ListNode()
        while(l1 and l2):
            if(l1.val < l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next= l1 or l2
        return r.next
        


if __name__ == "__main__":
    l1 = linkl.linked_list()

    l2 = linkl.linked_list()
    
    l1.append(1)
    l1.append(2)
    l1.append(4)
    
    l2.append(1)
    l2.append(3)
    l2.append(4)
    
    l1.print()
    l2.print()