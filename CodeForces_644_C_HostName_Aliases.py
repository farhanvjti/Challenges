from sys import maxsize as m
from itertools import product as P
from operator import itemgetter as ig 
class Solution:
    def bazinga(self,N,p):
        pass 

if __name__=='__main__':
    n = int(input())
    g = {}  #grouping on the basis of hostname 
    for i in range(n):
        urls =input()
        url=urls[7:]
        if '/' in url:
            s = url.index('/')
            hn = url[:s]
        else:
            hn = url
        if hn in g:
            if urls not in g[hn]:  #to add only unique 
                g[hn] += (urls,)
        else:
            g[hn] = (urls,)
    res = {}        #grouping on number of hostnames queries
    for k,v in g.items():
        q = len(v)  #num of queries
        
        if q in res:    res[q]+=('http://'+k,)
        else:           res[q]=('http://'+k,)
    Del = []
    for k,v in res.items():
        if len(v)<=1:   Del.append(k)
    for i in range(len(Del)):   del res[Del[i]] 
    ans = sorted(res.items(), key=ig(1))
    print(len(ans))
    for a in ans:
        print(' '.join(a[1]))
    
'''
C. Hostname Aliases
time limit per test
5 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

There are some websites that are accessible through several different addresses. For example, for a long time Codeforces was accessible with two hostnames codeforces.com and codeforces.ru.

You are given a list of page addresses being queried. For simplicity we consider all addresses to have the form http://<hostname>[/<path>], where:

    <hostname> — server name (consists of words and maybe some dots separating them),
    /<path> — optional part, where <path> consists of words separated by slashes. 

We consider two <hostname> to correspond to one website if for each query to the first <hostname> there will be exactly the same query to the second one and vice versa — for each query to the second <hostname> there will be the same query to the first one. Take a look at the samples for further clarifications.

Your goal is to determine the groups of server names that correspond to one website. Ignore groups consisting of the only server name.

Please note, that according to the above definition queries http://<hostname> and http://<hostname>/ are different.
Input

The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of page queries. Then follow n lines each containing exactly one address. Each address is of the form http://<hostname>[/<path>], where:

    <hostname> consists of lowercase English letters and dots, there are no two consecutive dots, <hostname> doesn't start or finish with a dot. The length of <hostname> is positive and doesn't exceed 20.
    <path> consists of lowercase English letters, dots and slashes. There are no two consecutive slashes, <path> doesn't start with a slash and its length doesn't exceed 20. 

Addresses are not guaranteed to be distinct.
Output

First print k — the number of groups of server names that correspond to one website. You should count only groups of size greater than one.

Next k lines should contain the description of groups, one group per line. For each group print all server names separated by a single space. You are allowed to print both groups and names inside any group in arbitrary order.
Examples
Input

10
http://abacaba.ru/test
http://abacaba.ru/
http://abacaba.com
http://abacaba.com/test
http://abacaba.de/
http://abacaba.ru/test
http://abacaba.de/test
http://abacaba.com/
http://abacaba.com/t
http://abacaba.com/test

Output

1
http://abacaba.de http://abacaba.ru 

Input

14
http://c
http://ccc.bbbb/aba..b
http://cba.com
http://a.c/aba..b/a
http://abc/
http://a.c/
http://ccc.bbbb
http://ab.ac.bc.aa/
http://a.a.a/
http://ccc.bbbb/
http://cba.com/
http://cba.com/aba..b
http://a.a.a/aba..b/a
http://abc/aba..b/a

Output

2
http://cba.com http://ccc.bbbb 
http://a.a.a http://a.c http://abc
'''
        
        
