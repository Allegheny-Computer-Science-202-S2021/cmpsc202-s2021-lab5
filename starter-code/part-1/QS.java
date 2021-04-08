import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
import java.util.ArrayList;
public class QS {
    public static ArrayList<Integer> prepareData(ArrayList<Integer> data, int size){
        /*
        Data is prepared by inserting random values 
        between 1 and 100. Data items may be assumed to 
        be repeated. 
        Please refer to lab spec for the problem definiton.
        */
        // what is our range?
        int min = 1;
        // create instance of Random class
        Random randomNum = new Random();
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i=0; i<size; i++) {
            int val = min + randomNum.nextInt(99);
            list.add(val);
        }
        Collections.shuffle(list);
    
        for (int i=0; i<size; i++) {
             data.add(list.get(i));
        }
    

        return data;
    }  
    public static ArrayList<Integer> start_sort(ArrayList<Integer> data){
        /*
        Add your logic below to sort the array.
        and store the final output in data.
        Create a separate method for Partition 
        use this method for main sorting procedure. */
    

        return data;
    }

    public static void main(String[] args) {
        System.out.println("Enter the no of items:");
        Scanner scan = new Scanner(System.in);
        int items = scan.nextInt();
        ArrayList<Integer> empty = new ArrayList<Integer>();

        ArrayList<Integer> data = prepareData(empty, items);

        System.out.print("Unsorted:\t");
        System.out.println(data);   
        
        /* Implement the Quick Sort methods, so as to 
        get the correct results.*/
        ArrayList<Integer> sorted_array = start_sort(data);
        
        /* The two lines below will print the output. 
        Do not uncomment these lines.  */
        System.out.print("Sorted:\t\t");
        System.out.println(sorted_array);   
        
        
    }   
}
