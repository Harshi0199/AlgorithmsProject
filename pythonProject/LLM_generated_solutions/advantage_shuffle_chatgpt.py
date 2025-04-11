from typing import List
import heapq
import random

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        max_heap = [(-val, idx) for idx, val in enumerate(nums2)]
        heapq.heapify(max_heap)

        result = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        while max_heap:
            val, idx = heapq.heappop(max_heap)
            if nums1[right] > -val:
                result[idx] = nums1[right]
                right -= 1
            else:
                result[idx] = nums1[left]
                left += 1

        return result


def generate_test_case():
    # Generate random numbers list nums1
    nums1 = random.sample(range(1, 101), random.randint(2, 10))

    # Generate random numbers list nums2 with same length as nums1
    nums2 = random.sample(range(1, 101), len(nums1))

    # Calculate the expected result using the Solution class
    expected_result = Solution.advantageCount(nums1, nums2)

    return nums1, nums2, expected_result


def generate_test_case():
    solution = Solution()

    # Generate random numbers list nums1
    nums1 = random.sample(range(1, 101), random.randint(2, 10))

    # Generate random numbers list nums2
    nums2 = random.sample(range(1, 101), len(nums1))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.advantageCount(nums1, nums2)

    return nums1, nums2, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums1, nums2, expected_result = generate_test_case()
        solution = Solution()
        assert solution.advantageCount(nums1, nums2) == expected_result
        print(f"assert solution.advantageCount({nums1}, {nums2}) == {expected_result}")
        test_case_generator_results.append(
            f"assert solution.advantageCount({nums1}, {nums2}) == {expected_result}")  # You can find that we construct the test case in the same format as the example
    return test_case_generator_results


solution = Solution()

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

# --------------------------------------
# Test Cases:
#assert solution.advantageCount([37, 100], [64, 98]) == [100, 37]
assert solution.advantageCount([19, 46, 74, 79], [72, 94, 68, 4]) == [79, 46, 74, 19]
assert solution.advantageCount([10, 23, 29, 43, 45, 77, 81, 87, 91], [23, 18, 54, 9, 85, 60, 12, 48, 50]) == [43, 29,
                                                                                                              87, 10,
                                                                                                              45, 91,
                                                                                                              23, 77,
                                                                                                              81]
assert solution.advantageCount([2, 74], [9, 23]) == [74, 2]
assert solution.advantageCount([57, 66], [81, 5]) == [66, 57]
assert solution.advantageCount([29, 36, 43, 48, 53, 65, 73, 99], [25, 24, 21, 81, 52, 50, 41, 82]) == [43, 36, 29, 99,
                                                                                                       65, 53, 48, 73]
assert solution.advantageCount([5, 8, 39, 50, 93, 97], [41, 65, 16, 34, 20, 71]) == [97, 8, 39, 93, 50, 5]
assert solution.advantageCount([23, 27, 28, 46, 49, 70, 79, 86, 91, 98], [99, 80, 22, 45, 64, 37, 83, 1, 100, 92]) == [
    79, 86, 27, 49, 70, 46, 91, 23, 28, 98]
assert solution.advantageCount([15, 78], [72, 1]) == [78, 15]
assert solution.advantageCount([4, 8, 36, 78, 85], [44, 76, 7, 35, 38]) == [85, 4, 8, 36, 78]
assert solution.advantageCount([1, 9, 30, 31, 37, 45, 62, 79, 93], [18, 1, 56, 51, 93, 84, 44, 14, 27]) == [31, 9, 79,
                                                                                                            62, 1, 93,
                                                                                                            45, 30, 37]
assert solution.advantageCount([53, 58, 82], [69, 47, 2]) == [82, 58, 53]
assert solution.advantageCount([18, 26, 39, 54, 60, 63, 64, 73, 80, 87], [53, 9, 80, 41, 62, 28, 20, 95, 69, 49]) == [
    63, 18, 87, 54, 64, 39, 26, 80, 73, 60]
