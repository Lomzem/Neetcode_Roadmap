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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[0]);

        int lenLeft(0);
        for (int i(0); i < inorder.size(); i++) {
            if (inorder[i] == preorder[0]) {
                lenLeft = i;
                break;
            }
        }

        vector<int> leftPreorder;
        for (int i(1); i <= lenLeft; i++) {
            leftPreorder.push_back(preorder[i]);
        }

        vector<int> leftInorder;
        for (int i(0); i < lenLeft; i++) {
            leftInorder.push_back(inorder[i]);
        }

        root->left = buildTree(leftPreorder, leftInorder);

        vector<int> rightPreorder;
        vector<int> rightInorder;
        for (int i(1 + lenLeft); i < preorder.size(); i++) {
            rightPreorder.push_back(preorder[i]);
            rightInorder.push_back(inorder[i]);
        }

        root->right = buildTree(rightPreorder, rightInorder);

        return root;
    }
};
