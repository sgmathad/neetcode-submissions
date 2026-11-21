class Solution {
    public int[] getConcatenation(int[] nums) {
        int size = nums.length;
        int[] result = new int[size * 2];

        for(int i=0; i<result.length;i++)
        {
            result[i] = nums[i%size];
        }
        return result;
    }
}