assert solution.advantageCount([1, 7, 10, 22, 37, 39, 63, 67, 91], [7, 32, 81, 10, 95, 55, 48, 72, 73]) == [10, 37, 7,
                                                                                                            22, 1, 67,
                                                                                                            63, 91, 39]
assert solution.advantageCount([58, 70, 80, 100], [87, 85, 2, 11]) == [80, 100, 58, 70]
assert solution.advantageCount([17, 19, 32, 45, 51, 57, 59, 77, 81], [49, 85, 70, 17, 37, 95, 29, 88, 55]) == [51, 81,
                                                                                                               77, 19,
                                                                                                               45, 17,
                                                                                                               32, 59,
                                                                                                               57]
assert solution.advantageCount([1, 6, 23, 40, 41, 56, 71, 95, 96, 97], [15, 83, 27, 87, 67, 84, 59, 54, 66, 11]) == [40,
                                                                                                                     97,
                                                                                                                     41,
                                                                                                                     1,
                                                                                                                     96,
                                                                                                                     6,
                                                                                                                     71,
                                                                                                                     56,
                                                                                                                     95,
                                                                                                                     23]
assert solution.advantageCount([40, 53, 58, 80, 81], [43, 63, 96, 51, 74]) == [53, 80, 40, 58, 81]
assert solution.advantageCount([74, 77, 98], [53, 5, 43]) == [98, 74, 77]
assert solution.advantageCount([16, 89], [51, 40]) == [16, 89]
assert solution.advantageCount([34, 40, 43, 51, 55, 86, 94], [80, 20, 92, 85, 6, 77, 11]) == [94, 43, 51, 55, 34, 86,
                                                                                              40]
assert solution.advantageCount([32, 44, 70, 83, 89, 94, 98], [11, 40, 14, 85, 75, 71, 39]) == [32, 83, 44, 98, 94, 89,
                                                                                               70]
assert solution.advantageCount([16, 43, 52, 60, 72, 96], [15, 44, 81, 49, 77, 54]) == [16, 52, 43, 60, 96, 72]
assert solution.advantageCount([21, 29], [90, 4]) == [29, 21]
assert solution.advantageCount([7, 15, 79], [51, 47, 11]) == [7, 79, 15]
assert solution.advantageCount([3, 4, 18, 29, 32, 56, 59, 68, 91], [32, 43, 45, 67, 5, 64, 79, 13, 99]) == [56, 59, 68,
                                                                                                            32, 18, 91,
                                                                                                            4, 29, 3]
assert solution.advantageCount([1, 38, 76, 89], [74, 27, 92, 57]) == [89, 38, 1, 76]
assert solution.advantageCount([8, 33], [90, 29]) == [8, 33]
assert solution.advantageCount([5, 15, 24, 27, 42], [61, 50, 29, 90, 47]) == [15, 24, 42, 5, 27]
assert solution.advantageCount([10, 13, 37, 79, 81, 84], [34, 22, 2, 69, 62, 49]) == [79, 37, 10, 13, 84, 81]
assert solution.advantageCount([14, 19, 21, 61, 81, 88], [37, 26, 35, 64, 82, 1]) == [88, 61, 81, 21, 19, 14]
assert solution.advantageCount([13, 49, 60, 67, 79], [2, 66, 69, 1, 83]) == [49, 67, 79, 13, 60]
assert solution.advantageCount([1, 11, 19, 36, 50, 65, 79, 84, 85, 88], [91, 62, 24, 19, 92, 41, 93, 61, 59, 30]) == [
    19, 88, 50, 36, 11, 79, 1, 85, 84, 65]
assert solution.advantageCount([20, 28, 43, 52, 54, 85, 87, 92, 98], [96, 88, 95, 40, 10, 84, 74, 89, 32]) == [28, 92,
                                                                                                               54, 52,
                                                                                                               20, 87,
                                                                                                               85, 98,
                                                                                                               43]
assert solution.advantageCount([6, 10, 19, 22, 32, 51, 65, 69, 70, 75], [23, 41, 93, 66, 51, 62, 20, 40, 79, 89]) == [
    32, 65, 6, 75, 69, 70, 22, 51, 19, 10]
