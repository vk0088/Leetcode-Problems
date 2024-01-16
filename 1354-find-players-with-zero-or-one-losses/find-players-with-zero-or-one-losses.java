class Solution {
    public List<List<Integer>> findWinners(int[][] arr) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        res.add(new ArrayList<>());
        int a[] = new int[100001];// winner
        int b[] = new int[100001];// loser
        for (int p[] : arr) {
            a[p[0]]++;
            b[p[1]]++;
        }
        for (int i = 0; i < a.length; i++) {
            if (a[i] > 0 && b[i] == 0) {
                res.get(0).add(i);
            }
        }
        for (int i = 0; i < b.length; i++) {
            if (b[i] == 1) {
                res.get(1).add(i);
            }
        }
        return res;
    }
}