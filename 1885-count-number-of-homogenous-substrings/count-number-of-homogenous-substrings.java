class Solution {
    public int countHomogenous(String s) {
      int hcount = 0;
		int rule = (int) (Math.pow(10, 9) + 7);
		int start = 0;

		for (int i = 1; i < s.length(); i++) {
			hcount++;
			if (s.charAt(start) != s.charAt(i)) {
				start = i;
			} else {
				int j = i - start;
				hcount = (hcount + j)%rule;
			}
		}
		return (hcount + 1) % rule;  
    }
}