class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        int lowest = prices[0], highest = prices[0], p = 0, index = 0;
        while (index < prices.size() - 1) {
            while (index < (prices.size() - 1) && prices[index] >= prices[index + 1]) {
                index++;
            }

            lowest = prices[index];

            while (index < (prices.size() - 1) && prices[index] <= prices[index + 1]) {
                index++;
            }

            highest = prices[index];
            p += (highest - lowest);
        }
        return p;
    }
};
