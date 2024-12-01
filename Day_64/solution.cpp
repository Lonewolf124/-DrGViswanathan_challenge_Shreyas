class Solution {
  public:
    // Function to find the smallest positive number missing from the array.
    int missingNumber(vector<int> &arr) {
        int n = arr.size();
        vector<bool> present(n, false);

        for (int i = 0; i < n; i++) {
            if (arr[i] > 0 && arr[i] <= n) {
                present[arr[i] - 1] = true;
            }
        }

        for (int i = 0; i < n; i++) {
            if (!present[i]) {
                return i + 1;
            }
        }

        return n + 1;
    }
