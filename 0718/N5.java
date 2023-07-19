class Solution {
    public int solution(String S) {
        int answer = 0;
        int s= Integer.parseInt(S);
        while(s !=0 ){
            if(s % 2 != 0)
                s-= 1;
            else
                s= s << 1;
            answer+=1;
        }
        return answer;
    }
}