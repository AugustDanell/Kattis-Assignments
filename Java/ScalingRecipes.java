import java.util.Scanner;

/**
 * Created by August DH on 2016-12-20.
 */
public class ScalingRecipes {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine();
        StringBuilder builderBob = new StringBuilder();

        for(int i = 0; i < cases; i++){
            String ingredientsData = sc.nextLine();
            String[] splittedIngridientsData = ingredientsData.split(" ");

            int ingridients = Integer.parseInt(splittedIngridientsData[0]);
            float portions = Float.parseFloat(splittedIngridientsData[1]);
            float desiredPortions = Float.parseFloat(splittedIngridientsData[2]);
            float multiplyingFactor = (desiredPortions/portions)/100;
            float mainWeightTimesFactor = 0;
            float[] savedBakersPercentage = new float [ingridients];
            String[] savedRecipes = new String[ingridients];

            builderBob.append("Recipe #" + " " + (i+1) + "\n");
            for(int j = 0; j < ingridients; j++){
                String ingredientData = sc.nextLine();
                String[] splittedIngridientData = ingredientData.split(" ");

                float weight = Float.parseFloat(splittedIngridientData[1]);
                float percentage = Float.parseFloat(splittedIngridientData[2]);

                savedRecipes[j] = splittedIngridientData[0] + " " +splittedIngridientData[2];
            //    savedBakersPercentage[i] = percentage;
                if(percentage == 100 || percentage == 100.0) {
                    mainWeightTimesFactor = weight * multiplyingFactor;
                }
            }

            for(int j = 0; j < ingridients; j++){
                String[] splittedIngridientData = savedRecipes[j].split(" ");
                builderBob.append(splittedIngridientData[0] + " " + ((Float.parseFloat(splittedIngridientData[1])*mainWeightTimesFactor)) + "\n");

            }
            builderBob.append("----------------------------------------" + "\n");
        }

        System.out.print(builderBob.toString());
    }
}
