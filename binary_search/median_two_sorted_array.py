class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = nums1
        B = nums2
        if len(A) < len(B):
            B, A = A, B

        total_len = len(A) + len(B)
        total_len_2 = total_len // 2
        result = min(A[total_len_2 // 2], B[total_len_2 // 2])
        return result


nums1 = [1,2,3,4]
nums2 = [5,6,7,8,9]
assert Solution().findMedianSortedArrays(nums1, nums2) == 5
