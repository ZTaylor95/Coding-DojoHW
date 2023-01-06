class Ninja {
    constructor(name, health, speed = 3, strength = 3) {
        this.name = name;
        this.health = 50;
        this.speed = speed;
        this.strength = strength;

    }

    sayName() {
        console.log(` ${this.name}`);
        return this;
    }

    sayStats() {
        console.log(` name- ${this.name}` , ` health- ${this.health}`, ` speed- ${this.speed} `, ` strentgh- ${this.strength}`);
        return this;
    }

    drinkSake() {
        console.log(` ${this.name} has taken a sip of sake`);
        this.health += 10;
        return this;

    }
    sayStats1() {
        console.log(` name- ${this.name}` , ` health- ${this.health}`, ` speed- ${this.speed} `, ` strentgh- ${this.strength}`, ` wisdom- ${this.wisdom}`);
        return this;
    }


}

const ninja1 =  new Ninja("Genjia")
    ninja1.sayName()
    ninja1.sayStats()
    ninja1.drinkSake()
    ninja1.sayStats()


class Sesnsi extends Ninja{
    constructor(name) {
        super(name, 200);
        this.name = name
        this.speed = 10
        this.strength = 10
        this.wisdom = 10
    }
    speakWisdom() {
        console.log(` ${this.name} has spoken wisdom`);
        this.wisdom += 10;
        return this;

    }

}
const sensi1 = new Sesnsi("Naruto")
sensi1.sayName()
sensi1.sayStats()
sensi1.speakWisdom()
sensi1.sayStats1()


  
