#include <iostream>
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
  public:
    void reorderList(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head->next;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        // now slow is at the halfway point
        // i dont think we need fast
        ListNode *prev = nullptr;
        while (slow != nullptr) {
            ListNode *temp(slow->next);
            slow->next = prev;
            prev = slow;
            slow = temp;
        }
        // now prev is at the "head" (former tail)
        while (head != nullptr && prev != nullptr) {
            ListNode *headNext(head->next);
            head->next = prev;
            head = headNext;
            ListNode *prevNext(prev->next);
            prev->next = headNext;
            prev = prevNext;
        }
    }
};
