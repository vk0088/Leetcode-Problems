class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        var dx = Math.abs(sx - fx);
        var dy = Math.abs(sy - fy);

        var dist = Math.max(dx, dy);

        return dist != 0 && t >= dist || dist == 0 && t != 1;
    }
}