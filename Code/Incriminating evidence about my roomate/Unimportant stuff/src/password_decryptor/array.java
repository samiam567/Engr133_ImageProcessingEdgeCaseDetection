package password_decryptor;


import java.util.Arrays;
import javax.swing.JOptionPane;

public class array {
	public static enum Type {Int,String,Double,Long};
	private  Type arrayType;
	private String delimiter = ",";
	private  int[] arrayListInt = new int[0];
	private  String[] arrayListString = new String[0];
	private  double[] arrayListDouble = new double[0];
	private  long[] arrayListLong = new long[0];
	private int length = 0;
	
	public array(String arrayTypeStr) {
		switch (arrayTypeStr) {
			case "String":
				arrayType = Type.String;
				break;
			case "int":
				arrayType = Type.Int;
				break;
			case "double":
				arrayType = Type.Double;
				break;
			case "long":
				arrayType = Type.Long;
				break;
			default:
				try {
					throw new NoSuchFieldException("lol u suk at progreming. Thats not a possible array tipe");
				}catch(NoSuchFieldException e) {
					e.printStackTrace();
				}
				break;
		}
		
		if (arrayType.equals(Type.Int)) {
			arrayListInt = new int[1];
		}else if  (arrayType.equals(Type.String)){
			arrayListString = new String[1];
		}else if  (arrayType.equals(Type.Double)){
			arrayListDouble = new double[1];
		}else if  (arrayType.equals(Type.Long)){
			arrayListLong = new long[1];
		}
	}
	
	public void setSize(int size) {
		length = size;
		resizeArrayList();
	}
	
	public void setDelimeter(String delimiter1) {
		delimiter = delimiter1;
	}
	
	public void setValues(String value, String delimiter1) {
		getValues(value,delimiter1);
	}
	
	public void setValues(int[] newArrayList) {
		arrayListInt = newArrayList;
	}
	
	
	public void setValues(double[] newArrayList) {
		arrayListDouble = newArrayList;
	}
	
	public void setValues(String[] newArrayList) {
		arrayListString = newArrayList;
	}
	
	public void setValues(long[] newArrayList) {
		arrayListLong = newArrayList;
	}
	
	public void add(int newElement) {
		length++;
		resizeArrayList();
		arrayListInt[length-1] = newElement;
	}
	
	public void add(double newElement) {
		length++;
		resizeArrayList();
		arrayListDouble[length-1] = newElement;
	}
	
	public void add(String newElement) {
		length++;
		resizeArrayList();
		arrayListString[length-1] = newElement;
	}
	
	public void add(long newElement) {
		length++;
		resizeArrayList();
		arrayListLong[length-1] = newElement;
	}
	
	public void removeLast() {
		length--;
		resizeArrayList();
	}
	
	
	
	public int indexOf(int element) { //returns the first index of the passed value in the array (returns -1 if it is not present)
		int index = -1;
		int cEl;
		for (int i = 0; i < arrayListInt.length; i++) {
			cEl = arrayListInt[i];
			if (cEl == element) {
				index = i;
				break;
			}
		}
		return index;
	}
	
	public int indexOf(double element) { //returns the first index of the passed value in the array (returns -1 if it is not present)
		int index = -1;
		double cEl;
		for (int i = 0; i < arrayListDouble.length; i++) {
			cEl = arrayListDouble[i];
			if (cEl == element) {
				index = i;
				break;
			}
		}
		return index;
	}
	

	public int indexOf(long element) { //returns the first index of the passed value in the array (returns -1 if it is not present)
		int index = -1;
		long cEl;
		for (int i = 0; i < arrayListLong.length; i++) {
			cEl = arrayListLong[i];
			if (cEl == element) {
				index = i;
				break;
			}
		}
		return index;
	}
	
	public int indexOf(String element) { //returns the first index of the passed value in the array (returns -1 if it is not present)
		int index = -1;
		String cEl;
		for (int i = 0; i < arrayListString.length; i++) {
			cEl = arrayListString[i];
			if (cEl.equals(element)) {
				index = i;
				break;
			}
		}
		return index;
	}
	
	private void calculateSize(String input) {
		length = 1;
		
		if (delimiter == "") { // if there is no delimiter, the array should be the same size as the input
			length = input.length();
		}else {
			String cChar;
			for (int i = 0; i < input.length(); i++) {
				cChar = input.substring(i, i+1);
				if ((cChar.equals(delimiter))) {
					length++;
				}
			}
		}
	}
	
	public void sort() { //sorts array by ascending order
		switch(arrayType) {
		case Int :
			Arrays.sort(arrayListInt);
			break;
		case Double :
			Arrays.sort(arrayListDouble);
		case String:
			Arrays.sort(arrayListString);
			break;
		case Long:
			Arrays.sort(arrayListLong);
			break;
		}
	}
	
