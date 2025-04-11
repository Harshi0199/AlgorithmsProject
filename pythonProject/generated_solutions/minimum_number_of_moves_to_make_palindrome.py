# Problem 2193: Minimum Number of Moves to Make Palindrome
# Difficulty: Hard
# Description:
# <p>You are given a string <code>s</code> consisting only of lowercase English letters.</p>
# <p>In one <strong>move</strong>, you can select any two <strong>adjacent</strong> characters of <code>s</code> and swap them.</p>
# <p>Return <em>the <strong>minimum number of moves</strong> needed to make</em> <code>s</code> <em>a palindrome</em>.</p>
# <p><strong>Note</strong> that the input will be generated such that <code>s</code> can always be converted to a palindrome.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;aabb&quot;
# <strong>Output:</strong> 2
# <strong>Explanation:</strong>
# We can obtain two palindromes from s, &quot;abba&quot; and &quot;baab&quot;. 
# - We can obtain &quot;abba&quot; from s in 2 moves: &quot;a<u><strong>ab</strong></u>b&quot; -&gt; &quot;ab<u><strong>ab</strong></u>&quot; -&gt; &quot;abba&quot;.
# - We can obtain &quot;baab&quot; from s in 2 moves: &quot;a<u><strong>ab</strong></u>b&quot; -&gt; &quot;<u><strong>ab</strong></u>ab&quot; -&gt; &quot;baab&quot;.
# Thus, the minimum number of moves needed to make s a palindrome is 2.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;letelt&quot;
# <strong>Output:</strong> 2
# <strong>Explanation:</strong>
# One of the palindromes we can obtain from s in 2 moves is &quot;lettel&quot;.
# One of the ways we can obtain it is &quot;lete<u><strong>lt</strong></u>&quot; -&gt; &quot;let<u><strong>et</strong></u>l&quot; -&gt; &quot;lettel&quot;.
# Other palindromes such as &quot;tleelt&quot; can also be obtained in 2 moves.
# It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
# 	<li><code>s</code> consists only of lowercase English letters.</li>
# 	<li><code>s</code> can be converted to a palindrome using a finite number of moves.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        cs = list(s)
        ans, n = 0, len(s)
        i, j = 0, n - 1
        while i < j:
            even = False
            for k in range(j, i, -1):
                if cs[i] == cs[k]:
                    even = True
                    while k < j:
                        cs[k], cs[k + 1] = cs[k + 1], cs[k]
                        k += 1
                        ans += 1
                    j -= 1
                    break
            if not even:
                ans += n // 2 - i
            i += 1
        return ans

def generate_test_case():
    # Initialize the solution class
    solution = Solution()
    
    # Generate random strings for s
    s_length = random.randint(1, 10)
    s = random.choices("abcdefghijklmnopqrstuvwxyz", k=s_length)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.minMovesToMakePalindrome(s)

    return s, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        s, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minMovesToMakePalindrome(s) == expected_result
        print(f'assert solution.minMovesToMakePalindrome("{"".join(s)}") == {expected_result}')
        test_case_generator_results.append(f'assert solution.minMovesToMakePalindrome("{"".join(s)}") == {expected_result}')
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

