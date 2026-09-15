func hasDuplicate(nums []int) bool {
    var vistos []int;
    for i := range(len(nums)){
        for j :=  range(len(vistos)){
            if nums[i] == vistos[j]{
                return true;
            }
        }
        vistos = append(vistos, nums[i])
    } 
    return false;
}
