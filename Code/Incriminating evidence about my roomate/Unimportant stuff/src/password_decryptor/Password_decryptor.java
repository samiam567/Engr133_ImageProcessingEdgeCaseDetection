package password_decryptor;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Password_decryptor {
	private static  int p, q; //two prime numbers (these are what are used to derive the private key)
	private static long N = p*q; //N and e make up the public key and are used to encrypt messages
	private static long e,d; //N and d make up the private key which you keep to yourself and is used to decrypt messages
	
	
	private static String[] chars = {"","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",","'",";",":","<",">","?","/","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","1","2","3","4","5","6","7","8","9","0"};
			
	private static array list = new array("String");
	
	
	private static String fileName = "../data.dat";
	private static String decodedFileName = "../onlyThoseWhoKnowTheSecretCanRead.txt";
	
	private static int indexOfInList(String thing)  {
		for (int i = 0; i < chars.length; i++) {
			if (thing.equals(chars[i])) return i;
		}
		return -1;
	}
	
	private static boolean isPrime(long num) {
		for (long i = 2; i <= Math.sqrt(num)+1; i++) {
			if (num%i==0) return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		//Congrats for deciphering the code! Check these out: (You're sure to like them) || https://www.youtube.com/watch?v=2rZY8iX8Mdw&ab_channel=OfficialENGR || https://www.youtube.com/watch?v=nFbWXuR_2Ow&ab_channel=OfficialENGR || Boiler Up!!
		boolean writeMode = true;
		
		
		try {
			if ( ((args.length > 0) && (args[0].equals("write"))) || (writeMode) ) {
					
					String input = JOptionPane.showInputDialog("What do you want to encrypt?");
					
					String password = "";
					while(! password.contains(" ")) {
						password = JOptionPane.showInputDialog("What password do you want to use? (Must be two words with a space inbetween them");
					}
					
					FileWriter out = new FileWriter(fileName);
					
					out.write(passwordCrypt(input,password.toLowerCase(),0));
					
					out.close();
			
				
			}else{
				File inFile = new File(fileName);
					
				Scanner scan = new Scanner(inFile);
					
				String input = scan.nextLine();
	
				scan.close();
					
				String output = passwordCrypt(input,JOptionPane.showInputDialog(null, "What is the password? (two words with a space inbetween)").toLowerCase(),1);
					
				System.out.println(output);
					
				FileWriter out = new FileWriter(decodedFileName);
					
				out.write(output);
					
				out.close();
					
				JOptionPane.showMessageDialog(null, output);
		
				
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			JOptionPane.showMessageDialog(null, "File not found");
		} catch (IOException e) {
			e.printStackTrace();
			JOptionPane.showMessageDialog(null, "ioException");
		}
		

	}
	
	public static String passwordCrypt(String input,String password, int mode) {

		
		password = password.toLowerCase();
		Scanner passScan = new Scanner(password);
		
		String first = passScan.next();
		String second = passScan.next();
		
		passScan.close();
		
		int firstPrime = 0, secondPrime = 0;
		   
		//extracting a number from first
		for (int i = 0; i < first.length(); i++) {
			firstPrime += Math.pow(indexOfInList(first.substring(i,i+1)),2);
		   }
		   
		//make sure firstPrime equates to a prime number
		while(! isPrime(firstPrime)) {
			firstPrime++;
		} 

		System.out.println("firstPrime: " + firstPrime);

		//extracting a number from second
		for (int i = 0; i < second.length(); i++) {
			secondPrime += Math.pow(indexOfInList(second.substring(i,i+1)),2);
		}

		//make sure secondPrime equiates to a prime numnber
		while(! isPrime(secondPrime)) {
			secondPrime++;
		}
		System.out.println("secondPrime: " + secondPrime);
		   
		p = firstPrime;
		q = secondPrime;		

		
		N = p*q;
		
		if (mode == 2) {
			if (input.substring(0,1).equals("{")) {
				mode = 1; //decrypt
			}else {
				mode = 0; //encrypt
			}
		}
		
		initialize();
		return crypt(input,mode,N,e);

	}
	
	public static void initialize() {
		int c = (p-1) * (q-1);
		
 	//guessing the rest of the numbers 
		//find e 
		e = 2;
		while ((c % e) == 0) {
			e++;
		}
		
		//find d 
		d = 2;
		while ((e*d) % c != 1) {
			d++;
		}
		
		System.out.println("N: " + N);
		System.out.println("e: " + e);
		System.out.println("d: " + d);

	//////////////
	}
	

	
	public static String crypt(String input, int mode, long N1, long e1) {
		if  (mode == 0) {//encrypt     //(input.substring(0, 1).equals("{")) { 
			N = N1;
			e = e1;
			String message = encrypt(input);
			message = encode(message);
			return message;
		}else if (mode == 1) { //decrypt
			String message = decode(input);
		
			message = decrypt(message);
			return message;
		}else {
			return "logic error";
		}
	}
	
	private static String encrypt(String input) {
		
		boolean charFound = false; //if the char has been matched yet
		for (int i = 0; i < input.length(); i++) {
			
			charFound = false; //reset the charFound for the next char
			
			String str = input.substring(i, i+1); //getting the char
	
			for (int q = 0; q < chars.length; q++) { //searching for the char in the chars list to get the index
				
				if (chars[q].equals(str)) {
					list.add("" + q); //adding the index to the output array
					charFound = true;
					break;
				}
			}
			
			if (! charFound) {
				System.out.println("Char " + str + " was not found in the char list and is therefore not a valid char");
			}
			
			
		}
		
		return list.toString();
	}
	
	
	private static String decrypt(String input) {
		list.getValues(input.substring(1, input.length()-1), ",");
		String translatedMessage = "";
	
		for (String str : list.getArray(" ")) {
			try {
				System.out.print(str);
				String translatedChar = (chars[Integer.parseInt(str) % chars.length]);
				System.out.println(" > " + translatedChar);
				translatedMessage += translatedChar;
			}catch(NumberFormatException n) {}
		}
		return translatedMessage;
	}
	
	private static String encode(String input) {
		list.getValues(input.substring(1, input.length()-1), ",");
		
		String[] valuesStr = list.getArray("");
		long[] values = new long[valuesStr.length];
		
		for (int q=0; q < values.length; q++) values[q] = Long.parseLong(valuesStr[q]);
		
		
		for (int i = 0; i < values.length; i++) {
			values[i] = RSA(values[i],e,N); 
			System.out.println(values[i]);
		}
	
	
		
		for (int q=0; q < values.length; q++) valuesStr[q] = "" + values[q];
		
		list.setValues(valuesStr);
		
		return list.toString();
	}
	
	private static long RSA(long b, long e, long m) {
		long answer = 1;
		for (int i = 1; i <= e; i++) {
			answer *= b % m;
			answer = answer % m;
		}
		System.out.println(answer);
		return answer;
	}
	
	private static String decode(String input) {
		list.getValues(input.substring(1, input.length()-1), ",");

		System.out.println("decode: " + list.toString());
		
		String[] valuesStr = list.getArray("");
		long[] values = new long[valuesStr.length];
	
		for (int q=0; q < values.length; q++) values[q] = Long.parseLong(valuesStr[q]);
		
		for (int i = 0; i < values.length; i++) {
			values[i] = RSA(values[i],d,N);
		}
		
		for (int q=0; q < values.length; q++) valuesStr[q] = "" + values[q];
		
		list.setValues(valuesStr);
		
		System.out.println("decoded: " + list.toString());
		
		return list.toString();
	}
}

