#include <stack>
#include <vector>
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> nodeStack;

        TreeNode* cur(root);
        while (!nodeStack.empty() || cur != nullptr) {
            while (cur != nullptr) {
                nodeStack.push(cur);
                cur = cur->left;
            }
            cur = nodeStack.top();
            result.push_back(cur->val);
            cur = cur->right;
            nodeStack.pop();
        }

        return result;
    }
};
