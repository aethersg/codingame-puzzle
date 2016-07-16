import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    static  final char ZERO_CHAR = '0';
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String MESSAGE = in.nextLine();

        StringBuilder binaryMsg = new StringBuilder("");

        for (char c :MESSAGE.toCharArray()){
            String binaryChar = Integer.toBinaryString(c);
            for (int i = binaryChar.length(); i < 7; i++) {
                binaryMsg.append(ZERO_CHAR);
            }
            binaryMsg.append(binaryChar);
        }
        char previous = '2';
        int count = 0;
        for (char c : binaryMsg.toString().toCharArray()) {
            if(c != previous){
                for (int i = 0; i < count; i++) {
                    System.out.print(ZERO_CHAR);
                }
                if (count != 0){
                    System.out.print(" ");
                }
                System.out.print((c== ZERO_CHAR) ? "00 ":"0 ");
                count = 1;
            }else{
                count++;
            }
            previous = c;

        }
        for (int i = 0; i < count ; i++) {
            System.out.print("0");
        }
    }
}