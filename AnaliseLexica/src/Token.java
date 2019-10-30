
public class Token {
	protected final int codigo;
	protected String valor;
	
	public Token(int c,String v) {
		this.codigo= c;
		this.valor=v;
	}
	public Token(int c) {
		this(c,null);
	}

	public String toString() {
		return 	"Token:\n"
				+ "<"+this.codigo+","+this.valor+">";

	}
}
