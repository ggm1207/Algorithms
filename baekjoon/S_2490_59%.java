import java.util.*

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in)

        for(int i=0
            i < 3
            i++){
            int A = 0
            for(int j=0
                j < 4
                j++){
                A += sc.nextInt()
            }
            System.out.println((char)('A'+((8-A) % 5)))
        }

    }
}
