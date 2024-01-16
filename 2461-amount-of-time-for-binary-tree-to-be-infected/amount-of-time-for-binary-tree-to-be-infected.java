class Solution {
    class Pair{
        int node;
        int curTime;
        Pair(int node, int curTime){
            this.node = node;
            this.curTime = curTime;
        }
    }

    public int amountOfTime(TreeNode root, int start) {
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        build(root, map);

        HashSet<Integer> set = new HashSet<>();
        int max_time = Integer.MIN_VALUE;
        Stack<Pair> stack = new Stack<>();
        set.add(start);
        stack.push(new Pair(start, 0));

        while(!stack.isEmpty()){
            int node = stack.peek().node;
            int curTime = stack.peek().curTime;
            stack.pop();

            max_time = Math.max(max_time, curTime);

            List<Integer> list = map.get(node);
            if(list == null){
                return 0;
            }
            for(int i = 0; i < list.size(); i++){
                int l = list.get(i);
                if(!set.contains(l)){
                    stack.add(new Pair(l, curTime + 1));
                    set.add(l);
                }
            }
        }

        return max_time;
    }

    private void build(TreeNode root, 
                HashMap<Integer, List<Integer>> map){
        if(root == null){
            return;
        }

        if(root.left == null && root.right == null){
            return;
        }

        if(!map.containsKey(root.val)){
             map.put(root.val, new ArrayList<>());
        }

        List<Integer> cur = map.get(root.val);
        if(root.left != null){
            cur.add(root.left.val);
        }
        if(root.right != null){
            cur.add(root.right.val);
        }
        map.put(root.val, cur);

        if(root.left != null && !map.containsKey(root.left.val)){
            map.put(root.left.val, new ArrayList<>());
            List<Integer> cur_left = map.get(root.left.val);
            cur_left.add(root.val);
            map.put(root.left.val, cur_left);
        }

        if(root.right != null && !map.containsKey(root.right.val)){
            map.put(root.right.val, new ArrayList<>());
            List<Integer> cur_right = map.get(root.right.val);
            cur_right.add(root.val);
            map.put(root.right.val, cur_right);
        }

        build(root.left, map);
        build(root.right, map);
    }
}