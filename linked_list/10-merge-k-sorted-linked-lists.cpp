#include <vector>
using namespace std;

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
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
        if (list1 == nullptr) {
            return list2;
        } else if (list2 == nullptr) {
            return list1;
        }

        ListNode *head;
        if (list1->val < list2->val) {
            head = list1;
            list1 = list1->next;
        } else {
            head = list2;
            list2 = list2->next;
        }
        ListNode *cur = head;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                cur->next = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        if (list1 != nullptr) {
            cur->next = list1;
        } else {
            cur->next = list2;
        }
        return head;
    }

  public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.size() == 0) {
            return nullptr;
        }

        while (lists.size() > 1) {
            vector<ListNode *> mergedLists;
            for (int i(0); i < lists.size(); i += 2) {
                ListNode *list2;
                if (i + 1 < lists.size()) {
                    list2 = lists[i + 1];
                } else {
                    list2 = nullptr;
                }
                mergedLists.push_back(mergeTwoLists(lists[i], list2));
            }
            lists = mergedLists;
        }
        return lists[0];
    }
};