# --------------------------------------
# Test Cases:
assert solution.minMovesToMakePalindrome("xfrhuro") == 5
assert solution.minMovesToMakePalindrome("c") == 0
assert solution.minMovesToMakePalindrome("ptudjnx") == 3
assert solution.minMovesToMakePalindrome("ouazvv") == 6
assert solution.minMovesToMakePalindrome("i") == 0
assert solution.minMovesToMakePalindrome("cbio") == 3
assert solution.minMovesToMakePalindrome("x") == 0
assert solution.minMovesToMakePalindrome("mwbk") == 3
assert solution.minMovesToMakePalindrome("zjuexp") == 5
assert solution.minMovesToMakePalindrome("byngs") == 2
assert solution.minMovesToMakePalindrome("jwujmxw") == 4
assert solution.minMovesToMakePalindrome("lhmjees") == 7
assert solution.minMovesToMakePalindrome("ldhlspue") == 9
assert solution.minMovesToMakePalindrome("egmtgmta") == 10
assert solution.minMovesToMakePalindrome("gomqxpvjkp") == 12
assert solution.minMovesToMakePalindrome("af") == 1
assert solution.minMovesToMakePalindrome("nbeh") == 3
assert solution.minMovesToMakePalindrome("prfp") == 1
assert solution.minMovesToMakePalindrome("fzho") == 3
assert solution.minMovesToMakePalindrome("efh") == 1
assert solution.minMovesToMakePalindrome("qps") == 1
assert solution.minMovesToMakePalindrome("xs") == 1
assert solution.minMovesToMakePalindrome("lawjs") == 2
assert solution.minMovesToMakePalindrome("qlyd") == 3
assert solution.minMovesToMakePalindrome("wlhs") == 3
assert solution.minMovesToMakePalindrome("lsrbfffd") == 10
assert solution.minMovesToMakePalindrome("whd") == 1
assert solution.minMovesToMakePalindrome("tepnnsww") == 12
assert solution.minMovesToMakePalindrome("ycaj") == 3
assert solution.minMovesToMakePalindrome("huvpi") == 2
assert solution.minMovesToMakePalindrome("omz") == 1
assert solution.minMovesToMakePalindrome("hxehlyhd") == 6
assert solution.minMovesToMakePalindrome("uj") == 1
assert solution.minMovesToMakePalindrome("vaxmcb") == 5
assert solution.minMovesToMakePalindrome("dvlzwtzrfo") == 13
assert solution.minMovesToMakePalindrome("atzrt") == 2
assert solution.minMovesToMakePalindrome("ifqnyz") == 5
assert solution.minMovesToMakePalindrome("wdmqhqkhe") == 12
assert solution.minMovesToMakePalindrome("wi") == 1
assert solution.minMovesToMakePalindrome("afj") == 1
assert solution.minMovesToMakePalindrome("padfchbgon") == 9
assert solution.minMovesToMakePalindrome("ox") == 1
assert solution.minMovesToMakePalindrome("dl") == 1
assert solution.minMovesToMakePalindrome("uojkw") == 2
assert solution.minMovesToMakePalindrome("ekjd") == 3
assert solution.minMovesToMakePalindrome("f") == 0
assert solution.minMovesToMakePalindrome("jnisv") == 2
assert solution.minMovesToMakePalindrome("iqxcc") == 3
assert solution.minMovesToMakePalindrome("cq") == 1
assert solution.minMovesToMakePalindrome("ldeokcc") == 5
assert solution.minMovesToMakePalindrome("vv") == 0
assert solution.minMovesToMakePalindrome("axhwito") == 3
assert solution.minMovesToMakePalindrome("dahw") == 3
assert solution.minMovesToMakePalindrome("seiqvnh") == 3
assert solution.minMovesToMakePalindrome("bdyetkhqc") == 4
assert solution.minMovesToMakePalindrome("ooykju") == 7
assert solution.minMovesToMakePalindrome("sjksm") == 2
assert solution.minMovesToMakePalindrome("rezdzd") == 6
assert solution.minMovesToMakePalindrome("seduqgo") == 3
assert solution.minMovesToMakePalindrome("a") == 0
assert solution.minMovesToMakePalindrome("wmbmfsh") == 6
assert solution.minMovesToMakePalindrome("jm") == 1
assert solution.minMovesToMakePalindrome("lhl") == 0
assert solution.minMovesToMakePalindrome("o") == 0
assert solution.minMovesToMakePalindrome("m") == 0
assert solution.minMovesToMakePalindrome("hfzwcqrfq") == 8
assert solution.minMovesToMakePalindrome("yf") == 1
assert solution.minMovesToMakePalindrome("ldc") == 1
assert solution.minMovesToMakePalindrome("grdpzucx") == 7
assert solution.minMovesToMakePalindrome("obhvoxdby") == 7
assert solution.minMovesToMakePalindrome("fiessogsv") == 7
assert solution.minMovesToMakePalindrome("xkwngkaciu") == 12
assert solution.minMovesToMakePalindrome("uraybzr") == 3
assert solution.minMovesToMakePalindrome("rtvd") == 3
assert solution.minMovesToMakePalindrome("asllcdbubz") == 18
assert solution.minMovesToMakePalindrome("dqrzkehl") == 7
assert solution.minMovesToMakePalindrome("fpbpgpillx") == 16
assert solution.minMovesToMakePalindrome("qmccpjq") == 4
assert solution.minMovesToMakePalindrome("muoavbuzv") == 8
assert solution.minMovesToMakePalindrome("kcrbc") == 2
assert solution.minMovesToMakePalindrome("cafunbsr") == 7
assert solution.minMovesToMakePalindrome("ty") == 1
assert solution.minMovesToMakePalindrome("fzdujdqesp") == 13
assert solution.minMovesToMakePalindrome("enuoasni") == 7
assert solution.minMovesToMakePalindrome("ehydjakdra") == 14
assert solution.minMovesToMakePalindrome("svqa") == 3
assert solution.minMovesToMakePalindrome("mvxblnbw") == 9
assert solution.minMovesToMakePalindrome("cofzgg") == 6
assert solution.minMovesToMakePalindrome("sadvermm") == 9
assert solution.minMovesToMakePalindrome("jzr") == 1
assert solution.minMovesToMakePalindrome("dvdhzbsw") == 10
assert solution.minMovesToMakePalindrome("qwtp") == 3
assert solution.minMovesToMakePalindrome("mwwjra") == 7
assert solution.minMovesToMakePalindrome("mkgh") == 3
assert solution.minMovesToMakePalindrome("bmszdqkp") == 7
assert solution.minMovesToMakePalindrome("xa") == 1
assert solution.minMovesToMakePalindrome("elu") == 1
assert solution.minMovesToMakePalindrome("fpwcm") == 2
assert solution.minMovesToMakePalindrome("ocmy") == 3
assert solution.minMovesToMakePalindrome("njjnp") == 2

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
