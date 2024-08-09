message = "my howercraft is full of ells"
translated = ""

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

# # Method 2
# translated = "".join([message[-1*(i+1)] for i in range(len(message))])

print(translated)
