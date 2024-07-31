#include <unordered_map>

class LRUCache {
    struct Node {
        int key;
        int value;
        Node *prev;
        Node *next;

        Node(int key, int value) : key(key), value(value) {
        }
    };

    int capacity;
    std::unordered_map<int, Node *> cache;
    // left is most recent
    Node *left = new Node(0, 0);

    // right is least recent
    Node *right = new Node(0, 0);

    void insert(Node *newNode) {
        Node *second(left->next);
        left->next = newNode;
        newNode->next = second;
        second->prev = newNode;
    }

  public:
    LRUCache(int capacity) : capacity(capacity) {
    }

    int get(int key) {
    }

    void put(int key, int value) {
        // if key exists, delete it from linked list
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
