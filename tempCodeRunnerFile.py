import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import random
from textblob import TextBlob

positive_emotions = ["happy", "excited", "energetic", "joyful", "brave", "optimistic", "content", "enthusiastic", "ecstatic", "grateful"]
negative_emotions = ["sad", "grief", "lousy", "unexcited", "depressed", "anxious", "angry", "worried", "disappointed", "frustrated"]

def categorize_emotion(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    elif any(word in text.lower() for word in negative_emotions):
        return "Negative"
    elif any(word in text.lower() for word in positive_emotions):
        return "Positive"
    else:
        return "Unknown"

positive_destinations = [
    "Jaipur", "Udaipur", "Goa", "Manali", "Agra",
    "Rishikesh", "Darjeeling", "Kerala Backwaters",
    "Mysore", "Puducherry", "Shimla",
    "Leh-Ladakh", "Jaisalmer", "Andaman and Nicobar Islands"  
]

negative_destinations = [
    "Varanasi", "Kolkata", "Mumbai", "Delhi", "Bangalore",
    "Chennai", "Hyderabad", "Ahmedabad",
    "Pune", "Lucknow", "Kanpur"
]

def generate_response(cluster_label):
    if cluster_label == 0:
        destination = random.choice(positive_destinations)
        return f"Seems like you are pretty Positive right now. You should visit {destination}."
    elif cluster_label == 1:
        destination = random.choice(negative_destinations)
        return f"Seems like you are feeling Negative right now. Maybe a visit to {destination} will help uplift your spirits."


texts = [
    "I can't wait for my vacation! I'm so excited!",
    "Feeling sad today, missing my family.",
    "This job interview went really well, I'm feeling optimistic about it!",
    "I'm so frustrated with this project, nothing seems to be working!",
    "I'm feeling grateful for the support I received from my friends.",
    "The movie was so joyful and heartwarming, it put me in a good mood!",
    "I'm anxious about the upcoming presentation; I hope it goes well.",
    "This news is disappointing; I was hoping for a better outcome.",
    "The concert was amazing! I felt ecstatic throughout the performance.",
    "I'm feeling content and at peace with myself after a relaxing day.",
    "I feel guilty for not spending enough time with my loved ones.",
    "I'm worried about the future and whether I'll be able to achieve my goals.",
    "My relationship is going through a rough patch, and I'm feeling lonely and disconnected.",
    "I'm angry at myself for making the same mistakes over and over again.",
    "I feel guilty for not spending enough time with my loved ones.",
    "The news of the accident left me feeling shocked and shaken.",
    "I'm embarrassed by my performance in front of others.",
    "I'm frustrated with the current situation and the lack of progress.",
    "I'm feeling bored and uninspired with my daily routine.",
    "I'm disappointed by the results of the exam, even though I studied hard.",
    "I'm feeling anxious about the upcoming presentation.",
    "I'm feeling overwhelmed by the workload and deadlines.",
    "I'm feeling stressed out due to financial problems.",
    "I'm feeling sad because my plans got canceled.",
    "I'm feeling down because I had an argument with my friend.",
]

emotion_categories = [categorize_emotion(text) for text in texts]

for i, text in enumerate(texts):
    print(f"Text: '{text}' - Emotion: {emotion_categories[i]}")

num_clusters = 2  #2 emotions
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

emotion_counts = np.array([[text.count(e) for e in ["Positive", "Negative"]] for text in emotion_categories])

kmeans.fit(emotion_counts)

cluster_labels = kmeans.labels_

for i, text in enumerate(texts):
    print(f"Text: '{text}' - Cluster: {cluster_labels[i]}")

for i, label in enumerate(cluster_labels):
    response = generate_response(label)
    print(f"{i+1}: {response}")


def model_input(chat_input:str):
    custom_input = chat_input #input("Enter your own sentence: ") #Input section the only place where you can input and this section is what the chat bot should accept

    custom_input_emotion = categorize_emotion(custom_input)

    custom_input_emotion_counts = np.array([[custom_input_emotion.count(e) for e in ["Positive", "Negative"]]])

    custom_input_cluster_label = kmeans.predict(custom_input_emotion_counts)

    response = generate_response(custom_input_cluster_label[0])
    print(f"{response}") #this response must be the output from the ChatBot
    return response
