public class Bat {





         //Attributes
    public static int energyLevel = 300;


        //Setter
        public static int energyLevel() {
            return energyLevel;
        }



        //Getter
        public static void setEnergyLevel(int energyLevel) {
            Bat.energyLevel = energyLevel;
        }

        //Methods

    public void fly(){
        System.out.println("*batwings flapping*");
    }

    public void eatHumans(){
        System.out.println("");

    }

    public void attackTown(){
        System.out.println("*SCREAMING*");

    }
}
