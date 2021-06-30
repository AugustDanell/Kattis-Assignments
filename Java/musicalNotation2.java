import java.util.Scanner;

/**
 * Created by August DH on 2017-08-27.
 */
public class musicalNotation2 {
    public static int getNote(char note){
        if(note == 'G'){
            return 0;
        }
        else if(note == 'F'){
            return 1;
        }
        else if(note == 'E'){
            return 2;
        }
        else if(note == 'D'){
            return 3;
        }
        else if(note == 'C'){
            return 4;
        }
        else if(note == 'B'){
            return 5;
        }
        else if(note == 'A'){
            return 6;
        }
        else if(note == 'g'){
            return 7;
        }
        else if(note == 'f'){
            return 8;
        }
        else if(note == 'e'){
            return 9;
        }
        else if(note == 'd'){
            return 10;
        }
        else if(note == 'c'){
            return 11;
        }
        else if(note == 'b'){
            return 12;
        }
        else{
            //If == 'a'
            return 13;
        }
    }

    public static void fillNotes(String[] notebook, String input){
        int step = 3;
        String[] splitted = input.split(" ");

        for(int i = 0; i < splitted.length; i++){
            int index = getNote(splitted[i].charAt(0));
            int increments = 0;
            if(splitted[i].length() > 1){
                increments = Integer.parseInt(splitted[i].substring(1));
            }
            else{
                increments = 1;
            }
            char[] arr = notebook[index].toCharArray();

            for(int j = 0; j < increments; j++){
                arr[step] = '*';
                step ++;
            }

            notebook[index] = new String(arr);

            step ++;
        }
    }

    public static void print(String[] notebook){
        for(int i = 0; i < 14; i ++){
            System.out.println(notebook[i]);
        }
    }

    public static void initialize(String[] notebook, int length){
        notebook[0] = "G:"; notebook[1] = "F:"; notebook[2] = "E:"; notebook[3] = "D:"; notebook[4] = "C:";
        notebook[5] = "B:"; notebook[6] = "A:"; notebook[7] = "g:"; notebook[8] = "f:";  notebook[9] = "e:";
        notebook[10] = "d:"; notebook[11] = "c:"; notebook[12] = "b:"; notebook[13] = "a:";

        for(int j = 0; j < 14; j++) {
            for (int i = -1; i < length; i++) {
                if(i == -1){
                    notebook[j] += " ";
                }
                else{
                    if(j == 1 || j == 3 || j == 5 || j == 7 || j == 9 || j == 13){
                        notebook[j] += "-";
                    }
                    else{
                        notebook[j] += " ";
                    }
                }
            }
        }
    }

    public static int getLength(String input){
        int returnLength = 0;
        String splitted[] = input.split(" ");

        for(int i = 0; i < splitted.length; i++){
            if(splitted[i].length() > 1) {
                returnLength += Integer.parseInt(splitted[i].substring(1));
            }
            else{
                returnLength ++;
            }

            if(i!= 0){
                //Apparently spaces should always be made?
                returnLength ++;
            }
        }

        return returnLength;
    }

    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int notes = sc.nextInt();
        sc.nextLine();

        String input = sc.nextLine();
        int length = getLength(input);

        String[] noteBook = new String[14];

        initialize(noteBook, length);
        fillNotes(noteBook, input);
        print(noteBook);
    }
}
