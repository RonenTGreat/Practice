package com.RonenTGreat;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    float weight;
	    float height;
        System.out.print("Enter your weight(in kg): ");
        Scanner scanner = new Scanner(System.in);
        weight = scanner.nextFloat();

        System.out.print("Enter your height (in cm): ");
        height = scanner.nextFloat();

        float bodyMassIndex = weight / height * height;

        if(bodyMassIndex > 0 && bodyMassIndex < 18.5)
            System.out.println("Your BMI is " + bodyMassIndex + "\n You are underweight. You should eat more foods.");

        else if(bodyMassIndex >= 18.5 && bodyMassIndex < 25)
            System.out.println("Your BMI is " + bodyMassIndex + "\n You are normal. Keep it up!");

        else if(bodyMassIndex >= 25 && bodyMassIndex < 30)
            System.out.println("Your BMI is " + bodyMassIndex + "\n You are overweight. " +
                    "Decrease the foods you eat and exercise;");

        else if(bodyMassIndex > 30)
            System.out.println("Your BMI is " + bodyMassIndex + "\n You are obese. Go on a diet and exercise intensively");

        else
            System.out.println("Invalid inputs");

    }
}
