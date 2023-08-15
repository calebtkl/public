def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2
    p1, p2, p3 = m - 1, n - 1, m + n - 1

    # Merge the arrays from the end, starting with the largest elements
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1

    # If there are remaining elements in nums2, add them to the beginning of nums1
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1

# Example usage:
nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 3, 4, 5, 6]

