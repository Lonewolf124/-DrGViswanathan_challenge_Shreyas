class Solution {
  public:
    int getSecondLargest(vector<int> &arr) {
        int max = arr[0];
        int smax = -1;
        for (int i =1 ;i<arr.size();i++){
            if (arr[i]>max ){
                smax = max;//updated second largest 
                max = arr[i];//updated largest
            
            }
            else if(arr[i]>smax && arr[i]<max){
                smax = arr[i];
            } 

        }
        return smax;
    }
};
