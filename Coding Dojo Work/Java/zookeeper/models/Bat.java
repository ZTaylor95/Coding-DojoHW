package com.zach.zookeeper.models;
public class Bat extends Mammal {



	public Bat() {
		super(300);
	}
	
	
	public void fly() {
		System.out.println("has started flying");
		this.energyLevel -= 50;
	}
	
	public void eatHumans() {
		System.out.println("has ate a person");
		this.energyLevel += 25;	
	}
	public void attackTown() {
		System.out.println("has attacked the town");
		this.energyLevel -= 25;	
	}
}
