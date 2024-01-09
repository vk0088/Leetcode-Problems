class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<>();
        Map<String,Integer> wordFrequency = new HashMap<>();

        if (words.length==0 || s.length()==0) 
        return ans;
        
        int wordSize = words[0].length();
        int wordCount = words.length;
        int windowSize = wordSize * wordCount;

        for(String word : words)
        {
            wordFrequency.put(word,wordFrequency.getOrDefault(word,0)+1);
        }

        for (int i = 0; i < wordSize; i++) {
            int left = i, right = i, count = 0;
            Map<String, Integer> currentWindow = new HashMap<>();

            while (right + wordSize <= s.length()) {
                String currentWord = s.substring(right, right + wordSize);
                right += wordSize;

                if (wordFrequency.containsKey(currentWord)) {
                    currentWindow.put(currentWord, currentWindow.getOrDefault(currentWord, 0) + 1);
                    count++;

                    while (currentWindow.get(currentWord) > wordFrequency.get(currentWord)) {
                        String leftWord = s.substring(left, left + wordSize);
                        currentWindow.put(leftWord, currentWindow.get(leftWord) - 1);
                        count--;
                        left += wordSize;
                    }

                    if (count == wordCount) {
                        ans.add(left);
                    }
                } else {
                    currentWindow.clear();
                    count = 0;
                    left = right;
                }
            }
        }
        return ans;

    }
}