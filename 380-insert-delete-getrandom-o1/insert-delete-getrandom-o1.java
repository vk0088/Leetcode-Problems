class RandomizedSet {
    public Map<Integer, Integer> map;
    public List<Integer> list;
    public RandomizedSet() {
        map = new HashMap<Integer, Integer>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        else map.put(val, 0);
        return true;
    }
    
    public boolean remove(int val) {
        if (map.containsKey(val)) map.remove(val);
        else return false;
        return true;
    }
    
    public int getRandom() {
        list = new ArrayList<Integer>(map.keySet());
        Random random = new Random();
        return list.get(new Random().nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */