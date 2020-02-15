package btu;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class Client implements Runnable {
    Socket socket;
    ObjectOutputStream out;
    String message;

    @Override
    public void run() {
        try {
            socket = new Socket(InetAddress.getByName("localhost"), 8888);
            out = new ObjectOutputStream(socket.getOutputStream());
            Scanner s = new Scanner(System.in);
            message = s.nextLine();
            out.writeObject(message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
