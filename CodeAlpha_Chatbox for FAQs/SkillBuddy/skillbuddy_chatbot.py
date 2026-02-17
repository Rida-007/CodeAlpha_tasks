import string
import tkinter as tk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')

# -----------------------------
# FAQs
# -----------------------------
faqs = {
#-----------------------------
# General
#-----------------------------
"Which course is best for beginners?":
"Python Programming and Web Development are best for beginners.",

"Which course has high job demand?":
    "Data Science, Cyber Security, and Web Development have high job demand.",

"Which course is best after plus two?":
    "Python Programming and Web Development are suitable after plus two.",

"Which course is best for engineering students?":
    "Data Science, Cyber Security, and Python Programming are recommended for engineering students.",

"Tell me about Python course":
    "The Python course covers programming basics, problem solving, and real-world applications.",

"Tell me about web development course":
    "The web development course focuses on building websites using frontend and backend technologies.",

"Tell me about data science course":
    "The data science course focuses on data analysis, visualization, and machine learning basics.",

"Tell me about cyber security course":
    "The cyber security course teaches system security, network protection, and ethical hacking basics.",

"Tell me about mobile app development course":
    "The mobile app development course focuses on building Android and iOS applications.",

"What is an IT course?":
    "An IT course teaches technical skills like programming, networking, and software development.",

"Who can join these courses?":
    "Students from any background with basic computer knowledge can join.",

"Are these courses beginner friendly?":
    "Yes, all courses start from basics and are suitable for beginners.",

"Do I need prior programming knowledge?":
    "No, prior programming knowledge is not mandatory for beginner courses.",

"What are the topics covered in Python?":
    "Topics include basics, loops, functions, OOP, file handling, and basic projects.",

"Is Python useful for jobs?":
    "Yes, Python is widely used in software development, data science, and automation.",

"Will I get a certificate for Python course?":
    "Yes, a certificate is provided after successful completion.",

"What are the topics covered in web development?":
    "HTML, CSS, JavaScript, frontend frameworks, and basic backend concepts are covered.",

"Is web development good for beginners?":
    "Yes, web development is a good starting point for beginners in IT.",

"Does web development provide certificate?":
    "Yes, a certificate is provided for the web development course.",

"What skills are needed for data science?":
    "Basic mathematics, statistics, and Python programming are helpful.",

"Is data science difficult?":
    "Data science may be challenging, but it can be learned step by step with practice.",

"Does data science include projects?":
    "Yes, practical projects are included in the data science course.",

"What skills are needed for cyber security?":
    "Networking basics and interest in security concepts are helpful.",

"Is cyber security a good career?":
    "Yes, cyber security has high demand and good career growth.",

"Does cyber security provide certificate?":
    "Yes, a certificate is provided after completing the course.",

"What tools are used for mobile app development?":
    "Tools include Android Studio, Flutter, or React Native.",

"Is mobile app development difficult?":
    "It is beginner friendly if you start with basics and practice regularly.",

"Does mobile app development provide certificate?":
    "Yes, a certificate is provided for mobile app development course.",

    # ----------------- Python ----------------
    "What is Python programming?":
        "Python is a programming language used for web development, data science, AI, and automation.",

    "Is the Python course free?":
        "Yes, the Python programming course is free for students.",

    "What is the duration of the Python course?":
        "The Python course duration is 8 weeks.",

    "Does Python course provide internship?":
        "Yes, a one-month internship is provided for the Python course.",

    "Is prior knowledge required for Python?":
        "No prior programming knowledge is required to learn Python.",

    "Is Python course online or offline?":
        "The Python course is conducted in online mode.",

    "Does Python course provide certificate?":
        "Yes, a certificate is provided after successful completion of the Python course.",

    # ---------------- Web Development ----------------
    "What is web development?":
        "Web development involves creating websites using HTML, CSS, JavaScript, and backend technologies.",

    "Is the web development course paid?":
        "Yes, the web development course is a paid course.",

    "What is the duration of web development course?":
        "The web development course duration is 10 weeks.",

    "Does web development provide internship?":
        "Yes, an internship is provided after completing the web development course.",

    "Is web development course online or offline?":
        "The web development course is offered in online mode.",

    "Is prior knowledge required for web development?":
        "Basic programming knowledge is preferred for web development.",

    "Does web development provide certificate?":
        "Yes, a certificate is provided after completing the web development course.",

    # ---------------- Data Science ----------------
    "What is data science?":
        "Data science involves analyzing data using statistics, Python, and machine learning.",

    "Is data science course free?":
        "No, the data science course is a paid course.",

    "What is the duration of data science course?":
        "The data science course duration is 12 weeks.",

    "Does data science provide internship?":
        "Internship is optional for the data science course.",

    "Does data science provide certificate?":
        "Yes, a certificate is provided after completing the data science course.",

    "Is prior knowledge required for data science?":
        "Basic knowledge of mathematics and Python is recommended for data science.",

    # ---------------- Cyber Security ----------------
    "What is cyber security?":
        "Cyber security focuses on protecting systems and networks from cyber attacks.",

    "Is cyber security course free?":
        "Yes, the cyber security course is free for students.",

    "What is the duration of cyber security course?":
        "The cyber security course duration is 8 weeks.",

    "Does cyber security provide internship?":
        "No, internship is not included in the cyber security course.",

    "Does cyber security provide certificate?":
        "Yes, a certificate is provided after completing the cyber security course.",

    "Is prior knowledge required for cyber security?":
        "Basic knowledge of networking is preferred for cyber security.",

    # ---------------- Mobile App Development ----------------
    "What is mobile app development?":
        "Mobile app development involves creating applications for Android and iOS devices.",

    "Is mobile app development course paid?":
        "Yes, the mobile app development course is a paid course.",

    "What is the duration of mobile app development course?":
        "The mobile app development course duration is 10 weeks.",

    "Does mobile app development provide internship?":
        "Yes, an internship is provided for the mobile app development course.",

    "Does mobile app development provide certificate?":
        "Yes, a certificate is provided after completing the mobile app development course.",

    "Is prior knowledge required for mobile app development?":
    "Basic knowledge of Java or Dart is recommended for mobile app development."

}

