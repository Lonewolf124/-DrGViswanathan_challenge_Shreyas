int circularSubarraySum(vector<int>& arr) {
        int t = 0, mx = 0, mn = 0; // t = total sum, mx = current max, mn = current min
        int gmx = arr[0], gmn = arr[0]; // gmx = global max, gmn = global min
        
        for (int i = 0; i < arr.size(); i++) {
            mx = max(mx + arr[i], arr[i]); // Max subarray sum ending at i
            mn = min(mn + arr[i], arr[i]); // Min subarray sum ending at i
            gmx = max(gmx, mx); // Update global max
            gmn = min(gmn, mn); // Update global min
            t += arr[i]; // Total sum
        }

        if (gmn == t) {
            return gmx; // All elements are negative
        } else {
            return max(gmx, t - gmn); // Maximum of non-circular and circular sum
        }
    }
