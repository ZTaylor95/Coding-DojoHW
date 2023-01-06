package com.zach.zookeeper.models;

public class Gorilla extends Mammal {

	public Gorilla() {
		super ();
	}

	
	public void throwSomething() {
		System.out.println("has thrown something");
		this.energyLevel -= 5;
		
	}
	
	public void eatBananas() {
		System.out.println("has eaten a banana");
		this.energyLevel += 10;
		
	}
	
	public void climb() {
		System.out.println("has started climbing");
		this.energyLevel -= 10;
	}

}
