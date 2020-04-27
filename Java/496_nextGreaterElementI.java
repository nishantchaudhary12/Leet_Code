/*You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

 */

import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> indx = new HashMap<>();

        for(int i=0; i<nums2.length; i++){
            indx.put(nums2[i], i);
        }

        int[] arr = new int[nums1.length];
        for(int i=0; i<nums1.length; i++){
            boolean flag = true;
            for(int j=indx.get(nums1[i])+1; j<nums2.length; j++){
                if(nums1[i] < nums2[j]){
                    arr[i] = nums2[j];
                    flag = false;
                    break;
                }
            }
            if(flag){
                arr[i] = -1;
            }
        }

        return arr;
    }
}