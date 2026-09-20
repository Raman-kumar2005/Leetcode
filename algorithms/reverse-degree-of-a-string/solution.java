class Solution {
    public int reverseDegree(String s) {
        
        int sum=0;
        for (int i=0; i<s.length(); i++){

            int position =26;
            for (char ch= 'a'; ch<='z'; ch++){
                if (s.charAt(i)==ch){
                    // int temp=1;
                    sum+=((1+i)*position);
                }
                position--;
            }
    }
    return sum;
    }
}