#Write a program to determine whether an input string x is a substring of another 
#input string y.  (For example, "bat"  is  a  substring  of  "abate",  but  not  of  "beat".)  
#You  may use  any  language  you  like

def substring(s,t):
    if s.count(t) >= 1:
        return 1
    return 0

print(substring("abte","bat"))
