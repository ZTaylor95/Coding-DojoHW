package com.zach.zookeeper;

import com.zach.zookeeper.models.Gorilla;

import com.zach.zookeeper.models.Bat;

public class GorillaTest {

	public static void main(String[] args ) {
		Gorilla g = new Gorilla();
		g.throwSomething();
		g.throwSomething();
		g.throwSomething();
		g.eatBananas();
		g.eatBananas();
		g.climb();
		g.displayEnergy();
		
		
		
		Bat b = new Bat(); 
		b.fly();
		b.fly();
		b.fly();
		b.eatHumans();
		b.eatHumans();
		b.attackTown();
		b.displayEnergy();
	}
}
	
	
