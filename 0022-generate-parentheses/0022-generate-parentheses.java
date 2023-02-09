class Solution {
    public List<String> generateParenthesis(int n) {
        
 List<String> list=new ArrayList<String>();

     Fun(n,"",list,0,0);


return list;
    }

    void Fun(int size,String temp,List<String> list,int open,int close)
    {
        if((open==close)&& (close==size))
        {
            list.add(temp);
            return;
        }

        if(open==close)
        Fun(size,temp+"(",list,open+1,close);

        else if (open > close && open <size)
        {
            Fun(size,temp+"(",list,open+1,close);
            Fun(size,temp+")",list,open,close+1);
        }

        else if (open == size && close < size)
       Fun(size,temp+")",list,open,close+1);

    }
}