assert solution.advantageCount([6, 13, 30, 34, 45, 55, 67, 99], [41, 38, 78, 61, 30, 17, 66, 63]) == [55, 45, 6, 67, 34,
                                                                                                      30, 13, 99]
assert solution.advantageCount([28, 33, 43, 97], [79, 3, 37, 72]) == [33, 28, 43, 97]
assert solution.advantageCount([15, 23, 26, 33, 43, 56, 64, 83, 84, 91], [62, 12, 85, 9, 21, 98, 49, 77, 45, 81]) == [
    83, 23, 43, 15, 26, 33, 64, 84, 56, 91]
assert solution.advantageCount([40, 41], [47, 24]) == [41, 40]
assert solution.advantageCount([38, 53], [6, 81]) == [38, 53]
assert solution.advantageCount([1, 15, 25, 32, 53, 71, 81], [84, 73, 31, 24, 76, 92, 74]) == [15, 81, 32, 25, 53, 1, 71]
assert solution.advantageCount([29, 76], [8, 65]) == [29, 76]
assert solution.advantageCount([4, 22, 32, 63, 84], [33, 84, 61, 94, 93]) == [63, 32, 84, 4, 22]
assert solution.advantageCount([2, 9, 29, 35, 41, 96], [89, 2, 8, 10, 29, 83]) == [2, 9, 29, 35, 41, 96]
assert solution.advantageCount([7, 15, 21, 34, 44, 56, 67, 74, 84], [86, 16, 61, 51, 32, 83, 9, 44, 58]) == [7, 21, 84,
                                                                                                             67, 34, 44,
                                                                                                             15, 56, 74]
assert solution.advantageCount([18, 28, 41, 56, 59, 90], [35, 71, 99, 48, 43, 33]) == [56, 28, 18, 90, 59, 41]
assert solution.advantageCount([2, 47, 75, 76], [20, 79, 95, 1]) == [47, 76, 75, 2]
assert solution.advantageCount([3, 5, 37, 53, 75, 84, 86, 91, 92, 95], [40, 49, 60, 53, 55, 68, 18, 59, 43, 4]) == [53,
                                                                                                                    84,
                                                                                                                    95,
                                                                                                                    86,
                                                                                                                    91,
                                                                                                                    3,
                                                                                                                    37,
                                                                                                                    92,
                                                                                                                    75,
                                                                                                                    5]
assert solution.advantageCount([4, 6, 11, 28, 64, 72, 84, 92, 95], [51, 84, 85, 7, 17, 94, 42, 34, 47]) == [92, 95, 6,
                                                                                                            11, 28, 4,
                                                                                                            72, 64, 84]
assert solution.advantageCount([35, 96], [48, 87]) == [96, 35]
assert solution.advantageCount([1, 4, 10, 22, 41, 55, 60, 82, 92, 97], [50, 89, 61, 67, 38, 88, 24, 93, 11, 41]) == [82,
                                                                                                                     4,
                                                                                                                     92,
                                                                                                                     97,
                                                                                                                     55,
                                                                                                                     10,
                                                                                                                     41,
                                                                                                                     1,
                                                                                                                     22,
                                                                                                                     60]
assert solution.advantageCount([22, 33, 47, 50, 53, 76, 91, 94, 95], [98, 97, 24, 79, 48, 59, 12, 23, 80]) == [53, 95,
                                                                                                               47, 91,
                                                                                                               50, 76,
                                                                                                               22, 33,
                                                                                                               94]
assert solution.advantageCount([27, 36, 44, 52, 55, 67, 71, 92], [64, 29, 87, 55, 73, 58, 75, 89]) == [92, 36, 44, 67,
                                                                                                       55, 71, 52, 27]
assert solution.advantageCount([20, 57, 66, 67, 86], [4, 46, 31, 28, 35]) == [20, 86, 66, 57, 67]
assert solution.advantageCount([11, 37, 45, 60, 65, 74, 79, 90, 91], [59, 95, 85, 35, 69, 92, 90, 16, 14]) == [65, 11,
                                                                                                               90, 60,
                                                                                                               74, 79,
                                                                                                               91, 45,
                                                                                                               37]
