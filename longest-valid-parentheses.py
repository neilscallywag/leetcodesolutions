def longestValidParentheses(s):
    ans, stack = 0, [-1]
    print("Start stack",stack)
    print("Start ans",ans)
    for i, c in enumerate(s):
        print("i=",i,"c=",c)
        if c == ")":
            print("prepop",stack)
            stack.pop()
            print("afterpop",stack)
            if stack:
                print("ifstack", stack)
                
                print("i=", i)
                print("stack[-1]=", stack[-1])
                print("i-stack[-1]=", i-stack[-1])
                ans = max(ans, i - stack[-1])
                print("ans=",ans)
                continue
        print("preappend",stack)    
        stack.append(i)
        print("postappend",stack)
    return ans

print(longestValidParentheses(")()(((("))


       


