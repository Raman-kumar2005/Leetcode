import java.util.HashMap;
import java.util.Map;

class MyStack {  
    char[] stack; 
    int top;

    public MyStack(int capacity) {
        this.stack = new char[capacity];
        top = -1;
    }

    public void push(char data) {
        if ((top + 1) == stack.length) {
            System.out.println("Stack overflow");
            return;
        }
        top++;
        stack[top] = data;
    }

    public char pop() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return '\0'; 
        }
        char item = stack[top]; 
        top--;
        return item;
    }
    
    public char peek() {
        if (top == -1) {
            return '\0'; 
        }
        return stack[top];
    }
    
    public boolean isEmpty() {
        return top == -1;
    }
}

class Solution {
    public boolean isValid(String s) { 
        MyStack stack = new MyStack(s.length()); 
        
        Map<Character, Character> matching = new HashMap<>();
        matching.put(')', '('); 
        matching.put(']', '[');
        matching.put('}', '{');
        
        for (int i = 0; i < s.length(); i++) { 
            char current = s.charAt(i); 
            
            
            if (current == '(' || current == '{' || current == '[') {
                stack.push(current);
            } else {
                if (stack.isEmpty() || stack.peek() != matching.get(current)) {
                    return false;
                }
                stack.pop(); 
            }
        }
        
        return stack.isEmpty();
    }
}