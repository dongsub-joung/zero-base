class Solution {
    public int solution(int n, int price) {
        int free=(int) n / 10; 
        return (n - free) * price;
    }
}
