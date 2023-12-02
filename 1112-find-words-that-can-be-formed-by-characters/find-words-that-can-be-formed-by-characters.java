class Solution {
    public int countCharacters(String[] words, String chars) {
        char a[]=chars.toCharArray();
        Arrays.sort(a);
        int f=0;
            for(int j=0;j<words.length;j++){
                char b[]=words[j].toCharArray();
                Arrays.sort(b);
                if(b.length>a.length){
                    continue;
                }
                    int c=0;
                    int p=0;
                for(int k=0;k<b.length;k++){
        for(int i=p;i<a.length;i++){
                    if(a[i]==b[k]){
                        c++;
                        p=i+1;
                        break;
                    }
                }
            }
                if(c==b.length){
                    f+=c;
                }
        }
        return f;
    }
}