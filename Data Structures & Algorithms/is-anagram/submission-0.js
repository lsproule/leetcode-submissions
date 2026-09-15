class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
      if (s.length !== t.length) {
        return false
      }
    
      const cuenta = new Map()
    
      for (let i = 0; i < s.length; i++) {
        const s_count = 1 + (cuenta.get(s[i]) || 0);
        cuenta.set(s[i], s_count)
        const t_count = -1 + (cuenta.get(t[i]) || 0);
        cuenta.set(t[i], t_count)
    
        if (s_count == 0) {
          cuenta.delete(s[i])
        }
    
        if (t_count == 0) {
          cuenta.delete(t[i])
        }
      }
    
      return cuenta.size == 0
  }
}
