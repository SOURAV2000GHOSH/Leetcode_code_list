//use for calculation
class Person{
    String name;
    int height;
    public Person(String name,int height){
        this.name=name;
        this.height=height;
    }
}

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // we are storing name and height for storing 
        List<Person> store = new ArrayList<>();
        for(int i=0;i<names.length;i++){
            store.add(new Person(names[i],heights[i]));
        }
        
        // sorting in decending order of height
        Collections.sort(store,(a,b)-> b.height-a.height);
        
        // taking all names from sorted list and adding in ans that will only return names
        String[] ans= new String[names.length];
        for(int i=0;i<names.length;i++){
            ans[i]=store.get(i).name;
        }
        return ans;
    }
}