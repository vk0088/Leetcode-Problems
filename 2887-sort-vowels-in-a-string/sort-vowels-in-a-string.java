class Solution {
    public String sortVowels(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        map.put('a',97);
        map.put('e',101);
        map.put('i',105);
        map.put('o',111);
        map.put('u',117);
        map.put('A',65);
        map.put('E',69);
        map.put('I',73);
        map.put('O',79);
        map.put('U',85);

        ArrayList<Integer> idx = new ArrayList<>();
        ArrayList<Character> list = new ArrayList<>();

        for(int i=0; i<s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                list.add(s.charAt(i));
                idx.add(i);
            }
        }

        Collections.sort(list);
        char[] arr = s.toCharArray();
        for(int i=0; i<idx.size(); i++){
            arr[idx.get(i)] = list.get(i);
        }

        return new String(arr);
    }
}