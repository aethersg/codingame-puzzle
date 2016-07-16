import java.util.*;
import java.io.*;
import java.math.*;
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        in.nextLine();
        String temps = in.nextLine(); // the n temperatures expressed as integers ranging from -273 to 5526
        int min_temp = 0;

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        if (n == 0) {
            int result = n;
            System.out.println(result);
        } else {
            String [] temp_array = temps.split(" ");
            for (String t:temp_array){
                if ( (min_temp ==0) || (Math.abs(Integer.parseInt(t)) < Math.abs(min_temp)) || ((Integer.parseInt(t) == -min_temp) &&(Integer.parseInt(t) > 0) )){
                    min_temp = Integer.parseInt(t);
                }
            }
            System.out.println(min_temp);
        }

    }
}