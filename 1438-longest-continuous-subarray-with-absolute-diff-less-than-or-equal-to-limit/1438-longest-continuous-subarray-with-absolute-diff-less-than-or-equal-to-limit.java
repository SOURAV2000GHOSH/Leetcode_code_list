class Solution {
    static int[] maxDeque;
    static int[] minDeque;
    static int maxHead;
    static int maxTail;
    static int minHead;
    static int minTail;

    public int longestSubarray(int[] nums, int limit) {
        int n = nums.length;
        maxDeque = new int[n];
        minDeque = new int[n];
        maxHead = 0;
        maxTail = 0;
        minHead = 0;
        minTail = 0;

        int res = 0;
        int r = 0;
        for (int l = 0; l < n; l++) {
            while (r < n && withinLimit(nums, nums[r], limit)) {
                addToLast(nums, r);
                r++;
            }
            res = Math.max(res, r - l);
            removeExpired(l);
        }
        return res;
    }

    public boolean withinLimit(int[] nums, int num, int limit) {
        int max = maxHead < maxTail ? Math.max(nums[maxDeque[maxHead]], num) : num;
        int min = minHead < minTail ? Math.min(nums[minDeque[minHead]], num) : num;
        return max - min <= limit;
    }

    public void addToLast(int[] nums, int r) {
        while (maxHead < maxTail && nums[maxDeque[maxTail - 1]] <= nums[r]) {
            maxTail--;
        }
        maxDeque[maxTail++] = r;

        while (minHead < minTail && nums[minDeque[minTail - 1]] >= nums[r]) {
            minTail--;
        }
        minDeque[minTail++] = r;
    }

    public void removeExpired(int l) {
        if (maxDeque[maxHead] == l) {
            maxHead++;
        }
        if (minDeque[minHead] == l) {
            minHead++;
        }
    }
}