package com.codingdojo.helloworld;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/daikichi")
public class HomeController {
    @RequestMapping("")
    public String index(){
      return "Welcome";
    }
    

    @RequestMapping("/tomorrow")
    public String world(){
      return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
    }
    @RequestMapping("/travel/{place}")
    public String place(@PathVariable("place")String place) {
    	return "Congratulations! You will soon travel to: " + place + "!";
    }
    
    
    @RequestMapping("/lotto/{number}")
    public String lotto(@PathVariable("number")Integer number) {
    	if (number%2 == 0 ) {
    		return "You will take a grand journey in the near future, but be weary of tempting offers";
    	}
    	else { 
    		return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends";
    	
    	}
    	
    		
    	
    }
  
}