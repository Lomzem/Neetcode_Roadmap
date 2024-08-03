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
    Node *left;

    // right is least recent
    Node *right;

    void insert(Node *newNode) {
        // adds node at left of linked list (most recent)
        Node *second(this->left->next);
        this->left->next = newNode;
        newNode->next = second;
        newNode->prev = this->left;
        second->prev = newNode;
    }

    void remove(Node *removedNode) {
        // removes node from linked list (not necessarily least recent)
        removedNode->prev->next = removedNode->next;
        removedNode->next->prev = removedNode->prev;
    }

  public:
    LRUCache(int capacity)
        : capacity(capacity), left(new Node(0, 0)), right(new Node(0, 0)) {
        this->left->next = this->right;
        this->right->prev = this->left;
    }

    int get(int key) {
        if (this->cache.find(key) != this->cache.end()) {
            this->remove(this->cache[key]);
            this->insert(this->cache[key]);
            return this->cache[key]->value;
        }
        return -1;
    }

    void put(int key, int value) {
        // if key exists, delete it from linked list
        if (this->cache.find(key) != this->cache.end()) {
            this->remove(this->cache[key]);
            delete cache[key];
            this->cache.erase(key);
        }

        while (this->cache.size() >= this->capacity) {
            // right is least recent (right is actually a dummy node)
            Node *lru(this->right->prev);
            this->cache.erase(lru->key);
            this->remove(lru);
            delete lru;
        }

        Node *newNode = new Node(key, value);
        this->insert(newNode);
        this->cache[key] = newNode;
    }
};
