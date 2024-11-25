class Solution {
  public:
 
    int maximumProfit(vector<int> &stockPrices) {
        if (stockPrices.empty()) return 0;
        
        int lowestPrice = stockPrices[0], maxProfit = 0;
        for (int index = 0; index < stockPrices.size(); index++) {
            if (stockPrices[index] < lowestPrice) {
                lowestPrice = stockPrices[index];
            } else {
                int currentProfit = stockPrices[index] - lowestPrice;
                if (currentProfit > maxProfit) {
                    maxProfit = currentProfit;
                }
            }
        }
        return maxProfit;
    }
};
