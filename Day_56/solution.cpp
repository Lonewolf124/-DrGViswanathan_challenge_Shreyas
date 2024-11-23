
class Solution {
    public:
    vector<int> findMajority(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return {};

        int c1 = INT_MIN, c2 = INT_MIN, c3 = 0, c4 = 0;

        for (int num : arr) {
            if (num == c1) {
                c3++;
            } else if (num == c2) {
                c4++;
            } else if (c3 == 0) {
                c1 = num;
                c3 = 1;
            } else if (c4 == 0) {
                c2 = num;
                c4 = 1;
            } else {
                c3--;
                c4--;
            }
        }

        c3 = c4 = 0;
        for (int num : arr) {
            if (num == c1) c3++;
            else if (num == c2) c4++;
        }

        vector<int> result;
        if (c3 > n / 3) result.push_back(c1);
        if (c4 > n / 3) result.push_back(c2);

        sort(result.begin(), result.end());
        return result;
    }
};
