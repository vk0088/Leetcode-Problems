import java.util.*;

class Solution {

    // Define a nested class to represent a lock and its steps
    static class LockPair {
        String lock; // The lock combination
        int steps;   // Number of steps taken to reach this lock

        // Constructor to initialize the lock and steps
        LockPair(String lock, int steps) {
            this.lock = lock;
            this.steps = steps;
        }
    }

    // Method to find the minimum number of turns required to reach the target lock combination
    public int openLock(String[] deadEnds, String target) {

        // Initialize a queue for breadth-first search
        Queue<LockPair> queue = new LinkedList<>();
        queue.offer(new LockPair("0000", 0)); // Start with the initial lock combination

        // Use a set to efficiently keep track of visited locks during the search
        Set<String> visited = new HashSet<>();
        visited.add("0000"); // Mark the initial lock as visited

        // Convert the array of dead-end lock combinations into a set for efficient lookup
        Set<String> deadEndSet = new HashSet<>();
        for (String deadEnd : deadEnds) {
            deadEndSet.add(deadEnd);
        }

        // Check if the initial lock combination is a dead end, if so, return -1
        if (deadEndSet.contains("0000")) return -1;

        // Perform breadth-first search
        while (!queue.isEmpty()) {
            LockPair pair = queue.poll(); // Retrieve the next lock combination from the queue
            String lock = pair.lock;      // Get the lock combination
            int steps = pair.steps;       // Get the number of steps taken so far

            // Check if the current lock combination is equal to the target, if so, return the number of steps
            if (lock.equals(target)) {
                return steps; // Return the minimum number of steps to reach the target
            }

            // Generate next possible lock combinations by rotating each digit of the lock
            for (int i = 0; i < lock.length(); i++) {
                char digit = lock.charAt(i); // Get the current digit of the lock combination
                int[] moves = {-1, 1};       // Define possible moves: decrement or increment the digit

                // Iterate through possible moves
                for (int move : moves) {
                    char possibleDigit; // Variable to store the digit after the move
                    // Handle edge cases: 0 and 9
                    if (digit == '0' && move == -1) {
                        possibleDigit = '9'; // If the current digit is 0, and the move is to decrement, wrap around to 9
                    } else if (digit == '9' && move == 1) {
                        possibleDigit = '0'; // If the current digit is 9, and the move is to increment, wrap around to 0
                    } else {
                        possibleDigit = (char) (digit + move); // Otherwise, perform the move
                    }

                    // Generate the new lock combination by replacing the current digit with the possible digit
                    char[] replacedLockArray = lock.toCharArray();
                    replacedLockArray[i] = possibleDigit;
                    String replacedLock = new String(replacedLockArray);

                    // Skip if the new lock combination has already been visited
                    if (visited.contains(replacedLock)) continue;

                    // Mark the new lock combination as visited
                    visited.add(replacedLock);

                    // If the new lock combination is not a dead end, add it to the queue for further exploration
                    if (!deadEndSet.contains(replacedLock)) {
                        queue.offer(new LockPair(replacedLock, steps + 1)); // Add the new lock combination to the queue with incremented steps
                    }
                }
            }
        }

        // If the target lock combination is not reachable, return -1
        return -1;
    }
}