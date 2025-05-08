package juegos;

public abstract class Juego {
	private int TotalVidas;
	private static int record = 0;
	private int vidas;
    
    
	public Juego(int vidas){
    	this.vidas = vidas;
    	this.TotalVidas = vidas;
	}
   
 
	public boolean QuitaVida(){
        	if(vidas >0){
                	vidas--;
                	if(vidas==0){
                    	return false;
                	}
            	return true;
            	}
        	return false;
    	}
   	 
    	public void ReiniciaPartida(){
        	vidas = TotalVidas;
    	}
   	 
    	public void ActualizaRecord(){
        	if(vidas > record){
            	record = vidas;
            	System.out.println("EL nuevo record es "+record);
        	}
        	else if(vidas == record){
            	record = record;
            	System.out.println("Se alcanzo el record en "+record);
        	}
    	}
    	public void MuestraVidasRestantes() {
    	System.out.println("Vidas restantes: " + vidas);
	}
   	 
}