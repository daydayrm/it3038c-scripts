$random = get-random -minimum 1 -maximum 31
$attempts = 1

    while($guesses -ne $random){

$guesses = read-host -prompt "Please guess a number between 1 and 30."
      
      if($guesses -gt $random) {write-host "Too high! Guess lower."}
      if($guesses -lt $random) {write-host "Too low! Guess higher."}
      if($guesses -eq $random) {write-host "Correct!! Great guess, WOW!!"}
      
    }
