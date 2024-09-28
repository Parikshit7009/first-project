package HelloWorld;

import java.util.HashMap;
import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {
        // Simulate a database (in reality, use a database connection)
        HashMap<String, String> userDatabase = new HashMap<>();
        userDatabase.put("john.doe", "password123"); 
        userDatabase.put("jane.smith", "securePassword");

        Scanner scanner = new Scanner(System.in);
        boolean loggedIn = false;

        while (!loggedIn) {
            System.out.println("Enter username:");
            String username = scanner.nextLine();

            System.out.println("Enter password:");
            String password = scanner.nextLine();

            // Validate credentials (in reality, hash and salt passwords)
            if (userDatabase.containsKey(username) && userDatabase.get(username).equals(password)) {
                System.out.println("Login successful!");
                loggedIn = true;
            } else {
                System.out.println("Invalid username or password. Try again.");
            }
        }

        scanner.close();
    }
}
