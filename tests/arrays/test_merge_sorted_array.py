from problems.arrays.merge_sorted_array import Solution


def test_basic():
    assert Solution().merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3) is None
