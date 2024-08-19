#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {
    }
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {
    }
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {
    }
};

class Solution {
  public:
    int kthSmallest(TreeNode* root, int k) {
        int counter(0);
        stack<TreeNode*> stk;
        TreeNode* cur(root);

        while (true) {
            while (cur != nullptr) {
                stk.push(cur);
                cur = cur->left;
            }
            cur = stk.top();
            counter++;
            if (counter == k) {
                return cur->val;
            }
            stk.pop();
            cur = cur->right;
        }
    }
};
