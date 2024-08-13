struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {
    }
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {
    }
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {
    }
};

class Solution {
  public:
    TreeNode *deleteNode(TreeNode *root, int key) {
        if (root == nullptr) {
            return nullptr;
        }

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (root->left == nullptr) {
                TreeNode *tmp(root);
                root = root->right;
                delete tmp;
            } else if (root->right == nullptr) {
                TreeNode *tmp(root);
                root = root->left;
                delete tmp;
            } else {
                // find min right child
                TreeNode *min(root->right);
                while (min->left != nullptr) {
                    min = min->left;
                }
                root->val = min->val;
                root->right = deleteNode(root->right, min->val);
            }
        }

        return root;
    }
};
