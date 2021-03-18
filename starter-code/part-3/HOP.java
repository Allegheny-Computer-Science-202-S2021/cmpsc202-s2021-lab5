import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
public class HOP {
    public static List<Integer> prepareData(List<Integer> childrens, int count){
        /*
        Data is prepared by inserting random numbers 
        starting from 1 - number of childrens. 
        Please refer to slides for the problem definiton.
        */
        for (int i = 0; i < count; i++){
                childrens.add(i+1);
        }
        Collections.shuffle(childrens);
        return childrens;
    }  
    public static int findWinner(List<Integer> childrens, int steps){
        int res = 0;
        /*
        Add your logic below to compute the winner 
        by applying the variatio of the Josephus solution 
        using Queue ADT. */
        


        return res;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the no of childrens:");
        int child_count = scan.nextInt();
        System.out.println("Enter the no of steps:");
        int steps = scan.nextInt();
        
        List<Integer> childs_initialized = new ArrayList<Integer>(); 
        List<Integer> childs_populated = prepareData(childs_initialized,child_count);

        // a set of days and their respective prices. 
        /* does a random distribution of prices.
        */
        /* Implement the computeSoan method, so as to 
        get the correct results.*/
        int winner = findWinner(childs_populated, steps);

        /* The lines below will print the output. 
        Do not uncomment these lines.  */
        System.out.println("Children:\t" + childs_populated);   
        System.out.println("No of childrens:\t" + child_count);   
        System.out.println("No of steps:\t" + steps);   
        System.out.println("Winner:\t" + winner);   
        
    }   
}
