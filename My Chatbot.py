import tkinter as tk
from tkinter import messagebox
import random
import os
import pyttsx3
import time
import threading
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk 


# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Create a stop event for threading
stop_event = threading.Event()

# Define updated responses and jokes
responses = {
    "anxiety": {
        "triggers": [
            "worried", "nervous", "tense", "overwhelmed", "panic", "fearful", "conflicted",
            "trapped", "helpless", "hopeless", "worthless", "desperate", "lost", "abandoned",
            "isolated", "alone", "sad", "depressed", "can't relax", "agitated", "anxiety",
            "attack", "bad"
        ],
        "greetings": ["hello", "hi", "hey", "howdy", "hola"],
        "responses": [
            "It's understandable to feel concerned about that. Would you like to talk more about what's worrying you?",
            "It's okay to feel nervous sometimes. Is there anything specific making you feel this way?",
            "I hear you. Taking deep breaths or trying some relaxation techniques might help. Would you like to try?",
            "Feeling overwhelmed can be tough. Let's break things down together. What's the most pressing thing you need to address?",
            "It sounds like you're having a tough time. Let's focus on your breathing. Take deep breaths with me, in and out.",
            "Fear can be powerful, but remember, you're not alone. We can work through this together. What can I do to support you?",
            "It's hard when your mind feels like it's in overdrive. Let's try some grounding exercises together to help slow things down.",
            "Relaxation can be challenging, but let's find something that helps you unwind. Would you like to try a guided meditation or listen to calming music?",
            "It's tough when your mind feels scattered. Let's take a short break and come back to it. Would you like to take a walk or do something else to clear your mind?",
            "Constantly feeling on edge can be exhausting. Let's explore some coping strategies together. What helps you feel more grounded?",
            "I understand. Irritability often accompanies anxiety. Let's figure out what's triggering it. Is there something specific bothering you?",
            "Sleep disturbances can be tough. Let's establish a bedtime routine to help you relax. Would you like to try some calming activities before bed?",
            "A racing heart can be scary, but it's often a symptom of anxiety. Let's focus on slowing down your breathing together.",
            "Sweating can be a physical reaction to stress. Let's find a cool, quiet space where you can take some deep breaths and relax.",
            "It sounds like your body is reacting to stress. Let's try some grounding exercises together to help you feel more stable.",
            "Agitation is a common response to anxiety. Let's find a calming activity to help you relax. Would you like to try some gentle stretching?",
            "Feeling strained can be exhausting. Let's find ways to lighten your load. Is there something I can help you with?",
            "Feeling uneasy is tough, but it's okay to feel this way sometimes. Let's explore what might be causing it. Is there something on your mind?",
            "Anxiety can be overwhelming, but remember, you're not alone. Let's talk about what's causing your anxiety and how we can address it together.",
            "Palpitations can be frightening, but they're often a symptom of anxiety. Let's focus on slowing down your breathing together.",
            "Shortness of breath can be distressing, but focusing on your breath can help. Let's try some deep breathing exercises together.",
            "Clenching your jaw is a common response to stress. Let's try some relaxation techniques together to help ease the tension.",
            "Muscle tension is a common physical symptom of anxiety. Let's try some gentle stretching exercises to help relieve the tension.",
            "An upset stomach is often a sign of stress. Let's try some soothing herbal tea or gentle foods to help settle your stomach.",
            "Dizziness can be disorienting, but it's often a symptom of anxiety. Let's find a quiet place where you can sit down and rest for a moment.",
            "Headaches can be tough to deal with, especially when they're persistent. Let's try some relaxation techniques to help ease the tension.",
            "Fatigue is a common symptom of anxiety. Let's take things slowly and focus on self-care.",
            "Avoidance can sometimes feel like the easiest option, but it can also perpetuate anxiety. Let's explore ways to face your fears together.",
            "It's natural to feel apprehensive sometimes, but it's important not to let fear hold you back. Let's talk about your concerns and how we can address them.",
            "Feeling jittery is a common symptom of anxiety. Let's find a calming activity to help you relax. Would you like to try some deep breathing exercises?",
            "Fidgeting can be a sign of nervousness. Let's find a way to channel that nervous energy into something productive. Would you like to try going for a walk?",
            "Hyperventilating can be scary, but it's often a symptom of anxiety. Let's focus on slowing down your breathing together.",
            "Feeling frazzled is tough, but it's important to take breaks and practice self-care.",
            "Distress can be overwhelming, but it's important to reach out for support. Let's talk about what's distressing you and how we can help.",
            "Feeling aggravated is tough, but it's important to find healthy ways to manage your anger. Let's talk about what's bothering you and how we can address it.",
            "Feeling stressed out is tough, but it's important to take breaks and practice self-care. Let's talk about some strategies to help you relax.",
            "Feeling frantic can be overwhelming, but it's important to take a step back and focus on what's most important. Let's prioritize your tasks together.",
            "Feeling hesitant is natural, especially when faced with uncertainty. Let's explore your concerns together. Is there something specific you're hesitant about?",
            "Feeling timid can be tough, but it's important to remember your strengths. Let's focus on building your confidence. What's one thing you feel confident about?",
            "Feeling shaky can be unsettling, but it's often a symptom of anxiety. Let's try some grounding exercises together to help you feel more stable.",
            "Feeling unsteady can be disorienting, but it's important to find ways to steady yourself. Let's find a quiet place where you can sit down and rest for a moment.",
            "Feeling skittish can be tough, especially when you're feeling on edge. Let's find a calming activity to help you relax. Would you like to try some deep breathing exercises?",
            "Feeling wary is natural, especially when faced with uncertainty. Let's explore your concerns together. Is there something specific you're wary of?",
            "Feeling jumpy is a common response to anxiety. Let's find a quiet place where you can sit down and take some deep breaths to help calm your nerves.",
            "Feeling paranoid can be distressing, but it's important to remember that your thoughts aren't always accurate reflections of reality. Let's talk through your concerns together.",
            "Feeling self-conscious is tough, but it's important to remember that everyone has insecurities. Let's focus on building your confidence. What's one thing you like about yourself?",
            "Feeling panicky can be overwhelming, but it's important to remember that panic attacks are temporary. Let's focus on slowing down your breathing together.",
            "Feeling cautious is natural, especially when faced with uncertainty. Let's explore your concerns together. Is there something specific you're cautious about?",
            "Feeling indecisive is tough, but it's important to trust your instincts. Let's talk through your options together. Is there something specific you're struggling to decide?",
            "Feeling agonized is tough, but it's important to reach out for support. Let's talk about what's agonizing you and how we can help.",
            "Feeling pained is tough, especially when it's emotional pain. Let's talk about what's causing you pain and how we can address it together.",
            "Feeling restive is tough, but it's important to find ways to relax and unwind. Let's talk about some strategies to help you feel more at ease.",
            "A throbbing heart can be a sign of anxiety, but it's important to remember to take deep breaths and try to calm yourself. Let's try some relaxation exercises together.",
            "Feeling aflutter can be unsettling, especially when you're feeling anxious. Let's find a calming activity to help you relax. Would you like to try some deep breathing exercises?",
            "Experiencing goosebumps is a common physical response to anxiety. Let's find a quiet place where you can sit down and take some deep breaths to help calm your nerves.",
            "Feeling startled can be unsettling, but it's important to remember that it's a normal response to unexpected stimuli. Let's take a moment to catch our breath and calm down.",
            "Feeling intense emotions can be overwhelming, but it's important to remember that they're temporary. Let's find a calming activity to help you relax. Would you like to try some deep breathing exercises?",
            "Feeling dread is tough, but it's important to remember that things aren't always as bad as they seem. Let's talk through your concerns together and come up with a plan.",
            "Feeling apprehensive is natural, especially when faced with uncertainty. Let's explore your concerns together. Is there something specific you're apprehensive about?",
            "Feeling perplexed is tough, especially when you're feeling overwhelmed. Let's break things down together and try to make sense of what's going on.",
            "Feeling disturbed is tough, but it's important to reach out for support. Let's talk about what's distressing you and how we can address it together.",
            "Feeling uneasy is natural, especially when faced with uncertainty. Let's explore your concerns together and come up with a plan.",
            "Feeling agitated is tough, but it's important to find ways to calm yourself down. Let's talk about some strategies to help you relax."
        ],
        "exercises": [
            "Try some deep breathing exercises: Inhale deeply through your nose for 4 counts, hold for 4 counts, exhale slowly through your mouth for 4 counts, and pause for 4 counts.",
            "Practice progressive muscle relaxation: Tense and then slowly release each muscle group in your body, starting from your toes and working up to your head.",
            "Go for a walk in nature or do some gentle stretching to help calm your mind and body.",
            "Try a short mindfulness meditation: Find a quiet place, focus on your breath, and gently bring your mind back whenever it starts to wander.",
            "Listen to calming music or nature sounds to help soothe your mind and create a relaxing atmosphere."
        ]
    },
    "hobbies": {
        "responses": [
            "What hobbies do you enjoy?",
            "Do you have any favorite pastimes?",
            "What activities do you find most relaxing?",
            "Are there any new hobbies you'd like to try?",
            "What do you like to do in your free time?"
        ]
    },
    "general": {
        "responses": [
            "I understand that you're feeling overwhelmed right now. Can you tell me more about what's going on?",
            "It sounds like you're having a tough time. Would you like to talk about it?",
            "I'm here to listen. What's been on your mind lately?",
            "Sometimes it helps to talk things out. What’s been troubling you?",
            "It’s okay to feel this way. Let’s see if we can work through it together."
        ]
    }
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired!",
    "How does a penguin build its house? Igloos it together!"
]


