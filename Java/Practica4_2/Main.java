
package Practica4_2;

import Profesor.Teclado;
import juegos.interfaces.Jugable;
import juegos.excepciones.JuegoException;

public class Main {

	
  	public static void main(String[] args) {
    	
    	 boolean seguirJugando = true;

        try {
            while (seguirJugando) {
                Jugable juego = Aplicacion.EligeJUego(); // Puede lanzar JuegoException

                if (juego != null) {
                    juego.MuestraInfo();
                    juego.Juega();
                } else {
                    break;
                }

                System.out.print("¿Quieres jugar de nuevo? (s/n): ");
                String respuesta = Teclado.LeeCadena();
                if (!respuesta.equalsIgnoreCase("s")) {
                    seguirJugando = false;
                    System.out.println("¡Gracias por jugar!");
                }
            }
        } catch (JuegoException e) {
            System.out.println("Error en el juego: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error inesperado: " + e.getMessage());
        } finally {
            System.out.println("Fin del programa");
        }
    }
}
