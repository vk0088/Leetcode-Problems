class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> map = new TreeMap<>();
        List<List<Integer>> list = new ArrayList<>();
        for (int n[] : matches) {
            if (!map.containsKey(n[0]))
                map.put(n[0], 0);
            map.put(n[1], map.getOrDefault(n[1], 0) + 1);
        }
        List<Integer> win = new ArrayList<>();
        List<Integer> lost = new ArrayList<>();
        for (int n : map.keySet()) {
            if (map.get(n) == 0)
                win.add(n);
            if (map.get(n) == 1)
                lost.add(n);
        }
        list.add(win);
        list.add(lost);
        return list;
    }
}