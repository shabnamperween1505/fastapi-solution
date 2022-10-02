class Solution:
    def isValid(self, s: str) -> bool:
        closure = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for i in range(len(s)):
            if(s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
            else:
                if(closure[str(stack[-1])] == s[i]):
                    stack.pop()
                else:
                    return False
        if (len(stack) != 0):
            return False     
        return True


# print("{[(){}]}", Solution.isValid(self= Solution, s="{[(){}]}"))

def test_1():
    assert True == Solution.isValid(self= Solution, s="([])")

def test_fail_1():
    assert False == Solution.isValid(self= Solution, s="([)")

def test_2():
    assert True == Solution.isValid(self= Solution, s="([{}])")

def test_fail_2():
    assert False == Solution.isValid(self= Solution, s="([{])")

def test_3():
    assert True == Solution.isValid(self= Solution, s="([{}])")

def test_fail_3():
    assert False == Solution.isValid(self= Solution, s="([{}")

def test_4():
    assert True == Solution.isValid(self= Solution, s="([{}])")

def test_fail_4():
    assert False == Solution.isValid(self= Solution, s="([})")

def test_5():
    assert True == Solution.isValid(self= Solution, s="{[(){}]}")

def test_fail_5():
    assert False == Solution.isValid(self= Solution, s="{[(){})}")

def test_empty_string():
    assert True == Solution.isValid(self= Solution, s="")


