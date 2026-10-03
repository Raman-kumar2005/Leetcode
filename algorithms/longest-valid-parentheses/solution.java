class MyStack{
    int[] arr;
    int top;
    int size;

    public MyStack(int size){
        this.arr=new int[size];
        this.size=size;
        top=-1;

    }
    public void  push(int data){
        if (top+1==size){
            System.out.println("Stack overflow!");
            return;
        }
        top++;
        arr[top]=data;
    }
    public int pop(){
        if (top==-1){
            System.out.println("Stack underFlow!");
            return -1;

        }
        
        int item=arr[top];
        top--;
        return item;
    }
    
    public int peek(){
        if (top==-1){
            System.out.println("Stack Stack is Empty !");
            return -1;

            }
        
        int item=arr[top];
        
        return item;
    }
    public boolean isEmpty() {
        return top == -1;
    }
    
}

class Solution {
    public int longestValidParentheses(String s) {
        MyStack stack = new MyStack(s.length()+1);
        stack.push(-1);
        int max_len=0;
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i)=='('){
                stack.push(i);
            }else{
                int index=stack.pop();
                if (stack.isEmpty()){
                    stack.push(i);
                }else{
                    int current_len= i-stack.peek();
                    if (current_len>max_len){
                        max_len = current_len;
                    }
                }
            }
        }
        return max_len;
        
    }
}