import java.util.*;
import java.io.*;
import java.math.*;
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    static  final char DOT = '.';
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt(); // Number of elements which make up the association table.
        int Q = in.nextInt(); // Number Q of file names to be analyzed.

        Map mapping = new HashMap();
        for (int i = 0; i < N; i++) {
            String EXT = in.next(); // file extension
            String MT = in.next(); // MIME type.
            mapping.put(EXT.toLowerCase(),MT);
        }
        in.nextLine();
        for (int i = 0; i < Q; i++) {
            String FNAME = in.nextLine(); // One file name per line.
            int position = FNAME.toLowerCase().lastIndexOf(DOT);
            String ext = (position ==-1)?"":FNAME.toLowerCase().substring(position+1,FNAME.toLowerCase().length());
            System.out.println((String)(mapping.getOrDefault(ext,"UNKNOWN")));
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
    }
}