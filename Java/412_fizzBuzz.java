/*Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
 */

import java.util.ArrayList;

class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> arr = new ArrayList<String>();
        for(int i=1; i<=n; i++){
            if(i%5 == 0 && i%3 == 0){
                arr.add("FizzBuzz");
            }else if(i%3 == 0){
                arr.add("Fizz");
            }else if(i%5 == 0){
                arr.add("Buzz");
            }else{
                arr.add(String.valueOf(i));
            }
        }
        return arr;
    }
}