def get_response(user_input):
    user_input = user_input.lower()
    
    if any(greeting in user_input for greeting in responses["anxiety"]["greetings"]):
        return "Hello! How can I assist you today?"
    
    if any(keyword in user_input for keyword in ["hobby", "hobbies", "pastime", "activity"]):
        return random.choice(responses["hobbies"]["responses"])
    
    if any(trigger in user_input for trigger in responses["anxiety"]["triggers"]):
        return random.choice(responses["anxiety"]["responses"])
    
    if any(keyword in user_input for keyword in ["exercise", "relaxation", "anxiety relief", "calm", "relieve"]):
        return "Try this anxiety-relief exercise: " + random.choice(responses["anxiety"]["exercises"])
    
    if 'joke' in user_input:
        return random.choice(jokes)
    
    return random.choice(responses["general"]["responses"])

def speak_text(text):
    def speak():
        tts_engine.say(text)
        tts_engine.runAndWait()
    
    threading.Thread(target=speak).start()

def display_response_animated(response):
    canvas.delete("response_text")
    
    # Create a text item with a specific width to allow word wrapping
    text_display_id = canvas.create_text(
        10, 10, 
        text="ANXI_TALK: ", 
        anchor="nw", 
        fill="black", 
        font=('Arial', 12, 'bold'), 
        width=680,  # Set a width for the text box to wrap text at the border
        tags="response_text"
    )
    
    # Animate the response
    for char in response:
        canvas.insert(text_display_id, "end", char)
        app.update()
        time.sleep(0.05)

    # Use threading to speak the response
    threading.Thread(target=speak_text, args=(response,)).start()


