convert_to_binary<- function(n) {
if(n > 1) {
convert_to_binary(as.integer(n/2))
 }
cat(n %% 2)
}


input = readline(prompt="Enter a number: ")
number <- as.integer(input)
convert_to_binary(number)

