import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    static final String ID = "id";
    static final String NAME = "name";
    static final String ADD = "add";
    static final String NO = "no";
    static final String LONG = "lon";
    static final String LATI = "lat";

    static float convert_to_float(String value){
        return Float.parseFloat(value.replace(",","."));
    }

    static double return_distance(String dlon, String dlat, String lon,String lat){
        float fdlon = convert_to_float(dlon);
        float fdlat = convert_to_float(dlat);
        float flon = convert_to_float(lon);
        float flat = convert_to_float(lat);
        double x = (fdlon - flon) * Math.cos((flat + fdlat)/2);
        double y = (fdlat-flat);
        return (Math.sqrt(x*x + y*y) * 6371);
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String LON = in.next();
        String LAT = in.next();
        int N = in.nextInt();
        in.nextLine();
        List<Map<String,String>> defibArray = new ArrayList<Map<String,String>>();
        for (int i = 0; i < N; i++) {
            String DEFIB = in.nextLine();
            String[] defibData = DEFIB.split(";");
            Map def_map = new HashMap();
            def_map.put(ID,defibData[0]);
            def_map.put(NAME,defibData[1]);
            def_map.put(ADD,defibData[2]);
            def_map.put(NO,defibData[3]);
            def_map.put(LONG,defibData[4]);
            def_map.put(LATI,defibData[5]);
            defibArray.add(def_map);
        }

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");
        Map nearestDefMap = new HashMap();
        double minDist = Double.MAX_VALUE;
        if (defibArray.size() >1){
            for (Map<String,String> df:defibArray) {
                double distance = return_distance(df.get(LONG),df.get(LATI),LON,LAT);
                if (distance < minDist){
                    minDist = distance;
                    nearestDefMap = df;
                }
            }
        }else{
            nearestDefMap = defibArray.get(0);
        }
        System.out.println(nearestDefMap.get(NAME));
    }
}