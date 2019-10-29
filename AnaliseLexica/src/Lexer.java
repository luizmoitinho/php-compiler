import  java.util.ArrayList;

public class Lexer {
	ArrayList<Token> tokens =  new ArrayList<Token>();
	Token token;
	Buffer buffer;
	public Lexer(String lexema){
		this.buffer =   new Buffer(lexema);
	}
	public Token proximoToken() {
		Character c;
		int estado =0; 			// indica o estado atual - AFD - AFND
		int ultimoFinal =-1;  	// nulo, ou seja nao existe
		buffer.marcarInicio();
		//percorre toda a string
		for(int i=0;i<buffer.lexema.length();i++) {
			c =  buffer.proximo();
			switch(estado) {
				case 0:
					//Ao entrar neste case, temos o primeiro caractere a ser lido
					// q0 -> q1
					if(delimitador(c))
						estado = 29;
					else if(c=='i') {
						ultimoFinal =  1;
						estado = 1;
						buffer.marcarUltimo();
					}
					// Verifica se é uma letra
					else if(Character.isLetter(c) && c!='i')
						this.setID(estado,ultimoFinal);
					
					else if(c =='<') {
						estado = 4;
						ultimoFinal =4;
						buffer.marcarUltimo();
					}
					else if(c =='=') {
						estado =6;
						ultimoFinal =6;
						buffer.marcarUltimo();
					}
					else if(c =='>') {
						estado =8;
						ultimoFinal =8;
						buffer.marcarUltimo();
					}
					// Verifica se é um digito
					//Integer.parseInt(String.valueOf(digits.charAt(i)));
					else if(Character.isDigit(c)){
						ultimoFinal =  10;
						estado = 10;
						buffer.marcarUltimo();
					}
					else if(c==';'){
						ultimoFinal =  29;
						estado = 29;
						buffer.marcarUltimo();
					}
				break;
				case 1:
					if(c=='f') {
						ultimoFinal = 2;
						estado  =2;
						buffer.marcarUltimo();
						token = new Token(2,"if");

					}
					else if(Character.isLetter(c) && c!='f')
						this.setID(estado,ultimoFinal);
					
					break;
				case 2:
					if(this.validarID(c))
						this.setID(estado,ultimoFinal);
					break;
				case 3:
					if(this.validarID(c))
						this.setID(estado,ultimoFinal);
					break;
				case 4:
					if(c =='=') {
						estado =5;
						ultimoFinal =5;
						buffer.marcarUltimo();
						token = new Token(5,"LE");
					}
					break;
				case 5:
					if(c =='>') {
						estado =7;
						ultimoFinal =7;
						buffer.marcarUltimo();
						token = new Token(7,"NEQ");
					}
					break;
				case 8:
					if(c =='=') {
						estado =9;
						ultimoFinal =9;
						buffer.marcarUltimo();
						token = new Token(9,"GE");
					}
					break;
				case 10:
					if(c =='.') {
						estado =11;
						ultimoFinal =11;
						buffer.marcarUltimo();
						token = new Token(9,"DOT");
					}
					else if(c =='E') {
						estado =13;
						ultimoFinal =13;
						buffer.marcarUltimo();
						token = new Token(13,"E");
					}
					break;
				case 11:
					if(Character.isDigit(c)) {
						estado =12;
						ultimoFinal =12;
						buffer.marcarUltimo();
						token = new Token(12,"NUMS");
					}
					break;
				case 12:
					if(Character.isDigit(c)) {
						estado =12;
						ultimoFinal =12;
						buffer.marcarUltimo();
						token = new Token(12,"NUMS");
					}
					else if(c =='E') {
						estado =13;
						ultimoFinal =13;
						buffer.marcarUltimo();
						token = new Token(13,"E");
					}
					break;
				case 13:
					if(c=='-' || c=='+') {
						estado =14;
						ultimoFinal =14;
						buffer.marcarUltimo();
						token = new Token(14,"OP");
					}
					else if(Character.isDigit(c)) {
						estado =15;
						ultimoFinal =15;
						buffer.marcarUltimo();
						token = new Token(15,"NUM_E");
					}
					
					break;
				case 14:
					if(Character.isDigit(c)) {
						estado =15;
						ultimoFinal =15;
						buffer.marcarUltimo();
						token = new Token(15,"NUM_E");
					}
	
					break;
				case 29:
					if(!delimitador(c)) {
						buffer.retrair(1);
						buffer.marcarInicio();
						estado=0;
					}	
					break;
			}
		}
		return token;
	}
	private boolean validarID(Character c) {
		if(Character.isLetter(c) || Character.isDigit(c)) {
			return true;
		}
		else
			return false;
		
	}
	private void setID(int estado,int ultimoFinal) {
			ultimoFinal = 3;
			estado = 3 ;
			buffer.marcarUltimo();
	}
	
	private boolean delimitador(int codigo) {
		return codigo ==';'?  true :  false;
	}
	


}
