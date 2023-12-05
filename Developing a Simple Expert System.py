import spacy

class SimpleChatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.greetings = ["hello", "hi", "hey", "greetings", "howdy"]
        self.goodbyes = ["bye", "goodbye", "see you", "farewell"]
        self.responses = {
            "how_are_you": ["I'm good, thank you!", "I'm doing well, how about you?", "All good, thanks!"],
            "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm still learning!"]
        }

    def process_input(self, user_input):
        doc = self.nlp(user_input.lower())
        tokens = [token.text for token in doc]

        # Check for greetings
        if any(greeting in tokens for greeting in self.greetings):
            return "Hello! How can I help you today?"

        # Check for goodbyes
        if any(goodbye in tokens for goodbye in self.goodbyes):
            return "Goodbye! Have a great day."

        # Check for specific questions or statements
        if "how are you" in tokens:
            return self.responses["how_are_you"][0]

        # Default response
        return self.responses["default"][0]

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if not user_input:
            break

        response = chatbot.process_input(user_input)
        print("Chatbot:", response)
