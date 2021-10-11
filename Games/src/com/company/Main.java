package com.company;


import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while(true){
            String[] choice = {"rock", "paper", "scissor"};
            int computerScore = 0;
            int playerScore = 0;
            java.util.Random random = new java.util.Random();
            int randomTake = random.nextInt(choice.length);
            String computer = (choice[randomTake]);
            System.out.println("Rock, Paper or Scissor?");
            System.out.print(">> ");
            String player = input.next();
            if(player.toLowerCase().strip().equals(computer))
                System.out.println("It's a tie!");
            else if(player.equalsIgnoreCase("rock")){
                if(computer.equals("paper")){
                    System.out.println("You lose! " + computer + " covers " + player + ".");
                    computerScore += 1;
                }
                else{
                    System.out.println("You win! " + player + " destroys " + computer + ".");
                    playerScore += 1 ;
                }
            }
        }

    }
}