assert solution.advantageCount([5, 35, 50, 56, 62, 64, 79, 87, 90], [16, 56, 24, 97, 99, 72, 90, 60, 28]) == [35, 62,
                                                                                                              50, 87, 5,
                                                                                                              79, 90,
                                                                                                              64, 56]
assert solution.advantageCount([22, 30, 31, 39, 48, 80, 100], [70, 67, 54, 14, 9, 4, 12]) == [48, 100, 80, 39, 30, 22,
                                                                                              31]
assert solution.advantageCount([4, 15, 25, 29, 34, 41, 42, 44, 71, 99], [24, 99, 87, 34, 70, 71, 82, 55, 65, 36]) == [
    25, 4, 15, 41, 44, 34, 29, 71, 99, 42]
assert solution.advantageCount([20, 33, 62, 64, 70, 94, 98], [94, 30, 92, 35, 71, 75, 23]) == [20, 62, 70, 64, 94, 98,
                                                                                               33]
assert solution.advantageCount([76, 88, 99], [53, 65, 52]) == [88, 99, 76]
assert solution.advantageCount([16, 30, 63, 64], [61, 64, 33, 31]) == [30, 16, 64, 63]
assert solution.advantageCount([4, 10, 13, 76, 86, 87], [73, 39, 70, 37, 91, 43]) == [10, 86, 13, 76, 4, 87]
assert solution.advantageCount([14, 19, 25, 82, 86], [43, 42, 86, 65, 73]) == [86, 82, 14, 25, 19]
assert solution.advantageCount([43, 56, 61, 74, 78], [78, 92, 84, 79, 95]) == [78, 56, 61, 74, 43]
assert solution.advantageCount([7, 10, 23, 44, 46, 92, 97, 100], [88, 43, 84, 35, 95, 86, 24, 96]) == [23, 92, 97, 46,
                                                                                                       10, 100, 44, 7]
assert solution.advantageCount([1, 8, 11, 21, 24, 38, 43, 49, 52, 55], [48, 4, 7, 33, 69, 10, 45, 68, 58, 100]) == [52,
                                                                                                                    8,
                                                                                                                    11,
                                                                                                                    38,
                                                                                                                    24,
                                                                                                                    21,
                                                                                                                    49,
                                                                                                                    43,
                                                                                                                    55,
                                                                                                                    1]
assert solution.advantageCount([21, 84, 98], [69, 97, 6]) == [84, 98, 21]
assert solution.advantageCount([15, 29, 32, 35, 43, 51, 80, 85, 92], [31, 26, 4, 72, 84, 15, 86, 89, 50]) == [35, 32,
                                                                                                              15, 80,
                                                                                                              85, 29,
                                                                                                              92, 43,
                                                                                                              51]
assert solution.advantageCount([9, 21, 38, 66, 88], [5, 73, 78, 33, 72]) == [9, 66, 21, 38, 88]
assert solution.advantageCount([3, 30, 82, 83, 86, 93], [93, 8, 67, 70, 65, 1]) == [93, 30, 83, 86, 82, 3]
assert solution.advantageCount([2, 5, 6, 21, 26, 62, 83, 85], [85, 72, 41, 27, 13, 20, 77, 4]) == [2, 85, 83, 62, 21,
                                                                                                   26, 6, 5]
assert solution.advantageCount([1, 16, 17, 35, 59, 98], [30, 74, 3, 35, 49, 86]) == [35, 17, 16, 59, 98, 1]
assert solution.advantageCount([46, 75], [91, 53]) == [46, 75]
assert solution.advantageCount([21, 61], [36, 81]) == [61, 21]
assert solution.advantageCount([1, 22, 23, 29, 44, 53, 61, 72, 84], [10, 51, 32, 46, 20, 25, 67, 59, 30]) == [22, 72,
                                                                                                              53, 61,
                                                                                                              23, 29, 1,
                                                                                                              84, 44]
