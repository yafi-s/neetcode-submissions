class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Always binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)

        while True:
            mid = (l + r) // 2
            mid_b = half - mid

            Aleft = A[mid - 1] if mid > 0 else float("-inf")
            Aright = A[mid] if mid < len(A) else float("inf")

            Bleft = B[mid_b - 1] if mid_b > 0 else float("-inf")
            Bright = B[mid_b] if mid_b < len(B) else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Took too many from A
            elif Aleft > Bright:
                r = mid - 1

            # Took too few from A
            else:
                l = mid + 1