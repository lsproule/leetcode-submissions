func containsNearbyDuplicate(nums []int, k int) bool {
    var seen []int 
    for _, num := range nums{
        for _, val :=  range seen {
            if val == num {
                return true
            }
        }
        seen = append(seen, num)
        if len(seen) > k {
            seen = seen[1:]
        }
    }
    return false
}
