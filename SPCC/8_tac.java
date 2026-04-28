import java.util.*;

/**
 * Experiment No. 5
 * Aim: To generate Three Address Code (TAC) for the given program.
 *
 * Supports arithmetic expressions with +, -, *, / and handles operator precedence.
 * Generates temporary variables (t1, t2, ...) for intermediate results.
 */
public class tac {

    // Token types
    static final int NUM   = 0;
    static final int ID    = 1;
    static final int PLUS  = 2;
    static final int MINUS = 3;
    static final int MUL   = 4;
    static final int DIV   = 5;
    static final int LPAREN = 6;
    static final int RPAREN = 7;
    static final int ASSIGN = 8;
    static final int EOF   = 9;

    // ── Lexer ────────────────────────────────────────────────────────────────

    static String input;
    static int    pos;
    static int    tokenType;
    static String tokenValue;

    static void nextToken() {
        // skip whitespace
        while (pos < input.length() && input.charAt(pos) == ' ') pos++;

        if (pos >= input.length()) { tokenType = EOF; tokenValue = ""; return; }

        char ch = input.charAt(pos);

        if (Character.isDigit(ch)) {
            StringBuilder sb = new StringBuilder();
            while (pos < input.length() && Character.isDigit(input.charAt(pos)))
                sb.append(input.charAt(pos++));
            tokenType  = NUM;
            tokenValue = sb.toString();
        } else if (Character.isLetter(ch) || ch == '_') {
            StringBuilder sb = new StringBuilder();
            while (pos < input.length() &&
                   (Character.isLetterOrDigit(input.charAt(pos)) || input.charAt(pos) == '_'))
                sb.append(input.charAt(pos++));
            tokenType  = ID;
            tokenValue = sb.toString();
        } else {
            pos++;
            switch (ch) {
                case '+': tokenType = PLUS;   tokenValue = "+"; break;
                case '-': tokenType = MINUS;  tokenValue = "-"; break;
                case '*': tokenType = MUL;    tokenValue = "*"; break;
                case '/': tokenType = DIV;    tokenValue = "/"; break;
                case '(': tokenType = LPAREN; tokenValue = "("; break;
                case ')': tokenType = RPAREN; tokenValue = ")"; break;
                case '=': tokenType = ASSIGN; tokenValue = "="; break;
                default:
                    System.err.println("Unknown character: " + ch);
                    nextToken();
            }
        }
    }

    // ── TAC generation state ─────────────────────────────────────────────────

    static int              tempCount = 0;
    static List<String>     tacCode   = new ArrayList<>();

    static String newTemp() { return "t" + (++tempCount); }

    static void emit(String code) { tacCode.add(code); }

    // ── Recursive-descent parser (returns the operand holding the value) ─────

    // expression → ID '=' expression
    //            | addExpr
    static String parseExpression() {
        // peek: if next token is ID followed by '=', treat as assignment
        int savedPos   = pos;
        int savedType  = tokenType;
        String savedVal = tokenValue;

        if (tokenType == ID) {
            String lhs = tokenValue;
            nextToken();
            if (tokenType == ASSIGN) {
                nextToken();                       // consume '='
                String rhs = parseAddExpr();
                emit(lhs + " = " + rhs);
                return lhs;
            } else {
                // not an assignment – roll back by re-initialising from saved state
                // (simple trick: reset and re-lex up to current pos)
                pos       = savedPos;
                tokenType = savedType;
                tokenValue = savedVal;
            }
        }
        return parseAddExpr();
    }

    // addExpr → mulExpr ( ('+' | '-') mulExpr )*
    static String parseAddExpr() {
        String left = parseMulExpr();
        while (tokenType == PLUS || tokenType == MINUS) {
            String op = tokenValue;
            nextToken();
            String right = parseMulExpr();
            String tmp   = newTemp();
            emit(tmp + " = " + left + " " + op + " " + right);
            left = tmp;
        }
        return left;
    }

    // mulExpr → unary ( ('*' | '/') unary )*
    static String parseMulExpr() {
        String left = parseUnary();
        while (tokenType == MUL || tokenType == DIV) {
            String op = tokenValue;
            nextToken();
            String right = parseUnary();
            String tmp   = newTemp();
            emit(tmp + " = " + left + " " + op + " " + right);
            left = tmp;
        }
        return left;
    }

    // unary → '-' unary | primary
    static String parseUnary() {
        if (tokenType == MINUS) {
            nextToken();
            String operand = parseUnary();
            String tmp = newTemp();
            emit(tmp + " = -" + operand);
            return tmp;
        }
        return parsePrimary();
    }

    // primary → '(' expression ')' | ID | NUM
    static String parsePrimary() {
        if (tokenType == LPAREN) {
            nextToken();             // consume '('
            String val = parseAddExpr();
            if (tokenType == RPAREN) nextToken(); // consume ')'
            return val;
        } else if (tokenType == ID || tokenType == NUM) {
            String val = tokenValue;
            nextToken();
            return val;
        } else {
            System.err.println("Unexpected token: " + tokenValue);
            nextToken();
            return "?";
        }
    }

    // ── Main ─────────────────────────────────────────────────────────────────

    static void generate(String expr) {
        input     = expr.trim();
        pos       = 0;
        tempCount = 0;
        tacCode   = new ArrayList<>();
        nextToken();
        parseExpression();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("TAC Generator. Type 'exit' to quit.");
        while (true) {
            System.out.print("Enter expression: ");
            String line = sc.nextLine().trim();
            if (line.equalsIgnoreCase("exit")) break;
            if (line.isEmpty()) continue;
            generate(line);
            System.out.println("TAC:");
            for (String tac : tacCode) System.out.println(tac);
        }
        sc.close();
    }
}
