class Solution {
  public:
    int getMinDiff(vector<int> &arr, int k) {
        
        int n = arr.size();
        sort(arr.begin(), arr.end());
        int a = arr[n - 1] - arr[0];
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] - k < 0) {
                continue;
            }
            int Min = min(arr[0] + k, arr[i] - k);
            int Max = max(arr[i - 1] + k, arr[n - 1] - k);
            a = min(a, Max - Min);
        }
    return a;
    }
    
};
