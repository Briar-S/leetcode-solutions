using System.Linq;

public class Solution {
    public string IntToRoman(int num) {
        int[] digits = num.ToString().ToCharArray().Select(a => a - '0').ToArray();
        Hashtable ones = new Hashtable();
        ones.Add(1, "I");
        ones.Add(5, "V");
        ones.Add(9, "IX");
        Hashtable tens = new Hashtable();
        tens.Add(1, "X");
        tens.Add(5, "L");
        tens.Add(9, "XC");
        Hashtable hundreds = new Hashtable();
        hundreds.Add(1, "C");
        hundreds.Add(5, "D");
        hundreds.Add(9, "CM");
        Hashtable thousands = new Hashtable();
        thousands.Add(1, "M");
        List<Hashtable> allHt = new List<Hashtable>();
        allHt.Add(thousands);
        allHt.Add(hundreds);
        allHt.Add(tens);
        allHt.Add(ones);
        int stPlace = 4-digits.Length;
        int minPlace = stPlace+1;
        if(stPlace == 4){minPlace=3;}
        if(stPlace ==0){minPlace = 1;}
        String[] tempStr = new String[4];
        int placeholder = 0;
        foreach(int digit in digits){ 
            Hashtable tempHt = allHt[stPlace];
            if(digit >=1 && digit <=3){
                    for(int i=0;i<digit;i++){
                        tempStr[placeholder] += tempHt[1];
                    }
            }            
            else if (digit == 4){
                tempStr[placeholder] = tempHt[1].ToString() + tempHt[5];
            }
            
            else if (digit >=5 && digit <=8){
                tempStr[placeholder] += tempHt[5];
                for(int i=0;i<digit-5;i++){
                    tempStr[placeholder] += tempHt[1];
                }                   
            }
            else if(digit==9){
                tempStr[placeholder] += tempHt[9];
            }
            
            stPlace++;
            placeholder++;
            
        }
        return tempStr[0]+ tempStr[1]+ tempStr[2]+ tempStr[3];
    }
}
