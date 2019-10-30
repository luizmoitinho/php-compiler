

public class Lexer {
	Token token;
	Buffer buffer;
	Simbolo simbolo = new Simbolo();
	
	public Lexer(String lexema){
		this.buffer =   new Buffer(lexema);
	}
	
	public Token proximoToken() {
		Character c;
		int estado =0; 			// indica o estado atual - AFD - AFND
		int ultimoEstadoFinal =-1,i=buffer.posAtual;  	// nulo, ou seja nao existe
		buffer.marcarInicio();
		// i 
		//percorre toda a string
		scan: while(true && i < buffer.lexema.length() ) {
			c =  buffer.proximo();
			switch(estado) {
				case 0:
					//Ao entrar neste case, temos o primeiro caractere a ser lido
					// q0 -> q1
					if(delimitador(c))
						estado = 29;
					else if(c=='i') {
						ultimoEstadoFinal =  1;
						estado = 1;
						buffer.marcarUltimo();
					}
					// Verifica se é uma letra
					else if(Character.isLetter(c) && c!='i') {
						ultimoEstadoFinal = 3;
						estado = 3 ;
						this.buffer.marcarUltimo();
					}
					
					else if(c =='<') {
						estado = 4;
						ultimoEstadoFinal =4;
						buffer.marcarUltimo();
					}
					else if(c =='=') {
						estado =6;
						ultimoEstadoFinal =6;
						buffer.marcarUltimo();
					}
					else if(c =='>') {
						estado =8;
						ultimoEstadoFinal =8;
						buffer.marcarUltimo();
					}
					// Verifica se é um digito
					//Integer.parseInt(String.valueOf(digits.charAt(i)));
					else if(Character.isDigit(c)){
						ultimoEstadoFinal =  10;
						estado = 10;
						buffer.marcarUltimo();
					}
					else if(c==';'){
						estado = 29;
						buffer.marcarUltimo();
					}
					else {
						ultimoEstadoFinal =  -1;
						break scan;
					}
				break;
				case 1:
					if(c=='f') {
						ultimoEstadoFinal = 2;
						estado  =2;
						buffer.marcarUltimo();
					}
					else if(Character.isLetter(c) || Character.isDigit(c)) {
						ultimoEstadoFinal = 3;
						estado = 3 ;
						this.buffer.marcarUltimo();
					}
					else if(delimitador(c)) {
						setultimoEstadoFinal(ultimoEstadoFinal);
						return token;
					}
					else {
						ultimoEstadoFinal =-1;
						estado =0;	
					}
					break;
				case 2:
					// if
					//Identifica se é um id, formado com letras e/ou numeros
					if(this.validarID(c)) {
						ultimoEstadoFinal = 3;
						estado  =3;
						buffer.marcarUltimo();
					}
					else if(delimitador(c)) {
						buffer.marcarUltimo();
						setultimoEstadoFinal(ultimoEstadoFinal);
						return token;
					}
					else {
						ultimoEstadoFinal =-1;
						estado =0;
						setultimoEstadoFinal(ultimoEstadoFinal);
					}
					break;
				case 3:
					if(this.validarID(c)) {
						ultimoEstadoFinal = 3;
						estado = 3 ;
						this.buffer.marcarUltimo();
					}
					else if(delimitador(c) || c=='=') {
						buffer.retrair(1);
						setultimoEstadoFinal(ultimoEstadoFinal);
						return token;
					}
					else {
						ultimoEstadoFinal =-1;
						estado =0;
						setultimoEstadoFinal(ultimoEstadoFinal);
					}
					
					break;
				case 4:
					if(c =='=') {
						estado =5;
						ultimoEstadoFinal =5;
						buffer.marcarUltimo();
					}
					else if(delimitador(c)) {
						buffer.retrair(1);
						setultimoEstadoFinal(ultimoEstadoFinal);
						return token;
					}
					else if(c =='>') {
						estado = 7;
						ultimoEstadoFinal =  7;
						buffer.marcarUltimo();
					}else {
						break scan;
					}
					break;
				case 5:
					ultimoEstadoFinal = 5;
					setultimoEstadoFinal(ultimoEstadoFinal);

					break;
				case 6:
					ultimoEstadoFinal = 6;
					setultimoEstadoFinal(ultimoEstadoFinal);
					break;
				case 7:
					ultimoEstadoFinal = 7;
					setultimoEstadoFinal(ultimoEstadoFinal);
					break;
				case 8:
					if(c =='=') {
						estado =9;
						ultimoEstadoFinal =9;
						buffer.marcarUltimo();
					}
					break;
				case 10:
					if(Character.isDigit(c)){
						ultimoEstadoFinal =  10;
						estado = 10;
						buffer.marcarUltimo();
					}
					else if(c =='.') {
						estado =11;
						ultimoEstadoFinal =10;
						buffer.marcarUltimo();
					}
					else if(c =='E') {
						estado =13;
						ultimoEstadoFinal =10;
						buffer.marcarUltimo();
					}else {
						break scan;
					}
					break;
				case 11:
					if(Character.isDigit(c)) {
						estado =12;
						ultimoEstadoFinal =12;
						buffer.marcarUltimo();
					}else {
						ultimoEstadoFinal =  -1;
					}
					break;
				case 12:
					if(Character.isDigit(c)) {
						estado =12;
						ultimoEstadoFinal =12;
						buffer.marcarUltimo();
					}
					else if(c =='E') {
						estado =13;
						ultimoEstadoFinal =12;
						buffer.marcarUltimo();
					}else {
						break scan;
					}
					break;
				case 13:
					if(c=='-' || c=='+') {
						estado =14;
						buffer.marcarUltimo();
					}
					else if(Character.isDigit(c)) {
						estado =15;
						ultimoEstadoFinal =15;
						buffer.marcarUltimo();
					}
					else {
						break scan;
					}
					break;
				case 14:
					if(Character.isDigit(c)) {
						estado =15;
						ultimoEstadoFinal =15;
						buffer.marcarUltimo();
					}else {
						ultimoEstadoFinal =  -1;
					}
	
					break;
				case 29:
					if(!delimitador(c)) {
						buffer.retrair(1);
						buffer.marcarInicio();
						estado=0;
					}else {
						break scan;
					}
					break;
			}
			i++;
		} //  fim scan:while
		setultimoEstadoFinal(ultimoEstadoFinal);
		return token;
	}
	private boolean validarID(Character c) {
		if(Character.isLetter(c) || Character.isDigit(c)) {
			return true;
		}
		else
			return false;
	}

	private boolean delimitador(Character codigo) {
		return codigo == ' '?  true :  false;
	}
	private void setultimoEstadoFinal(int ultimoEstadoFinal) {
		switch(ultimoEstadoFinal) {
			case -1:
				System.out.println("Palavra não foi reconhecida!");
				break;
			case 1:
				this.buffer.marcarUltimo();
				this.token=  new Token(this.simbolo.ID,buffer.lexema());
				break;
			case 2:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.IF);
				break;	
			case 3:
				this.buffer.marcarUltimo();
				this.token=  new Token(this.simbolo.ID,buffer.lexema());
				break;
			case 5:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.LE);
				break;
			case 6:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.EQ);
				break;
			case 7:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.NEQ);
				break;
			case 8:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.GT);
				break;
			case 9:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.GE);
				break;
			case 10:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.NUM);
				break;
			case 12:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.NUM);
				break;
			case 15:
				this.buffer.marcarUltimo();
				this.token = new Token(this.simbolo.NUM);
				break;
		}
		
		
	}


}
