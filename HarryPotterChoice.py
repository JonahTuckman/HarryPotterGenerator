"""Will choose a random Harry Potter movie to watch"""

from random import randint 
import time

print("Harry Potter tonight? Great Choice!")

choices = ["Harry Potter and the Sorcerers Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half Blood Prince", "Harry Potter and the Deathly Hallows Part 1", "Harry Potter and the Deathly Hallows Part 2"]

final = choices[randint(0,7)]
time.sleep(2)
print("Then lets watch " + str(final))

