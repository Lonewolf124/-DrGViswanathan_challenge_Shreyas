class Solution {
  public:
    string addBinary(string& s1, string& s2) {
        size_t pos1 = s1.find('1');
        size_t pos2 = s2.find('1');
        s1 = (pos1 == string::npos) ? "0" : s1.substr(pos1);
        s2 = (pos2 == string::npos) ? "0" : s2.substr(pos2);

       
        if (s1.size() < s2.size()) {
            swap(s1, s2);
        }

        int n = s1.size(), m = s2.size();
        int carry = 0;
        string result = s1; // Use s1 as a base for result

        
        for (int i = n - 1, j = m - 1; i >= 0; i--) {
            int bit1 = s1[i] - '0';
            int bit2 = (j >= 0) ? (s2[j--] - '0') : 0;

            int sum = bit1 + bit2 + carry;
            result[i] = (sum % 2) + '0'; 
            carry = sum / 2;
        }

        
        if (carry > 0) {
            result = '1' + result;
        }

        return result;
    }
