/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int road = in.nextInt(); // the length of the road before the gap.
        int gap = in.nextInt(); // the length of the gap.
        int platform = in.nextInt(); // the length of the landing platform.

        // game loop
        while (true) {
            int speed = in.nextInt(); // the motorbike's speed.
            int coordX = in.nextInt(); // the position on the road of the motorbike.

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");

            int distance_left = road + gap;
            int distance_gap = gap + 1;
            // A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
            if ((coordX >= distance_left) || (speed > distance_gap)) {
                System.out.println("SLOW");
            } else if (speed <= gap) {
                System.out.println("SPEED");
            } else if (coordX + speed >= distance_left) {
                System.out.println("JUMP");
            } else {
                System.out.println("WAIT");
            }
        }
    }
}