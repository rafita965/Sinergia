/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Practica4_2;

 
import Profesor.Teclado;
import juegos.Juego;
import juegos.Numeros.JuegoAdivinaImpar;
import juegos.Numeros.JuegoAdivinaPar;
import juegos.Numeros.JuegoAdivinaNumero;
import juegos.interfaces.Jugable;
import java.util.*;
import juegos.excepciones.JuegoException;
import juegos.letras.JuegoAhorcado;

public class Aplicacion extends Juego{
	public Aplicacion(int vidas) {
    	super(vidas);
	}
        
        public static void InfoVector(Vector<Jugable> vector) {
        System.out.println("Capacidad del vector: " + vector.capacity());
        System.out.println("Tamaño del vector: " + vector.size());
        
        }
	public static Jugable EligeJUego() throws JuegoException{
        Vector<Jugable> juegos = new Vector<>(3, 2);
        InfoVector(juegos); 
   	 
    	JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3);
        JuegoAdivinaImpar juego2 = new JuegoAdivinaImpar(3);
        JuegoAdivinaPar juego3 = new JuegoAdivinaPar(3);
        JuegoAhorcado juego4 = new JuegoAhorcado(3);

        // Añadir los 3 juegos de números
        juegos.add(juego1);
        juegos.add(juego2);
        juegos.add(juego3);
        InfoVector(juegos); // Mostrar estado tras añadir los 3 juegos

        // Añadir juego del ahorcado
        juegos.add(juego4);
        InfoVector(juegos); 
   	 
    	
    	int eleccion = -1;
    	boolean bucle = true;
    	
    	while (bucle) {
        	System.out.println("Elige un juego:");
        	System.out.println("1. Adivina un número");
        	System.out.println("2. Adivina un número impar");
        	System.out.println("3. Adivina un número par");
        	System.out.println("4. Juego de ahorcado");
        	System.out.print("Opción: ");

       
            	eleccion  = Teclado.LeeEntero();
                while(eleccion>5 || eleccion<0){
                    System.out.println("Elige un juego:");
                    System.out.println("1. Adivina un número");
                    System.out.println("2. Adivina un número impar");
                    System.out.println("3. Adivina un número par");
                    System.out.println("4. Juego de ahorcado");
                    System.out.print("Opción: ");
                    eleccion = Teclado.LeeEntero();
                }
                
            	if (eleccion >= 1 && eleccion <= 4) {
                	return juegos.get(eleccion - 1); 
            	} else if (eleccion == 5) {
                	bucle = false;
                	System.out.println("Saliendo del programa.");
              	 
            	} else {
                	System.out.println("Opción no válida. Intenta de nuevo.");
            	}
        	
    	}
	return null;
	}
 
}
