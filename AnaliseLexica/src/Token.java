
public class Token {
	public final int codigo;
	public String valor;
	
	public Token(int c,String v) {
		this.codigo= c;
		this.valor=v;
	}
	public Token(int c) {
		this(c,null);
	}
	
	
}
