# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    result = ""
    i = 0


    while i < len(s1):
        if s1[i] in s2:
            temp = ""
            j = 1
            while temp in s2:
                if j >= len(s1):
                    if len(temp) > len(result) or (len(temp) == len(result) and temp <result):
                        result = temp
                
                temp += s1[j]
