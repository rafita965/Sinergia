package porfolios;
import java.io.*;
import java.net.*;
public class Cliente {
    private static final String HOST = "localhost";
    private static final int    PORT = 1234;
    public static void main(String[] args) {
        try (BufferedReader console = new BufferedReader(new InputStreamReader(System.in))) {
            // 1) Pedir al usuario que ingrese su ID de cliente
            System.out.print("Ingresa tu ID de cliente (número): ");
            String clientId = console.readLine().trim();
            String prefix = "Cliente " + clientId + ": ";
            // 2) Conectar al servidor
            Socket socket = new Socket(HOST, PORT);
            BufferedReader in  = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter   out = new PrintWriter(socket.getOutputStream(), true);

            System.out.println("Conectado al servidor " + HOST + ":" + PORT);

            // 3) Hilo para leer mensajes del servidor
            new Thread(() -> {
                try {
                    String line;
                    while ((line = in.readLine()) != null) {
                        // Si el mensaje viene de este cliente, no lo mostramos
                        if (!line.startsWith(prefix)) {
                            System.out.println(line);
                        }
                    }
                } catch (IOException e) {
                    System.err.println("Conexión cerrada.");
                }
            }).start();
            // 4) Bucle de envío de mensajes con prefijo [ID]
            String msg;
            while ((msg = console.readLine()) != null) {
                if (!msg.trim().isEmpty()) {
                    out.println(prefix + msg);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}