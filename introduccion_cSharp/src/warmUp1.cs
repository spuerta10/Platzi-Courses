namespace warmUp1 
{
    public class warmUp1
    {
        public bool sleepIn(bool weekDay, bool vacation)
        /*
        The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. 
        We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.

        Test Cases:
        sleepIn(false, false) → true
        sleepIn(true, false) → false
        sleepIn(false, true) → true
        */
        {
            if (!weekDay || vacation){return true;}
            return false;
        }

        public bool monkeyTrouble(bool aSmile, bool bSmile)
        /*
        We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling. 
        We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.
        Test Cases:
        monkeyTrouble(true, true) → true
        monkeyTrouble(false, false) → true
        monkeyTrouble(true, false) → false
        */
        {
            if ((aSmile && bSmile) || (!aSmile && !bSmile)){return true;}
            return false;
        }

        public int sumDouble(int a, int b)
        /*
        Given two int values, return their sum. Unless the two values are the same, then return double their sum.
        Test Cases:
        sumDouble(1, 2) → 3
        sumDouble(3, 2) → 5
        sumDouble(2, 2) → 8
        */
        {
            if (a == b){return 2*(a+b);}
            return a+b;
        }

        public int diff21(int n)
        /*
        Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
        Test Cases:
        diff21(19) → 2
        diff21(10) → 11
        diff21(21) → 0
        */
        {
            if(n <= 21){return (21 - n);}
            return 2*(n-21);
        }


        public bool parrotTrouble(bool talking, int hour)
        /*
        We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
        We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.
        Test Cases:
        parrotTrouble(true, 6) → true
        parrotTrouble(true, 7) → false
        parrotTrouble(false, 6) → false
        */
        {
            if (((hour < 7))&&talking || ((hour > 20))&&talking){return true;}
            return false;
        }


        public bool makes10(int a, int b)
        /*
        Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.
        Test Cases:
        makes10(9, 10) → true
        makes10(9, 9) → false
        makes10(1, 9) → true
        */
        {
            if(((a == 10)||(b == 10))||(a+b == 10)){return true;}
            return false;
        }


        public bool nearHundred(int n)
        /*
        Given an int n, return true if it is within 10 of 100 or 200.
        Test Cases:
        nearHundred(93) → true
        nearHundred(90) → true
        nearHundred(89) → false
        */
        {
            if ((Math.Abs(100 - n) <= 10)||(Math.Abs(200 - n) <= 10)){return true;}
            return false;
        }


        public bool posNeg(int a, int b, bool negative)
        /*
        Given 2 int values, return true if one is negative and one is positive. Except if the parameter "negative" is true, then return true only if both are negative.
        Test Cases:
        posNeg(1, -1, false) → true
        posNeg(-1, 1, false) → true
        posNeg(-4, -5, true) → true
        */
        {
            if(negative){return(a < 0 && b < 0);}
            return ((a < 0 && !(b < 0))||(!(a < 0) && b < 0));
        }


        public string notString(string str)
        {
            if(str.Equals("not") || str.Equals("not " + str)){return str;}
            return "not " + str;
        }

        public string missingChar(string str, int n)
        /*
        Given a non-empty string and an int n, return a new string where the char at index n has been removed.
        Test Cases:
        missingChar("kitten", 1) → "ktten"
        missingChar("kitten", 0) → "itten"
        missingChar("kitten", 4) → "kittn"
        */
        {
            return str.Remove(n, 1);
        }

        public string frontBack(string str)
        /*
        Given a string, return a new string where the first and last chars have been exchanged.
        Test Cases:
        frontBack("code") → "eodc"
        frontBack("a") → "a"
        frontBack("ab") → "ba"
        */
        {
            char[] charArray = str.ToCharArray();
            var ans = "";
            for (int i = (charArray.Length - 1); i >= 0; i--)
            {
                ans += charArray[i];
            }
            return ans;
        }

        public string front3(string str)
        /*
        Given a string, we'll say that the front is the first 3 chars of the string. 
        If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
        Test Cases:
        front3("Java") → "JavJavJav"
        front3("Chocolate") → "ChoChoCho"
        front3("abc") → "abcabcabc"
        */
        {
            if(str.Length < 3){return str + str + str;}
            var first3 = str.Substring(0,3);
            return first3 + first3 + first3;
        }

        public string backAround(string str)
        /*
        Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" yields "tcatt".
        Test Cases:
        backAround("cat") → "tcatt"
        backAround("Hello") → "oHelloo"
        backAround("a") → "aaa"
        */
        {
            var lastChar = str.Substring(str.Length -1);
            return lastChar + str + lastChar;
        }

        public bool or35(int n)
        /*
        Return true if the given non-negative number is a multiple of 3 or a multiple of 5.
        */
        {
            return((n%3==0)||(n%5==0));
        }


        public static void Main(string[] args)
        {
            warmUp1 answer = new warmUp1();
            Console.WriteLine(answer.frontBack("kitten"));    
        }


    }
}
