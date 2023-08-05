import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("res/input_view.txt"));
		Scanner sc = new Scanner(System.in);
		// T=sc.nextInt();
        int T = 10;
		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList<Integer>();
            for (int i=1; i<=N; i++){
                arr.add(sc.nextInt());
            }
            System.out.println(arr);
            System.out.println(test_case);
		}
	}
}