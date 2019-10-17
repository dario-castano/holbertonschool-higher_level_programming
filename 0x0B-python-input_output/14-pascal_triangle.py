#!/usr/bin/python3


def pascal_triangle(n):
    """A very cool pascal triangle"""
    ans = []
    if n <= 0:
        return ans
    ans.append([1])
    if n == 1:
        return ans
    ans.append([1, 1])
    if n == 2:
        return ans
    for i in range(2, n):
        newlist = []
        newlist.append(1)
        fill = [ans[i-1][k] + ans[i-1][k+1] for k in range(len(ans) - 1)]
        newlist += fill
        newlist.append(1)
        ans.append(newlist)
    return ans
