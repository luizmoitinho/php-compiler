
public class Lexer {
	Buffer buffer =  new Buffer("if");
	
	public Token  proximoToken() {
		int estado =0; // indica o estado atual - AFD - AFND
		int ultimoFinal =-1;
		int c;
		buffer.marcarInicio(estado);
		//percorre toda a string
		for(int i=0;i<buffer.lexema.length();i++) {
			c =  buffer.proximo();
			switch(estado) {
				case 0:
					if(delimitador(c))
						estado = 29;
					else if(c=='i') {
						ultimoFinal =  1;
						estado = 1;
						buffer.marcarUltimo();
					}
					// Verifica se � uma letra
					else if(Character.isLetter(c)){
						ultimoFinal =  3;
						estado =3;
						buffer.marcarUltimo();
					}
				break;
				case 1:
					if(c=='f') {
						ultimoFinal = 2;
						estado  =2 ;
						buffer.marcarUltimo();
					}
					else if(Character.isLetter(c) || Character.isDigit(c)) {
						ultimoFinal =3;
						
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
	}
	
	public boolean delimitador(int codigo) {
		return codigo ==';'?  true :  false;
	}

}
