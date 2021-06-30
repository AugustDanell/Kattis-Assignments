import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by August DH on 2017-03-05.
 * Solution to "Booking a Room".
 */
public class bookingARoom2 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        String[] splitted = input.split(" ");

        int rooms = Integer.parseInt(splitted[0]);
        int booked = Integer.parseInt(splitted[1]);

        ArrayList<Integer> roomList = new ArrayList<>();

        for(int i = 0; i < booked; i++){
            int bookedRoom = sc.nextInt();
            sc.nextLine();

            roomList.add(bookedRoom);
        }
        int room = -1;
        for(int i = 1; i <= rooms; i++ ){
            if(!roomList.contains(i)){
                room = i;
                break;
            }
        }

        if(room == -1){
            System.out.print("too late");
        }
        else{
            System.out.print(room);
        }
    }
}
