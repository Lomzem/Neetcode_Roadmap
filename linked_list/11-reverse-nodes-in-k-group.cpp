struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {
    }
    ListNode(int x) : val(x), next(nullptr) {
    }
    ListNode(int x, ListNode *next) : val(x), next(next) {
    }
};

class Solution {
  public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        ListNode *dummy = new ListNode(0, head);

        ListNode *kth(dummy);
        ListNode *prevGroup(dummy);

        while (true) {
            for (int i(0); i < k; i++) {
                if (kth == nullptr) {
                    break;
                }
                kth = kth->next;
            }
            if (kth == nullptr) {
                break;
            }
            ListNode *cur(prevGroup->next);
            ListNode *groupNext(kth->next);
            ListNode *prev(groupNext);

            while (cur != groupNext) {
                ListNode *curNext = cur->next;
                cur->next = prev;
                prev = cur;
                cur = curNext;
            }
            // cur is just a temp variable
            cur = prevGroup->next;
            prevGroup->next = kth;
            prevGroup = cur;
            kth = prevGroup;
        }
        ListNode *newHead(dummy->next);
        delete dummy;
        return newHead;
    }
};
