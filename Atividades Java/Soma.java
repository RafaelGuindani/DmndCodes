package com.company;
import java.util.Scanner; // Importing  the Scanner class

public class Soma {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); //Creating an object named "sc" of the Scanner class.
        System.out.println("Insira o primeiro valor:\n>: ");
        int a = sc.nextInt();
        System.out.println("Insira o segundo valor:\n>: ");
        int b = sc.nextInt();

        int sum = a + b;
        System.out.println("A soma dos valores é:\n>: "+ sum);
    }}
