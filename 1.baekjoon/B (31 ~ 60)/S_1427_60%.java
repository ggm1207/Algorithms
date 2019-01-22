import java.util.*

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in)

        String n = sc.nextLine()

        char arr[] = new char[n.length()]

        for(int i=0
            i < n.length()
            i++){
            arr[i] = n.charAt(i)
        }
        Arrays.sort(arr)
        for(int i=arr.length-1
            i >= 0
            i--)
        System.out.print(arr[i])
    }

}
