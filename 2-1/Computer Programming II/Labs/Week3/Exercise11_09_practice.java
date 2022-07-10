import java.util.ArrayList;
import java.util.Scanner;

public class Exercise11_09_practice {
  public static void main(String[] args) {
    System.out.print("Enter the array size n: ");
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();

    System.out.println("The random array is:");
    int[][] matrix = new int[n][n];

	//Randomly fill the array with 0s and 1s.

    // Check rows
    int rowSum = sumRow(matrix[0]);
    ArrayList<Integer> list = new ArrayList<Integer>();
    //Fill this part

    System.out.print("The most 0s row index: ");
    //Fill this part


    // Check columns
    int columnSum = sumColumn(matrix, 0);
    //Fill this part

    System.out.print("\nThe most 0s column index: ");
    //Fill this part

  }

  //sumRow method returns the sum of given array
  public static int sumRow(int row[]) {

  }


  //sumColumn method returns the sum of the given column
  public static int sumColumn(int matrix[][], int column) {

  }
}
