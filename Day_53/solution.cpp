class Solution {
  public:
// code here
    void reverseArray(vector<int> &arr) {
        
        int length = arr.size();
        
        
        int start = 0 ;
        int end = (length - 1) ; 
        while(start<end){
            int temp;
            //swap
            temp = arr[start];
            arr[start] = arr[end];
            arr[end]= temp;
            
            start++;
            end--;
            
        }
        
        
    }
};
