#include <set>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};

class Solution {
  public:
    bool hasCycle(ListNode *head) {
        std::set<ListNode *> seen;
        ListNode *cur(head);
        while (cur != nullptr) {
            std::pair<std::set<ListNode *>::iterator, bool> ret =
                seen.insert(cur);
            if (ret.second == false) {
                return true;
            }
            cur = cur->next;
        }
        return false;
    }
};
