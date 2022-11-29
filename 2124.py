public class Solution {
    public bool CheckString(string s) {
        char[] letter = new char[s.Length];
        letter = s.ToCharArray();
        
            for(int i =0; i<letter.Length;i++){
                try{
                    if((letter[i] == 'b') && (letter[i+1] =='a')){
                        return false;
                    }
                }
                catch(IndexOutOfRangeException e){
                   return true; 
                }
            }
        return true;
    }
}
