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
    public List<Integer> postorderTraversal(TreeNode root) {
        
        // Check if the root is null
        if(root == null){
            // If the root is null, return an empty ArrayList
            return new ArrayList<Integer>();
        }

        // Create a new ArrayList to store the values obtained in a post-order traversal
        ArrayList<Integer> ans = new ArrayList<>();

        // Recursively perform a post-order traversal on the left subtree and add the obtained values to the ArrayList
        ans.addAll(postorderTraversal(root.left));

        // Recursively perform a post-order traversal on the right subtree and add the obtained values to the ArrayList
        ans.addAll(postorderTraversal(root.right));

        // Add the value of the root to the ArrayList
        ans.add(root.val);

    // Return the ArrayList containing all the values obtained in the post-order traversal
    return ans;
    }
}