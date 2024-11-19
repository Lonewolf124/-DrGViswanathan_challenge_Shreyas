class Solution {
  public:
    void pushZerosToEnd(vector<int>& arr) {
        // code here
        
        int index=0;
        
        
        for(int i=0;i<arr.size();i++){
            if (arr[i]!=0){
                
                arr[index]=arr[i];
                index+=1;
                
            }
        }
        while(index<arr.size()){
            arr[index] = 0;
            index+=1;
        }
        
        
    }
    
};
