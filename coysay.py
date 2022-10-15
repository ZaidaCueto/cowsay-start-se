from distutils.command.build_scripts import first_line_re
from typing import Container


userText = input("Digite uma fala para a vaquinha: ") 
words = userText.split()

if len(words) > 8:
    firstLine = "".join(words[:len](words)//2 + 1)
    secondLine = "".join(words[len(words)//2 + 1:])
    line = (len( firstLine) + 4) * "-"
    content = "| " + userText + " |\n|" + secondLine +  " |"

else:
    line = (len(userText) + 4) * "-"
    content = "│" + userText + " │"


container = [line, content, line]

for item in container:
    print(item)

cow = [
"            \\  ^__^",
"             \\ (oo)\\________ ",
"                (__)\\        \\/\\",
"                    ||----W |",
"                    ||     ||"]
for item  in  cow:
    print(item)

   

