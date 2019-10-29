import java.util.Scanner;
public class Main {
	public static void main(String Args[]) {
		Lexer lexer =  new Lexer("if(x==10)");
		System.out.println(lexer.proximoToken().valor);
		
	}
}
