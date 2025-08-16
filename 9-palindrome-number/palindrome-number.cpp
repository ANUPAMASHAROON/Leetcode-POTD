class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return false;
        long num = x;
        long ans = 0;
        while(num != 0)
        {
            int rem = num % 10;
            ans = ans*10 + rem;
            num /= 10;
        }
        return ans == x;
    }
};