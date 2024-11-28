class Solution {
  public:
 
    int maxProduct(vector<int> &arr) {
       
        if (arr.empty()) return 0;
    
        int maxProduct = arr[0];
        int Max = arr[0];
        int Min = arr[0];
    
        
        for (size_t i = 1; i < arr.size(); ++i) {
           
            if (arr[i] < 0) {
                swap(Max, Min);
            }
    
         
            Max = max(arr[i], Max * arr[i]);
            Min = min(arr[i], Min * arr[i]);
    
           
            maxProduct = max(maxProduct, Max);
        }
    
        return maxProduct;
    }
};
