package btu;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server implements Runnable {
    Socket sock;
    ServerSocket serverSock;
    ObjectInputStream in;

    @Override
    public void run() {
        try {
            serverSock = new ServerSocket(8888);
            sock = serverSock.accept();
            in = new ObjectInputStream(sock.getInputStream());
            System.out.println("Client: " + in.readObject());
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