def handle_user_input():
    user_input = user_entry.get()
    if user_input.strip():
        response = get_response(user_input)
        display_response_animated(response)
        user_entry.delete(0, tk.END)

def play_music():
    music_path = "C:\\Users\\Ahmad Nisar\\Desktop\\Weather App\\music.mp3"
    if os.path.exists(music_path):
        os.startfile(music_path)
    else:
        messagebox.showerror("Error", "Music file not found!")

def clear_chat():
    canvas.delete("all")
    canvas.create_image(0, 0, image=background_image, anchor="nw")

def calling_helpline():
    emergency_numbers = (
        "Emergency Services (Police, Ambulance, Fire): 15\n"
        "National Emergency Helpline: 116\n"
        "Mental Health Helpline (Pakistan): 0304-111-0066\n"
        "Child Protection Helpline: 1099\n"
        "Domestic Violence Helpline: 1099\n"
        "Anti-Terrorism Helpline: 0300-876-1010\n"
    )
    display_response_animated("Here are some emergency numbers you can contact:\n" + emergency_numbers)

# Create the main application window
app = tk.Tk()
app.title("ANXI_TALK")
app.geometry("700x600")
app.configure(bg='#e0f7fa')

# Load and resize the image
image_path = "C:\\Users\\Ahmad Nisar\\Downloads\\vecteezy_artificial-intelligence-chat-bot-concept_21477545_150\\image.png"
image = Image.open(image_path)
image = image.resize((700, 300), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

# Create a Canvas widget
canvas = tk.Canvas(app, width=700, height=300, bg='#e0f7fa')
canvas.pack()
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create the entry field for user input
user_entry = tk.Entry(app, width=60, font=('Arial', 14))  # Adjust font size here
user_entry.pack(pady=10)

# Create the submit button
submit_button = tk.Button(app, text="Send", command=handle_user_input, bg='#4caf50', fg='#ffffff', font=('Arial', 14))
submit_button.pack(pady=5)

# Create other buttons and functionalities
exercise_button = tk.Button(app, text="Get Relaxation Exercise", command=lambda: display_response_animated("Try this anxiety-relief exercise: " + random.choice(responses["anxiety"]["exercises"])), bg='#03a9f4', fg='#ffffff', font=('Arial', 14))
exercise_button.pack(pady=5)

play_button = tk.Button(app, text="Play Music", command=play_music, bg='#ff9800', fg='#ffffff', font=('Arial', 14))
play_button.pack(pady=5)

clear_button = tk.Button(app, text="Clear Chat", command=clear_chat, bg='#9e9e9e', fg='#ffffff', font=('Arial', 14))
clear_button.pack(pady=5)

emergency_button = tk.Button(app, text="Helpline", command=calling_helpline, bg='#e91e63', fg='#ffffff', font=('Arial', 14))
emergency_button.pack(pady=5)

# Run the application
app.mainloop()