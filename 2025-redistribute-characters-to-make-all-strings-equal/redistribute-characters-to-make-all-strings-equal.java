class Solution {
    public boolean makeEqual(String[] words) {
        int n = words.length;
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0; i<n; i++){
            for(int j=0; j<words[i].length(); j++){
                char c = words[i].charAt(j);
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
        }
        for(char c : map.keySet()){
            if(map.get(c) % n != 0)
                return false;
        }
        return true;
    }
}