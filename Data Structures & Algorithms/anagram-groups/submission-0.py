class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tstrs = []
        st = []
        t = []

        for i in range(len(strs)):
            tstrs.append("".join(sorted(strs[i])))

        # sort both lists together to keep the link
        paired = sorted(zip(tstrs, strs))  
        
        k = paired[0][0]
        t.append(paired[0][1])

        for i in range(1, len(paired), 1):
            if paired[i][0] == k:
                t.append(paired[i][1])
            else:
                st.append(t)
                t = []              # reset t
                k = paired[i][0]   # fix: use sorted key not original word
                t.append(paired[i][1])

        st.append(t)   # fix: save the last group

        return st      # fix: return st not tstrs