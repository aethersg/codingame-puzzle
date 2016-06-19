import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        // game loop
        while (true) {
            Map <Integer,Integer> HeightMountain =  new HashMap<Integer,Integer>();
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain, from 9 to 0.
                HeightMountain.put(i,mountainH);
            }
            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            System.err.println("Debug messages..." + HeightMountain);
            int maxValue = Collections.max(HeightMountain.values());
            System.err.println("max value ..." + maxValue);
            Iterator it = HeightMountain.entrySet().iterator();
            while (it.hasNext()){
                Map.Entry pair = (Map.Entry)it.next();
                if ((int)pair.getValue() == maxValue){
                    System.out.println(pair.getKey());
                    break;
                }
            }
        }
    }
}