	public void sortByAlpha(String sortMethod) {
		Exception e = new Exception("this method is empty");
		e.printStackTrace();
	}

	
	public String toString() {
		
		String stringRep = "{";
		if (arrayType.equals(Type.Int)) {
			int cChar;
			for (int i = 0; i < arrayListInt.length; i++) {
				cChar = arrayListInt[i];
				if (i == arrayListInt.length-1) {
					stringRep += "" + cChar;
				}else {
					stringRep += "" + cChar + ",";
				}
			}
		}else if (arrayType.equals(Type.String)) {
			String cChar;
			for (int i = 0; i < arrayListString.length; i++) {
				cChar = arrayListString[i];
				if (i == arrayListString.length-1) {
					stringRep += "" + cChar;
				}else {
					stringRep += "" + cChar + ",";
				}
			}
		}else if (arrayType.equals(Type.Double)) {
			double cChar;
			for (int i = 0; i < arrayListDouble.length; i++) {
				cChar = arrayListDouble[i];
				if (i == arrayListDouble.length-1) {
					stringRep += "" + cChar;
				}else {
					stringRep += "" + cChar + ",";
				}
			}
		}else if (arrayType.equals(Type.Long)) {
			long cChar;
			for (int i = 0; i < arrayListLong.length; i++) {
				cChar = arrayListLong[i];
				if (i == arrayListLong.length-1) {
					stringRep += "" + cChar;
				}else {
					stringRep += "" + cChar + ",";
				}
			}
		}
		stringRep+="}";
		return stringRep;
	}
	

	public void getValues(String value,String delimiter1) {
		delimiter = delimiter1;
		boolean repeat = false;
		int a = 0;
		if (arrayType.equals(Type.String)) {
			calculateSize(value);
			arrayListString = value.split(delimiter);
			
		}else if (arrayType.equals(Type.Int)){
			calculateSize(value);
			arrayListInt = new int[length];
			arrayListString = value.split(delimiter);
			
			for (int i = 0; i < arrayListString.length; i++) {
				do {
					try {
						arrayListInt[a] = Integer.parseInt(arrayListString[i]);	
						repeat = false;
						a++;
					}catch(NumberFormatException e) {				
						System.out.println(arrayListString[i]);
						length = length - 1;
						repeat = true;
						i++;
					}
				}while (repeat);
			}
		}else if (arrayType.equals(Type.Long)){
			calculateSize(value);
			arrayListLong = new long[length];
			arrayListString = value.split(delimiter);
			
			for (int i = 0; i < arrayListString.length; i++) {
				do {
					try {
						arrayListLong[a] = Long.parseLong(arrayListString[i]);	
						repeat = false;
						a++;
					}catch(NumberFormatException e) {				
						System.out.println(arrayListString[i]);
						length = length - 1;
						repeat = true;
						i++;
					}
				}while (repeat);
			}
		}else if (arrayType.equals(Type.Double)) {
			calculateSize(value);
			arrayListDouble = new double[length];
			arrayListString = value.split(delimiter);
			
			for (int i = 0; i < arrayListString.length; i++) {
				do {
					try {
						arrayListDouble[a] = Double.parseDouble(arrayListString[i]);	
						repeat = false;
						a++;
					}catch(NumberFormatException e) {				
						System.out.println(arrayListString[i]);
						length = length - 1;
						repeat = true;
						i++;
					}catch(ArrayIndexOutOfBoundsException q) {
						System.out.println("ERROR: BAD-INPUT in array.getValues");		
					}
				}while (repeat);
			}
		}
		resizeArrayList();

	}
	
	public void getValues() {	
		String value = JOptionPane.showInputDialog("What is the array?");
		boolean repeat = false;
		int a = 0;
		if (arrayType.equals(Type.String)) {
			calculateSize(value);
			arrayListString = value.split(delimiter);
			
		}else if (arrayType.equals(Type.Int)){
			calculateSize(value);
			arrayListInt = new int[length];
			arrayListString = value.split(delimiter);
			
			for (int i = 0; i < arrayListString.length; i++) {
				do {
					try {
						arrayListInt[a] = Integer.parseInt(arrayListString[i]);	
						repeat = false;
						a++;
					}catch(NumberFormatException e) {				
						System.out.println(arrayListString[i]);
						length = length - 1;
						repeat = true;
						i++;
					}
				}while (repeat);
			}
		}else if (arrayType.equals(Type.Double)) {
			calculateSize(value);
			arrayListDouble = new double[length];
			arrayListString = value.split(delimiter);
			
			for (int i = 0; i < arrayListString.length; i++) {
				do {
					try {
						arrayListDouble[a] = Double.parseDouble(arrayListString[i]);	
						repeat = false;
						a++;
					}catch(NumberFormatException e) {				
						System.out.println(arrayListString[i]);
						length = length - 1;
						repeat = true;
						i++;
					}
				}while (repeat);
			}
		}
		resizeArrayList();
	}
	
	public String[] getArray(String a) {
		return arrayListString;
	}
	
	public int[] getArray(int a) {
		return arrayListInt;
	}
	
	public double[] getArray(double a) {
		return arrayListDouble;
	}
	
	public Type getType() {
		return arrayType;
	}
	
	private void resizeArrayList() {
		int len = length;
		switch(arrayType) {
			case Int :
				if (length > arrayListInt.length) len = arrayListInt.length;
				int[] postArrayInt = new int[length];
				for (int i = 0; i < len; i++) {
					postArrayInt[i] = arrayListInt[i];
				}
				arrayListInt = postArrayInt;
				break;
			case Double :
				if (length > arrayListDouble.length) len = arrayListDouble.length;
				double[] postArrayDouble = new double[length];
				for (int i = 0; i < len; i++) {
					postArrayDouble[i] = arrayListDouble[i];
				}
				arrayListDouble = postArrayDouble;
				break;
			case String:
				if (length > arrayListString.length) len = arrayListString.length;
				String[] postArrayString = new String[length];
				for (int i = 0; i < len; i++) {
					postArrayString[i] = arrayListString[i];
				}
				arrayListString = postArrayString;
				break;
		default:
			break;
		}	
	}

}
