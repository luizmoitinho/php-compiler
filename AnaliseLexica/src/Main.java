import java.util.Scanner;
public class Main {
	public static void main(String Args[]) {
		Buffer buffer =  new Buffer("if(x==10)");
		System.out.println(buffer.proximo());
		System.out.println(buffer.proximo());
		
	}
}
