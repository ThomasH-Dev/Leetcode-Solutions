class Solution:
    def numSplits(self, s: str) -> int:
        if len(s)== 1:
            return 0
        left = [0]*len(s)
        
        right = [0]*len(s)
        seenL = set()
        seenR = set()
        count = 0
        for i in range(len(s)):
            j = len(s) - i-1
            
            if s[i] not in seenL:
                seenL.add(s[i])
                left[i] = left[i-1] + 1
            else:
                left[i] = left[i-1] 
            print(j)  
            
            
            if s[j] not in seenR:
                seenR.add(s[j])
                if j == len(s) - 1:
                    right[j] += 1
                else:
                    right[j] = right[j+1] + 1
            else:
                right[j] = right[j+1] 
            
        for i in range(len(left) -1):
            
            if left[i] == right[i+1]:
                
                count +=1
        print(left)
        print(len(seenL))
        print (right)
        return count
        
        