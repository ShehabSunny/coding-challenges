class Solution:
    def reverse(self, x: int) -> int: 
        if x >= 0 :
            r =  int(str(x)[::-1])
        else:
            r = int(str(x*-1)[::-1]) * -1

        mina = -2**31  
        maxa = 2**31 - 1
        if r not in range(mina, maxa): 
            return 0 
        else: 
            return r

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1534236469))