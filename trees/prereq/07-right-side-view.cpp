#include <vector>
#include <queue>
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int qSize = q.size();
            TreeNode* cur = q.front();
            if (cur->left) {
                q.push(cur->left);
            }
            if (cur->right) {
                q.push(cur->right);
            }
            for (int i = 1; i < qSize; i++) {
                cur = q.front();
                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
                q.pop();
            }
            cur = q.front();
            res.push_back(cur->val);
            if (cur->left) {
                q.push(cur->left);
            }
            if (cur->right) {
                q.push(cur->right);
            }
            q.pop();
        }
        return res;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(3);
    root->right->right = new TreeNode(4);
    Solution s;
    s.rightSideView(root);
    return 0;
}
