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
        TreeNode* cur(root);
        stack<TreeNode*> stk;

        while (counter < k) {
            while (cur->left != nullptr) {
                stk.push(cur);
                cur = cur->left;
            }
            counter++;
            if (counter == k) {
                return cur->val;
            }

            while (cur->right == nullptr && counter < k) {
                counter++;
                cur = stk.top();
                stk.pop();
            }
            if (counter == k) {
                return cur->val;
            }
            cur = cur->right;
        }
        return cur->val;
    }
};
