import pyjokes

for i in range(3):
    joke = pyjokes.get_joke()
    print(joke)