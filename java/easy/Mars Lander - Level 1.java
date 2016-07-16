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

        int surfaceN = in.nextInt(); // the number of points used to draw the surface of Mars.

        int[] surfaceX = new int[surfaceN];
        int[] surfaceY = new int[surfaceN];

        for (int i = 0; i < surfaceN; i++) {
            int landX = in.nextInt(); // X coordinate of a surface point. (0 to 6999)
            int landY = in.nextInt(); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
            surfaceX[i] = landX;
            surfaceY[i] = landY;
        }

        // game loop
        while (true) {
            int X = in.nextInt();
            int Y = in.nextInt();
            int hSpeed = in.nextInt(); // the horizontal speed (in m/s), can be negative.
            int vSpeed = in.nextInt(); // the vertical speed (in m/s), can be negative.
            int fuel = in.nextInt(); // the quantity of remaining fuel in liters.
            int rotate = in.nextInt(); // the rotation angle in degrees (-90 to 90).
            int power = in.nextInt(); // the thrust power (0 to 4).

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            int groundY = -1;
            for (int i = 0; (i < surfaceN && groundY == -1); i++)
            {
                if (surfaceX[i] <= X && X <= surfaceX[i + 1])
                {
                    groundY = surfaceY[i];
                }
            }

            double vdY = vSpeed - 8.555;
            double vY = Y - 36.665 + 5*vSpeed;
            long t = Math.round((-40 - vdY) / 0.289);
            if (vY + t*(vdY+0.289*(1+t)/2) > groundY) {
                System.out.println("0 0");
            }else {
                System.out.println("0 4");
            }
            // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
        }
    }
}