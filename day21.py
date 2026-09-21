def nextGreaterElement( l ):
        stack=[]
        arr=[-1]*len(l)
        for i in range(len(l)-1,-1,-1):

            while stack and stack[-1]<=l[i]:
                stack.pop()
            if stack:
                arr[i]=stack[-1]
            
            
            
            stack.append(l[i])
            
        print(arr)


nextGreaterElement([1,3,4,2])