assert solution.advantageCount([18, 21, 26, 37, 38, 62, 69], [62, 38, 84, 45, 9, 96, 41]) == [37, 62, 26, 38, 18, 21,
                                                                                              69]
assert solution.advantageCount([19, 26, 32, 43, 47, 60], [19, 24, 94, 63, 90, 12]) == [26, 32, 43, 60, 47, 19]
assert solution.advantageCount([6, 11, 23, 26, 35, 39, 43, 49, 73, 76], [13, 44, 24, 11, 53, 86, 55, 92, 28, 96]) == [
    26, 49, 35, 23, 73, 43, 76, 11, 39, 6]
assert solution.advantageCount([1, 5, 9, 29, 30, 56, 100], [84, 53, 22, 61, 67, 10, 49]) == [1, 100, 30, 9, 5, 29, 56]
assert solution.advantageCount([11, 21, 24, 74, 76, 89], [12, 55, 77, 82, 45, 29]) == [21, 89, 24, 11, 76, 74]
assert solution.advantageCount([31, 39], [25, 68]) == [31, 39]
assert solution.advantageCount([17, 33, 53, 77, 82, 96], [96, 8, 94, 59, 75, 70]) == [33, 17, 53, 77, 96, 82]
assert solution.advantageCount([67, 81, 96, 98], [5, 32, 51, 42]) == [67, 81, 98, 96]
assert solution.advantageCount([6, 63, 75, 95], [94, 45, 33, 89]) == [6, 75, 63, 95]
assert solution.advantageCount([7, 9, 16, 24, 61, 77, 80], [22, 68, 9, 34, 23, 29, 13]) == [61, 7, 16, 9, 77, 80, 24]
assert solution.advantageCount([39, 50, 68, 69, 73, 75, 92, 93], [72, 39, 41, 6, 59, 73, 54, 21]) == [92, 68, 69, 39,
                                                                                                      75, 93, 73, 50]
assert solution.advantageCount([51, 91, 97], [5, 70, 46]) == [51, 97, 91]
assert solution.advantageCount([9, 17, 41, 45, 58, 61, 72], [14, 19, 55, 58, 95, 91, 34]) == [17, 41, 58, 61, 9, 72, 45]
assert solution.advantageCount([8, 63, 98], [54, 47, 81]) == [98, 63, 8]
assert solution.advantageCount([38, 64, 75, 77, 86, 92, 96, 100], [16, 69, 88, 44, 51, 85, 31, 74]) == [38, 86, 100, 75,
                                                                                                        77, 96, 64, 92]
assert solution.advantageCount([13, 26, 45, 66, 85, 90], [20, 30, 21, 59, 45, 78]) == [26, 66, 45, 90, 85, 13]
assert solution.advantageCount([7, 35, 49, 51, 61, 81, 99], [22, 63, 9, 4, 88, 1, 27]) == [51, 81, 49, 35, 99, 7, 61]
assert solution.advantageCount([37, 53, 54, 58, 60, 70, 95], [79, 5, 54, 74, 88, 85, 99]) == [70, 37, 58, 95, 54, 60,
                                                                                              53]
assert solution.advantageCount([14, 30, 38, 51, 55], [24, 43, 23, 40, 67]) == [38, 55, 30, 51, 14]
assert solution.advantageCount([78, 79], [13, 52]) == [78, 79]
assert solution.advantageCount([29, 31, 50, 52, 76, 93], [29, 31, 42, 4, 95, 52]) == [31, 50, 52, 29, 93, 76]
assert solution.advantageCount([22, 64, 65, 78, 90, 93, 96], [95, 2, 85, 64, 43, 71, 44]) == [96, 22, 93, 78, 64, 90,
                                                                                              65]
assert solution.advantageCount([29, 31, 75], [16, 90, 99]) == [29, 75, 31]
assert solution.advantageCount([12, 27, 37, 77, 90], [88, 43, 44, 77, 25]) == [12, 77, 90, 37, 27]
assert solution.advantageCount([3, 35, 47, 81, 95], [44, 18, 33, 32, 15]) == [3, 47, 95, 81, 35]

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
