public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Hashtable ht = new Hashtable();
        int index = 0;
        int[] outArray = new int[2];
        foreach(int item in nums){
            ht.Add(item, index);
        }
        
        if(ht.ContainsKey(needVal)){
            outArray[0]=index;
            outArray[1]=(int)ht[needVal];
            goto finish;
        }
            index++;
        finish: return outArray;
    }
}
