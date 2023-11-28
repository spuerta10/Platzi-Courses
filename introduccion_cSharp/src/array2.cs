public class array2
{

    public int bigDiff(int[] nums)
    /*
    Given an array length 1 or more of ints, 
    return the difference between the largest and smallest values in the array. 
    
    Test Cases:
    bigDiff([10, 3, 5, 6]) → 7
    bigDiff([7, 2, 10, 9]) → 8
    bigDiff([2, 10, 7, 2]) → 8
    */
    {
        var max = nums[0];
        var min = nums[0];
        for (int i = 0; i < nums.Length; i++)
        {
            min = Math.Min(min, nums[i]);
            max = Math.Max(max, nums[i]);
        }
        return max - min; 
    }




    public int sum13(int[] nums)
    /*
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, 
    so it does not count and numbers that come immediately 
    after a 13 also do not count.
    
    Test Case:
    sum13([1, 2, 2, 1]) → 6
    sum13([1, 1]) → 2
    sum13([1, 2, 2, 1, 13]) → 6
    */
    {
        var sum = 0;
        if(nums.Length == 0){return sum;}
        for (var i = 0; i < nums.Length; i++)
        {
            if(nums[i]==13)
            {
                nums[i] = 0;
                if(i+1 < nums.Length){nums[i+1] = 0;}
            }
            sum += nums[i];
        }
        return sum;
    }



    public int sum67(int[] nums)
    /*
    Return the sum of the numbers in the array, 
    except ignore sections of numbers starting with a 6 
    and extending to the next 7 (every 6 will be followed by at least one 7). 
    Return 0 for no numbers.

    Test Cases:
    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4
    */
    {
        var found6 = false; //flag to know when a 6 is found
        int sum = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            if(nums[i] == 6){found6 = true;}
            if(!found6){sum += nums[i];}
            if(nums[i] == 7){found6 = false;}
        } 
        return sum;  
    }


    public bool has22(int[] nums)
    /*
    Given an array of ints, return true if the array contains a 
    2 next to a 2 somewhere.

    Test Cases:
    has22([1, 2, 2]) → true
    has22([1, 2, 1, 2]) → false
    has22([2, 1, 2]) → false
    */
    {
        for (int i = 0; i < nums.Length; i++)
        {
            if(nums[i] == 2)
            {
                if((i + 1 < nums.Length) && (nums[i+1] == 2)){return true;}
            }
        }
        return false; 
    }

    public bool lucky13(int[] nums)
    /*
    Given an array of ints, return true if the array contains 
    no 1's and no 3's.

    Test Cases:
    lucky13([0, 2, 4]) → true
    lucky13([1, 2, 3]) → false
    lucky13([1, 2, 4]) → false
    */
    {
        for(var i = 0; i < nums.Length; i++)
        {
           if(nums[i] == 3 || nums[i] == 1){return false;} 
        }
        return true;
    }


    public bool sum28(int[] nums)
    /*
    Given an array of ints, return true if the sum of all the 
    2's in the array is exactly 8.

    Test Cases:
    sum28([2, 3, 2, 2, 4, 2]) → true
    sum28([2, 3, 2, 2, 4, 2, 2]) → false
    sum28([1, 2, 3, 4]) → false
    */
    {
        int sum2 = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            if(nums[i] == 2){sum2 += nums[i];}
        }
        return (sum2 == 8);
    }



    public bool more14(int[] nums)
    /*
    Given an array of ints, return true if the number of 1's is 
    greater than the number of 4's

    Test Cases:
    more14([1, 4, 1]) → true
    more14([1, 4, 1, 4]) → false
    more14([1, 1]) → true
    */
    {
        var nums1 = 0;
        var nums4 = 0;
        for (var i = 0; i < nums.Length; i++)
        {
            if(nums[i] == 1){nums1 += 1;}
            if(nums[i] == 4){nums4 += 1;}
        }
        return (nums1 > nums4);
    }


    public int[] fizzArray(int n)
    /*
    Given a number n, create and return a new int array of length
    n, containing the numbers 0, 1, 2, ... n-1. The given n may 
    be 0, in which case just return a length 0 array. 
    You do not need a separate if-statement for the length-0 
    case; the for-loop should naturally execute 0 times in that 
    case, so it just works. 
    
    Test Case:
    fizzArray(4) → [0, 1, 2, 3]
    fizzArray(1) → [0]
    fizzArray(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    */
    {
        int[] array = new int[n]; 
        for (int i =0; i < n; i++)
        {
            array[i] = i;
        }
        return array;
    }


    public bool only14(int[] nums)
    /* 
    Given an array of ints, return true if every element is a 1 
    or a 4.

    Test Cases:
    only14([1, 4, 1, 4]) → true
    only14([1, 4, 2, 4]) → false
    only14([1, 1]) → true
    */
    {
        int sumArray = 0;
        for(int i = 0; i < nums.Length; i++)
        {
            if(nums[i] == 1 || nums[i] == 4){sumArray += 1;}
        }
        return (sumArray == nums.Length); 
    }


    public string[] fizzArray2(int n)
    /*
    Given a number n, create and return a new string array of 
    length n, containing the strings "0", "1" "2" .. through n-1.
    N may be 0, in which case just return a length 0 array. 

    Test Cases:
    fizzArray2(4) → ["0", "1", "2", "3"]
    fizzArray2(10) → ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fizzArray2(2) → ["0", "1"]
    */
    {
        string[] array = new string[n]; 
        for (int i =0; i < n; i++)
        {
            array[i] = "" + i;
        }
        return array;
    }



    public static void main(string[] args)
    {
        array2 ans = new array2(); 
    }
}