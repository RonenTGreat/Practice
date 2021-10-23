
import static java.lang.Thread.sleep;

import java.util.Scanner;

public class Heads_Tails {

    public static void main(String[] args) throws InterruptedException {    
        while(true){
            Scanner scanner = new Scanner(System.in);
            String[] select = {"Heads", "Tails"};
            java.util.Random random = new java.util.Random();
            int randomChoose = random.nextInt(select.length);
            String selection = select[randomChoose]; 
            System.out.println("Heads or Tails?");
            System.out.print(">> ");
            scanner.nextLine();
            sleep(1000);
            System.out.println("It's " + selection);
                     
        }

    
    }
}