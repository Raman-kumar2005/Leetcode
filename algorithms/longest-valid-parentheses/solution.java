class Solution {
    
    public List<String> generateParenthesis(int n) {
        List<String> result =new ArrayList<>();
        backtrack(n, n, "", result);
        return result;
        
        
    }
    public void backtrack(int open, int close, String s, List<String> result){
        
            if (open==0 && close==0){
                result.add(s);
                return;
            }
            if (open>0){
                backtrack(open-1,close,s+"(", result);
            }
            if (open<close){
                backtrack(open,close-1,s+")", result);

            }
    }

            
}