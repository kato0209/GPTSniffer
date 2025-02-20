<?php
function sequentialSearchSorted($arr, $searchElement) {
    for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] == $searchElement) {
            return $i; // Element found
        }
        if ($arr[$i] > $searchElement) {
            break; // Element not in the list
        }
    }
    return -1; // Element not found
}

// Example usage with a sorted array
$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
$searchElement = 7;
$result = sequentialSearchSorted($arr, $searchElement);

if ($result != -1) {
    echo "Element found at index: $result";
} else {
    echo "Element not found.";
}
?>
