import java.io.IOException;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class lexicalAnalyser{


    public enum TokenType{
        KEYWORD, IDENTIFIER, LITERAL, OPERATOR, PUNCTUATION, WHITESPACE, COMMENT, UNKNOWN
    }

    public class Token{
        private TokenType tokenType;
        private String value;

        public Token(TokenType type, String value){
            this.tokenType = type;
            this.value = value;
        }

        public TokenType getType(){
            return tokenType;
        }

        public String getValue(){
            return value;
        }

        @Override
        public String toString() {
            return "Token{" + "type=" + tokenType + ", value='" + value + '\'' + '}';
        }
    }

    public class Lexer{
        private String input;
        private int currentPosition;

        public Lexer(String input){
            this.input = input;
            this.currentPosition = 0;
        }

        public List<Token> tokenise(){
            
            List<Token> tokens = new ArrayList<>();

            while (currentPosition < input.length()) {
                char currentChar = input.charAt(currentPosition);
                if(Character.isWhitespace(currentChar)){
                    currentPosition++;
                    continue;
                }

                Token token = nextToken();
                if(token != null){
                    tokens.add(token);
                } else {
                    throw new RuntimeException("Unknown character: " + currentChar);
                }
            }

            return tokens;
        }

        private Token nextToken(){
            
            if (currentPosition >= input.length()) {
                return null;
            }

            String[] tokenPatterns = {
                "if|else|while|for",         // Keywords
                "[a-zA-Z_][a-zA-Z0-9_]*",    // Identifiers
                "\\d+",                      // Literals
                "[+-/*=<>!]",                // Operators
                "[.,;(){}]",                 // Punctuation
            };

            TokenType[] tokenTypes = {
                TokenType.KEYWORD,
                TokenType.IDENTIFIER,
                TokenType.LITERAL,
                TokenType.OPERATOR,
                TokenType.PUNCTUATION,
            };

            for(int i = 0 ; i < tokenPatterns.length ; i++){
                
                Pattern pattern = Pattern.compile("^" + tokenPatterns[i]);
                Matcher matcher = pattern.matcher(input.substring(currentPosition));

                if(matcher.find()){
                    String value = matcher.group();
                    currentPosition += value.length();
                    return new Token(tokenTypes[i], value);
                }

                
            }

            return null;



        }
    }

    public static void main(String[] args){

        String code = "float interest = p*n*r;";
        exp1 e = new exp1();
        Lexer lexer = e.new Lexer(code);
        List<Token> tokens = lexer.tokenise();

        for (Token token : tokens) {
            System.out.println(token);
        }
    }

}