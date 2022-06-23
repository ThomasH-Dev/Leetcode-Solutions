class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0, len(A) -1
        while True:
            midA = (l+r) //2
            midB = (half - midA) -2 
            
            leftA = A[midA] if midA >= 0 else float("-infinity")
            rightA = A[midA + 1] if midA +1 < len(A) else float("infinity")
            leftB = B[midB] if midB >= 0 else float("-infinity")
            rightB = B[midB + 1] if midB + 1< len(B) else float("infinity")
            
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA,leftB) + min(rightA,rightB)) / 2
            elif leftA > rightB:
                r = midA - 1
            else:
                l = midA + 1
            
            
            
            
        
        