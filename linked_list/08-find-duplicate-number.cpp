#include <vector>
using namespace std;

class Solution {
  public:
    int findDuplicate(vector<int> &nums) {
        int slow = 0;
        int fast = 0;
        while (true) {
            slow = nums.at(slow);
            fast = nums.at(nums.at(fast));
            if (slow == fast) {
                break;
            }
        }
        int slow2 = 0;
        while (true) {
            slow = nums.at(slow);
            slow2 = nums.at(slow2);
            if (slow == slow2) {
                break;
            }
        }
        return slow;
    }
};
