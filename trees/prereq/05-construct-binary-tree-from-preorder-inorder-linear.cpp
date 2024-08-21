#include <unordered_map>
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
  private:
    TreeNode* buildTreeHelper(vector<int> &preorder, vector<int> &inorder,
                              unordered_map<int, int> &indices, int &index,
                              int leftPointer, int rightPointer) {
        if (leftPointer > rightPointer) {
            return nullptr;
        }

        TreeNode* root = new TreeNode(preorder[index]);

        int mid(indices[preorder[index]]);

        index++;
        root->left = buildTreeHelper(preorder, inorder, indices, index,
                                     leftPointer, mid - 1);

        root->right = buildTreeHelper(preorder, inorder, indices, index,
                                      mid + 1, rightPointer);

        return root;
    }

  public:
    TreeNode* buildTree(vector<int> &preorder, vector<int> &inorder) {
        int index(0);

        unordered_map<int, int> indices; // map from value to index
        for (int i(0); i < inorder.size(); i++) {
            indices[inorder[i]] = i;
        }

        return buildTreeHelper(preorder, inorder, indices, index, 0,
                               preorder.size() - 1);
    }
};
