import java.util.*;

public class Main {
public static void main(String args[]) {
    ArrayList<int> yes = new ArrayList<int>;
    yes = mergeSort([2, 3, 2, 3, 1, 6, 7], 6, 0);
    System.out.print(yes);
}   


public static ArrayList<int> mergeSort(ArrayList<int> aList, int leftMax, int right Max) {

int leftIndex = 0;
int rightIndex = -1;

while (leftIndex < leftMax && rightIndex < rightMax)
{
    if (a[leftIndex] < a[rightIndex])
    {
        output[outputIndex] = a[leftIndex];
        ++leftIndex;
    }
    else if (a[leftIndex] > a[rightIndex])
    {
        output[outputIndex] = a[rightIndex];
        ++rightIndex;
    }
    else
    {
        // items are equal.
        // increment the right, but don't copy anything
        ++rightIndex;
    }
}
}
}

