public class Solution {
    public int RotatedDigits(int n) {
        int count=0;
        for(int j=1;j<=n;j++){
            string i = j.ToString();
            if(i.Contains("3") || i.Contains("4") || i.Contains("7")){}
            else if(!i.Contains("2") && !i.Contains("5") && !i.Contains("6") && !i.Contains("9")){}
            else{count++;}
        }
        return count;
    }
}
