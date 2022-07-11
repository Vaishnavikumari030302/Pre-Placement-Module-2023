class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(s, p):
            count = 0
            while p>=0 and count != 0 or s[p] == '#':
                count = count+1 if s[p] == '#' else count-1
                p -= 1
            return p

        p1, p2 = len(s)-1, len(t)-1
        while p1 >= 0 and p2 >= 0:
            # print(p1, p2, s[p1], t[p2])
            p1 = back(s, p1)
            p2 = back(t, p2)
            # print(p1, p2, s[p1], t[p2])
            # print()
            if (p1 < 0 and p2 >= 0) or (p1 >= 0 and p2 < 0) or p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
            p1 -= 1
            p2 -= 1
        p1 = back(s, p1) if p1 >= 0 else p1
        p2 = back(t, p2) if p2 >= 0 else p2
        return True if p1 < 0 and p2 < 0 else False

    # 智慧 算. . .
    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])