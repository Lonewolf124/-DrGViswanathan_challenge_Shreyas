class Solution {
  public:
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(vector<int> &arr) {
     
        long long maxEndingHere = arr[0];
        long long maxSoFar = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            maxEndingHere = max((long long)arr[i], maxEndingHere + arr[i]);
            maxSoFar = max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }
};
