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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry(0);
        ListNode *head = new ListNode();
        ListNode *cur(head);
        while (l1 != nullptr || l2 != nullptr) {
            cur->next = new ListNode();
            cur = cur->next;
            int inp1(0);
            int inp2(0);
            if (l1 != nullptr) {
                inp1 = l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                inp2 = l2->val;
                l2 = l2->next;
            }
            int sum(inp1 + inp2 + carry);
            carry = sum / 10;
            int digit(sum % 10);
            cur->val = digit;
        }
        if (carry > 0) {
            cur->next = new ListNode();
            cur = cur->next;
            cur->val = carry;
        }
        cur = head->next;
        delete head;
        return cur;
    }
};
