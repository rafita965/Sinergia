package juegos.letras;

import Profesor.Teclado;
import java.awt.Frame;
import java.awt.Label;
import juegos.Juego;
import juegos.interfaces.Jugable;
import java.util.*;
import juegos.excepciones.JuegoException;

public class JuegoAhorcado extends Juego implements Jugable {
    Random random = new Random();
    private String[] palabras = { "computadora", "programacion", "teclado", "raton", "pantalla",
    "java", "codigo", "variable", "funcion", "metodo", "objeto",
    "clase", "herencia", "polimorfismo", "interfaz", "compilador",
    "algoritmo", "estructura", "condicional", "bucle", "recursividad",
    "archivo", "modulo", "paquete", "importar", "sintaxis",
    "conexion", "internet", "servidor", "cliente", "base",
    "datos", "tabla", "registro", "consulta", "clave",
    "primaria", "foranea", "indice", "normalizacion", "consulta",
    "json", "xml", "html", "css", "javascript", "python",
    "arduino", "robotica", "sensor", "motor", "resistencia",
    "futbol", "cancha", "torneo", "jugador", "equipo",
    "balon", "arbitro", "gol", "camiseta", "zapatos",
    "pelota", "pasion", "deporte", "amistad", "competencia",
    "escuela", "educacion", "materia", "tarea", "examen",
    "historia", "geografia", "ciencia", "literatura", "musica",
    "arte", "teatro", "pintura", "escultura", "bateria",
    "guitarra", "piano", "violin", "trompeta", "canto",
    "circulo", "cuadrado", "triangulo", "rectangulo", "figura",
    "numero", "decimal", "entero", "fraccion", "dividir"};
    private int indice = random.nextInt(palabras.length);
    private String adescubrir = palabras[indice];
    private boolean bucle=false;
    Frame f = new Frame();
    public JuegoAhorcado(int vidas) throws JuegoException{
    	super(vidas);
   	for (char c : adescubrir.toCharArray()) {
        if (Character.isDigit(c)) {
            throw new JuegoException("La palabra contiene un número: " + adescubrir);
        }
	}
        
    }
     

    @Override
    public void MuestraInfo() {
        f = new Frame("Juego el ahorcado");
    	f.setSize(950, 200);
    	f.setLayout(null); // Usamos el layout nulo para poder poner los componentes en posiciones específicas
   	 
    	// Llamar a los métodos para agregar las etiquetas
    	Label l1 = new Label("Adivina la palabra");
     	l1.setBounds(400, 50, 200, 80);
    	f.add(l1);
    	Label l2 = new Label("Hay que adivinar una palabra, te va ir mostrando si acertaste y tienes 3 vidas "
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

    @Override
    public void Juega() {
        ReiniciaPartida();
        int cont=0;
        String adivinar = String.format("%0" + adescubrir.length() + "d", 0).replace("0", "-");
        System.out.println("La palabra a adivinar es: " + adivinar);
        
        while(bucle!=true){
        System.out.print("Ingrese una letra para empezar a jugar :");
        char letra = Teclado.LeeCaracter();
        
        while(letra == 0){
            System.out.print("Ingrese una letra para empezar a jugar :");
            letra = Teclado.LeeCaracter();
        }
        char[] adivinarArray = adivinar.toCharArray();
        for (int i = 0; i < adivinar.length(); i++) {
            if(adescubrir.charAt(i) == letra){
                cont++;
                adivinarArray[i] = letra;
                adivinar = new String(adivinarArray);
                
            }
            
            }
        
         if(adivinar.equalsIgnoreCase(adescubrir)){
        	System.out.println("Ganaste");
        	ActualizaRecord();
        	bucle=true;
            }
         if(cont == 0){
        	if(QuitaVida()){
           	 
            	MuestraVidasRestantes();
            	
        	}
        	else{
            	System.out.println("Perdiste :(");
             	bucle=true;  	 
                    	}
      	 
            }
        
            
         cont=0;
   	 System.out.println(adivinar);
    
    	
    	
    }
    }
}


