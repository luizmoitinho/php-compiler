import java.util.Scanner;

public class Buffer {
	protected String lexema;
	protected int posAtual, posUltimo, posInicio;
	
	public Buffer(String lexema){
		this.lexema=lexema;
		this.posAtual=0;
		this.posUltimo=0;
		this.posInicio=0;
	}
	
	public char proximo() {
		return this.lexema.charAt(this.posAtual++);
	}
	public void marcarInicio(){
		this.posInicio= this.posAtual;
	}
	public void marcarUltimo(){
		this.posUltimo = this.posAtual;	
	}
	public void retrair(int pos) {
		this.posAtual -=pos; 
	}
	public void retrairAoUltimo() {
		this.posAtual--;
	}
	public String lexema() {
		return this.lexema.substring(this.posInicio,this.posUltimo);
	}
	
	public int getPosAtual() {
		return this.posAtual;
	}
}
