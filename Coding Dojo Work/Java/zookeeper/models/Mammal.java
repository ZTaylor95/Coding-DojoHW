package com.zach.zookeeper.models;

public class Mammal {
	 protected int energyLevel;


	
	public Mammal() {
		this.energyLevel = 100;
		
	}

	public Mammal(int energyLevel ) {
		this.energyLevel = energyLevel;
	}

	public int displayEnergy () {
		System.out.println("Current Energy level is" + energyLevel);
		return energyLevel;
		
		
	}
	
	}
	
