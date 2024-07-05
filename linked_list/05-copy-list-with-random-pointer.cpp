#include <cstddef>
#include <map>
using namespace std;

class Node {
  public:
    int val;
    Node *next;
    Node *random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
  public:
    Node *copyRandomList(Node *head) {
        if (head == nullptr) {
            return nullptr;
        }
        Node *cur(head);
        map<Node *, Node *> oldToNew;
        oldToNew.insert(pair(nullptr, nullptr));
        while (cur != nullptr) {
            oldToNew.insert(pair(cur, new Node(cur->val)));
            cur = cur->next;
        }
        cur = head;
        while (cur != nullptr) {
            Node *curClone(oldToNew.at(cur));
            curClone->next = oldToNew.at(cur->next);
            curClone->random = oldToNew.at(cur->random);
            cur = cur->next;
        }
        return oldToNew.at(head);
    }
};
