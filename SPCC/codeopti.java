import java.util.*;

public class codeopti {

    static void optimize(List<String> lines) {
        // seen: maps "rhs" -> first temp that computed it
        Map<String, String> seen = new LinkedHashMap<>();
        List<String> result = new ArrayList<>();

        for (String line : lines) {
            line = line.replaceAll("\\s+", "");
            if (line.isEmpty()) continue;

            int eq = line.indexOf('=');
            if (eq == -1) { result.add(line); continue; }

            String lhs = line.substring(0, eq);
            String rhs = line.substring(eq + 1);

            if (!seen.containsValue(lhs)) {
                // lhs hasn't appeared as a replacement yet
                if (!seen.containsKey(rhs)) {
                    seen.put(rhs, lhs);
                    result.add(lhs + " = " + rhs);
                }
                // else it's a duplicate — skip
            }
        }

        System.out.println("Optimized Code:");
        for (String r : result) System.out.println(r);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("CSE Optimizer. Enter TAC lines, blank line to optimize, 'exit' to quit.");
        while (true) {
            List<String> lines = new ArrayList<>();
            System.out.println("Enter TAC:");
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.equalsIgnoreCase("exit")) { sc.close(); return; }
                if (line.trim().isEmpty()) break;
                lines.add(line);
            }
            if (!lines.isEmpty()) optimize(lines);
        }
    }
}

