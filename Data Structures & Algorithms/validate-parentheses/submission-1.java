class Solution {
    public boolean isValid(String s) {
        Stack<Character> st  = new Stack<>();
        HashMap<Character,Character> map = new HashMap<>();

        map.put('(', ')');
        map.put('[',']');
        map.put('{', '}');

        for(char c : s.toCharArray()){
            if(map.containsKey(c)){
                st.push(map.get(c));
            }
            else if (!st.isEmpty() && st.peek() == c){
                st.pop();
            }
            else{
                return false;
            }
        }
        return st.isEmpty();
    }
}
