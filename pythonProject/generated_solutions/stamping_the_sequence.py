# Problem 936: Stamping The Sequence
# Difficulty: Hard
# Description:
# <p>You are given two strings <code>stamp</code> and <code>target</code>. Initially, there is a string <code>s</code> of length <code>target.length</code> with all <code>s[i] == &#39;?&#39;</code>.</p>
# <p>In one turn, you can place <code>stamp</code> over <code>s</code> and replace every letter in the <code>s</code> with the corresponding letter from <code>stamp</code>.</p>
# <ul>
# 	<li>For example, if <code>stamp = &quot;abc&quot;</code> and <code>target = &quot;abcba&quot;</code>, then <code>s</code> is <code>&quot;?????&quot;</code> initially. In one turn you can:
#     <ul>
#     	<li>place <code>stamp</code> at index <code>0</code> of <code>s</code> to obtain <code>&quot;abc??&quot;</code>,</li>
#     	<li>place <code>stamp</code> at index <code>1</code> of <code>s</code> to obtain <code>&quot;?abc?&quot;</code>, or</li>
#     	<li>place <code>stamp</code> at index <code>2</code> of <code>s</code> to obtain <code>&quot;??abc&quot;</code>.</li>
#     </ul>
#     Note that <code>stamp</code> must be fully contained in the boundaries of <code>s</code> in order to stamp (i.e., you cannot place <code>stamp</code> at index <code>3</code> of <code>s</code>).</li>
# </ul>
# <p>We want to convert <code>s</code> to <code>target</code> using <strong>at most</strong> <code>10 * target.length</code> turns.</p>
# <p>Return <em>an array of the index of the left-most letter being stamped at each turn</em>. If we cannot obtain <code>target</code> from <code>s</code> within <code>10 * target.length</code> turns, return an empty array.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> stamp = &quot;abc&quot;, target = &quot;ababc&quot;
# <strong>Output:</strong> [0,2]
# <strong>Explanation:</strong> Initially s = &quot;?????&quot;.
# - Place stamp at index 0 to get &quot;abc??&quot;.
# - Place stamp at index 2 to get &quot;ababc&quot;.
# [1,0,2] would also be accepted as an answer, as well as some other answers.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> stamp = &quot;abca&quot;, target = &quot;aabcaca&quot;
# <strong>Output:</strong> [3,0,1]
# <strong>Explanation:</strong> Initially s = &quot;???????&quot;.
# - Place stamp at index 3 to get &quot;???abca&quot;.
# - Place stamp at index 0 to get &quot;abcabca&quot;.
# - Place stamp at index 1 to get &quot;aabcaca&quot;.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
# 	<li><code>stamp</code> and <code>target</code> consist of lowercase English letters.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:

from collections import deque
import random
import string
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        slen, tlen = len(stamp), len(target)
        res = []
        
        s_covers = set()   # create permutation of cover on characters in stamp
        for i in range(slen):
            for j in range(slen - i):
                s_covers.add('#' * i + stamp[i:slen-j] + '#' * j)
		# print(s_covers)
		
        done = '#' * tlen
		
        p = tlen - slen 
        while target != done:
            
            found = False
            for i in range(p, -1, -1):
                if target[i: i+slen] in s_covers:
                    target = target[:i] + '#' * slen + target[i+slen:]  # add the mask to the target
                    res.append(i)
                    found = True
            if not found:   # if we cannot find where to put the stamp, return empty array
                return []
        
        return res[::-1]

def generate_test_case():
    solution = Solution()
    
    # Generate random strings
    stamp_length = random.randint(1, 10)
    stamp = ''.join(random.choices(string.ascii_lowercase, k=stamp_length))
    
    target_length = random.randint(stamp_length, 10)
    target = ''.join(random.choices(string.ascii_lowercase, k=target_length))

    expected_result = solution.movesToStamp(stamp, target)
    print("abc")
    print(expected_result)
    return stamp, target, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        stamp, target, expected_result = generate_test_case()
        solution = Solution()
        assert solution.movesToStamp(stamp, target) == expected_result
        if len(expected_result) != 0:
            print(f"assert solution.movesToStamp('{stamp}', '{target}') == {expected_result}")
            test_case_generator_results.append(f"assert solution.movesToStamp('{stamp}', '{target}') == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)


# --------------------------------------
# Test Cases:


if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
