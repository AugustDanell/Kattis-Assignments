import java.util.*;

/**
 * Created by August DH on 2017-06-16.
 */
public class unbearableZoo1 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        boolean run = true;

        StringBuilder builderBob = new StringBuilder();
        int list = 1;

        while(run){
            int animals = sc.nextInt();
            sc.nextLine();

            if(animals == 0){
                run = false;
            }
            else{
                builderBob.append("List " + list + ":\n");

                //Filling the list with the animal type
                String[] inputList = new String[animals];
                for(int i = 0; i < animals; i++){
                    String input = sc.nextLine();
                    String[] splittedInput = input.split(" ");
                    inputList[i] = splittedInput[splittedInput.length - 1];
                }

                //Putting the inputList into the animal list.
                HashMap<String, Integer> animalList = new HashMap<>();
                for(int i = 0; i < animals; i++){
                    boolean found = false;

                    //Iterating over the keyset
                    for(String key: animalList.keySet()){
                        if (inputList[i].equalsIgnoreCase(key)){
                            found = true;
                            animalList.put(key, animalList.get(key) + 1);
                            //If found, increments the integer belonging to the name.
                        }
                    }

                    if(!found){
                        animalList.put(inputList[i], 1); //One animal
                    }
                }

                ArrayList<String> printList = new ArrayList<>();
                for(String key: animalList.keySet()){
                    String filthyAnimal = key;
                    filthyAnimal = Character.toLowerCase(filthyAnimal.charAt(0)) + filthyAnimal.substring(1);
                    printList.add(filthyAnimal + " | " + animalList.get(key));

                    // The rathr simple line for making the String "filthyAnimal" lowercase was found on Stack Overflow
                    // https://stackoverflow.com/questions/4052840/most-efficient-way-to-make-the-first-character-of-a-string-lower-case
                }

                Collections.sort(printList);

                for(int i = 0; i < printList.size(); i++){
                    builderBob.append(printList.get(i) + "\n");
                }

                list++;
            }
        }

        System.out.print(builderBob.toString());
    }
}
