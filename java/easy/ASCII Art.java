import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    static final char START_CHAR = 'a';
    static final char END_CHAR = 'z';
    static final char DELIMITER_CHAR = END_CHAR + 1;

    public static void printhar(int l, int w, char c,String[] array){
        int start = (c-START_CHAR)* w;
        int end = start+w;
        System.out.print(array[l].substring(start,end));
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        int H = in.nextInt();
        in.nextLine();
        String T = in.nextLine();
        String text = T.toLowerCase();

        String[] rowArray = new String[H];
        for (int i = 0; i < H; i++) {
            String ROW = in.nextLine();
            rowArray[i]=ROW;
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        for (int i = 0; i < H; i++) {
            for (char c : text.toCharArray()){
                if(START_CHAR <= c && c <= END_CHAR){
                    printhar(i,L,c,rowArray);
                }else{
                    printhar(i,L,DELIMITER_CHAR,rowArray);
                }
            }
            System.out.print("\n");
        }
    }
}