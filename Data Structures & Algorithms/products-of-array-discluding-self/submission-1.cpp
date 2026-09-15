class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        size_t zero_count = 0;
        int product = 1;
        for (auto& num:  nums){
            if (num){
                product *= num;
            }
            else {
                zero_count++;
            }
        }
        if (zero_count > 1){
            return vector<int>(nums.size());
        }
        vector<int> res(nums.size());
        for (int i = 0; i < nums.size(); i++){
            if (zero_count){
                if (nums[i] == 0){
                    res[i] = product;
                    return res;
                }
            }
            else{
                res[i] = product / nums[i];
            }
        }
        return res;
    }
};
