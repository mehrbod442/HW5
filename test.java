// Main program class
public class MainProgram {
    public static void main(String[] args) {
        // Create an object of the second class
        SecondClass mySecondClass = new SecondClass(); // Instantiation of the SecondClass

        // Call a method from the second class
        mySecondClass.displayMessage();
    }
}

// Second class definition
class SecondClass {
    // Method to display a message
    public void displayMessage() {
        System.out.println("Hello from SecondClass!");
    }