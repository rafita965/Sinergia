package porfolios;
import java.io.*;
import java.net.*;
import java.util.*;
public class Server {
    private static final int PORT = 1234;
    private static final List<PrintWriter> clients =
        Collections.synchronizedList(new ArrayList<>());

    public static void main(String[] args) {
        System.out.println("Servidor iniciado en puerto " + PORT);
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Cliente conectado: " + socket.getRemoteSocketAddress());
                new ClientHandler(socket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static class ClientHandler extends Thread {
        private Socket socket;
        private BufferedReader in;
        private PrintWriter out;

        ClientHandler(Socket socket) {
            this.socket = socket;
        }
        @Override
        public void run() {
            try {
                in  = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);
                clients.add(out);

                String msg;
                while ((msg = in.readLine()) != null) {
                    System.out.println("Reenviando: " + msg);
                    broadcast(msg);
                }
            } catch (IOException e) {
                System.err.println("Error con cliente " + socket.getRemoteSocketAddress());
            } finally {
                clients.remove(out);
                try { socket.close(); } catch (IOException ignored) {}
                System.out.println("Cliente desconectado: " + socket.getRemoteSocketAddress());
            }
        }
        private void broadcast(String msg) {
            synchronized (clients) {
                for (PrintWriter writer : clients) {
                    writer.println(msg);
                }
            }
        }
    }
}