# -----------------------------
# NLP
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

questions = [preprocess(q) for q in faqs.keys()]
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)
    index = similarity.argmax()

    if similarity[0][index] < 0.3:
        return "Sorry, I don’t have information about that yet."
    return answers[index]

# -----------------------------
# UI Functions
# -----------------------------
def send_message(event=None):
    user_text = entry.get().strip()
    if not user_text:
        return

    add_message("You", user_text, "#00E5FF")
    entry.delete(0, tk.END)

    response = chatbot_response(user_text)
    add_message("SkillBuddy", response, "#B388FF")

def add_message(sender, message, color):
    chat_frame = tk.Frame(chat_area, bg="#0B0B0F")
    label = tk.Label(
        chat_frame,
        text=f"{sender}: {message}",
        bg="#0B0B0F",
        fg=color,
        wraplength=350,
        justify="left",
        font=("Segoe UI", 11)
    )
    label.pack(anchor="w", padx=10, pady=5)
    chat_frame.pack(fill="x", anchor="w")
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1)

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("SkillBuddy – Your Course Companion")
root.geometry("420x600")
root.configure(bg="#0B0B0F")

# -----------------------------
# Chat Area with Scrollbar
# -----------------------------
chat_canvas = tk.Canvas(root, bg="#0B0B0F", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=chat_canvas.yview)
chat_canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
chat_canvas.pack(side="top", fill="both", expand=True)

chat_area = tk.Frame(chat_canvas, bg="#0B0B0F")
chat_canvas.create_window((0, 0), window=chat_area, anchor="nw")

chat_area.bind(
    "<Configure>",
    lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
)

# Welcome message
add_message(
    "SkillBuddy",
    "Hey! 👋 I’m SkillBuddy. Ask me about IT & skill development courses.",
    "#FF4DFF"
)

# -----------------------------
# Input Area
# -----------------------------
entry_frame = tk.Frame(root, bg="#0B0B0F")
entry_frame.pack(fill="x", pady=10)

entry = tk.Entry(
    entry_frame,
    font=("Segoe UI", 12),
    bg="#1A1A2E",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(side="left", padx=10, pady=5, fill="x", expand=True)
entry.bind("<Return>", send_message)

send_btn = tk.Button(
    entry_frame,
    text="➤",
    font=("Segoe UI", 14),
    bg="#FF2EDF",
    fg="black",
    relief="flat",
    command=send_message
)
send_btn.pack(side="right", padx=10)

root.mainloop()
