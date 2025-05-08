/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package juegos.Numeros;


import juegos.interfaces.Jugable;
import juegos.Juego;
import Profesor.Teclado;
import java.awt.*;
import java.util.*;

public class JuegoAdivinaImpar extends Juego implements Jugable{
    	Random randomNumbers = new Random();
    	private int numeroadivinar;
	private boolean bucle = false;
    	Frame f = new Frame();
    
	public JuegoAdivinaImpar(int vidas) {
    	super(vidas);
   	 
	}
    	public boolean ValidaNumero(){
	numeroadivinar = randomNumbers.nextInt(10);
    	while (numeroadivinar % 2 == 0){
	numeroadivinar = randomNumbers.nextInt(10);
    	}
    	return true;
    
	}
  	 
    
	public void Juega(){
	ReiniciaPartida();
    	ValidaNumero();
    	System.out.println(numeroadivinar);
 	while(bucle!=true){
   	 
    	System.out.println("adivine un número entre el 0 y el 10 Impar.");
    	System.out.print("Ingrese valor :");
        
    	int numero = Teclado.LeeEntero();
    	while(numero>10 || numero<0){
            System.out.println("adivine un número entre el 0 y el 10 Impar.");
            System.out.print("Ingrese valor :");
            numero = Teclado.LeeEntero();
        }
        
    	if(numero == numeroadivinar){
        	System.out.println("Ganaste");
        	ActualizaRecord();
        	bucle=true;
    	}
    	else{
        	if(QuitaVida()){
           	 
            	MuestraVidasRestantes();
            	if(numero > numeroadivinar){
                	System.out.println("Ingrese un valor menor");
            	}
            	else{
                	System.out.println("Ingrese un valor mayor");
            	}
        	}
        	else{
            	System.out.println("Perdiste :(");
             	bucle=true;  	 
                    	}
      	 
    	}
   	 
	}
	}

	@Override
	public void MuestraInfo() {
   	 
    	f = new Frame("Juego Adivina un Número IMPAR");
    	f.setSize(950, 200);
    	f.setLayout(null); // Usamos el layout nulo para poder poner los componentes en posiciones específicas
   	 
    	// Llamar a los métodos para agregar las etiquetas
    	Label l1 = new Label("Adivina un número Impar");
     	l1.setBounds(400, 50, 200, 80);
    	f.add(l1);
    	Label l2 = new Label("Hay que adivinar un numero entre el 0 y el 10, que va a ser impar, tienes 5 vidas, "
            	+ "si logras adivinarlo antes de que se te acaben ganas, sino pierdes.");
     	l2.setBounds(20, 100, 1000, 80);
     	f.add(l2);
   	 
    	// Hacer visible el JFrame
    	f.setVisible(true);
    	f.addWindowListener(new java.awt.event.WindowAdapter() {
        	public void windowClosing(java.awt.event.WindowEvent we) {
            	f.dispose();
        	}
    	});
	}


}
