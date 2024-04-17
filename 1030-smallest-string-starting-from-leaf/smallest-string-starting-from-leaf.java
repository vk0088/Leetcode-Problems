/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    StringBuilder smallest = null;
    public String smallestFromLeaf(TreeNode root)
    {
        helper(root,"");
        return smallest.toString();
    }
    public void helper(TreeNode node, String s)
    {
        if(node==null) return;
        if(node.left == null && node.right ==null)
        {
            s+=(char)(97+node.val);
            StringBuilder str = new StringBuilder(s);
            str.reverse();

            if(smallest == null)
            {
                smallest = str;
            }
            else if(str.compareTo(smallest)<0)
            {
                smallest = str;
            }
            else
            return;
        }
        s+=(char)(97+node.val);


        helper(node.left,s);
        helper(node.right,s);
    }
}