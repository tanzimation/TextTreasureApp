# import tkinter as tk
# import nltk
# from textblob import TextBlob
# from newspaper import Article
#
#
# def summarize():
#
#     url = utext.get("1.0", "end").strip()
#
#     article = Article(url)
#
#     article.download()
#     article.parse()
#
#     article.nlp()
#
#     title.config(state='normal')
#     author.config(state='normal')
#     publication.config(state='normal')
#     summary.config(state='normal')
#     sentiment.config(state='normal')
#
#     title.delete('1.0', 'end')
#     title.insert('1.0', article.title)
#
#
#     author.delete('1.0', 'end')
#     author.insert('1.0', article.authors)
#
#     publication.delete('1.0', 'end')
#     publication.insert('1.0', article.publish_date)
#
#     summary.delete('1.0', 'end')
#     summary.insert('1.0', article.summary)
#
#     analysis = TextBlob(article.text)
#     sentiment.delete('1.0', 'end')
#     sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral" }')
#
#     title.config(state='disabled')
#     author.config(state='disabled')
#     publication.config(state='disabled')
#     summary.config(state='disabled')
#     sentiment.config(state='disabled')
#
#     title.delete('1.0', 'end')
#     title.insert('1.0', article.title)
#
#     author.delete('1.0', 'end')
#     author.insert('1.0', article.authors)
#
#     publication.delete('1.0', 'end')
#     publication.insert('1.0', article.publish_date)
#
#     summary.delete('1.0', 'end')
#     summary.insert('1.0', article.summary)
#
#
# root = tk.Tk()
# root.title("News Summarizer")
# root.geometry('1200x600')
#
# tlabel = tk.Label(root, text = "Title")
# tlabel.pack()
#
# title = tk.Text(root, height=1, width=140)
# title.config(state='disabled', bg='#1c1c1c')
# title.pack()
#
# alabel = tk.Label(root, text = "Author")
# alabel.pack()
#
# author = tk.Text(root, height=1, width=140)
# author.config(state='disabled', bg='#1c1c1c')
# author.pack()
#
#
# plabel = tk.Label(root, text = "Publication Date")
# plabel.pack()
#
# publication= tk.Text(root, height=1, width=140)
# publication.config(state='disabled', bg='#1c1c1c')
# publication.pack()
#
#
# slabel = tk.Label(root, text = "Summary")
# slabel.pack()
#
# summary= tk.Text(root, height=20, width=140)
# summary.config(state='disabled', bg='#1c1c1c')
# summary.pack()
#
# selabel = tk.Label(root, text = "Sentiment Analysis")
# selabel.pack()
#
# sentiment= tk.Text(root, height=1, width=140)
# sentiment.config(state='disabled', bg='#dddddd')
# sentiment.pack()
#
# ulabel = tk.Label(root, text = "URL")
# ulabel.pack()
#
# utext= tk.Text(root, height=1, width=140)
# utext.pack()
#
# btn = tk.Button(root, text= "Summarize", command=summarize)
# btn.pack()
#
#
#
# root.mainloop()
#
# -----------------------------------------------

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from textblob import TextBlob
from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pyttsx3

def summarize():
    url = utext.get("1.0", "end").strip()

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')

        title.delete('1.0', 'end')
        title.insert('1.0', article.title)

        author.delete('1.0', 'end')
        author.insert('1.0', ", ".join(article.authors))

        publication.delete('1.0', 'end')
        publication.insert('1.0', article.publish_date)

        summary.delete('1.0', 'end')
        summary.insert('1.0', article.summary)

        analysis = TextBlob(article.text)
        sentiment.delete('1.0', 'end')
        sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

        title.config(state='disabled')
        author.config(state='disabled')
        publication.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')

        # Word Cloud
        wordcloud = WordCloud(width=800, height=400).generate(article.text)
        plt.figure(figsize=(8, 4))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def speak_summary():
    summary_text = summary.get("1.0", "end")
    engine = pyttsx3.init()
    engine.say(summary_text)
    engine.runAndWait()

root = tk.Tk()
root.title("TextTreasure App")
root.geometry('1200x800')

# Tab Control
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Summarize')
tab_control.add(tab2, text='Settings')
tab_control.pack(expand=1, fill='both')

# Tab 1 - Summarize
tlabel = tk.Label(tab1, text="Title")
tlabel.pack()
title = ScrolledText(tab1, height=1, width=140)
title.config(state='disabled', bg='#1c1c1c')
title.pack()

alabel = tk.Label(tab1, text="Author")
alabel.pack()
author = ScrolledText(tab1, height=1, width=140)
author.config(state='disabled', bg='#1c1c1c')
author.pack()

plabel = tk.Label(tab1, text="Publication Date")
plabel.pack()
publication = ScrolledText(tab1, height=1, width=140)
publication.config(state='disabled', bg='#1c1c1c')
publication.pack()

slabel = tk.Label(tab1, text="Summary")
slabel.pack()
summary = ScrolledText(tab1, height=20, width=140)
summary.config(state='disabled', bg='#1c1c1c')
summary.pack()

selabel = tk.Label(tab1, text="Sentiment Analysis")
selabel.pack()
sentiment = ScrolledText(tab1, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(tab1, text="URL")
ulabel.pack()
utext = ScrolledText(tab1, height=1, width=140)
utext.pack()
btn_summarize = tk.Button(tab1, text="Summarize", command=summarize)
btn_summarize.pack()
btn_speak = tk.Button(tab1, text="Speak Summary", command=speak_summary)
btn_speak.pack()

# Tab 2 - Settings
# Add settings options here
# Tab 2 - Settings
settings_frame = ttk.Frame(tab2)
settings_frame.pack(fill='both', expand=1)

# Create and set default settings
dark_mode_var = tk.BooleanVar()
dark_mode_var.set(False)  # Default to light mode

# Dark Mode Toggle
dark_mode_label = tk.Label(settings_frame, text="Dark Mode")
dark_mode_label.grid(row=0, column=0, padx=10, pady=10)
dark_mode_toggle = ttk.Checkbutton(settings_frame, variable=dark_mode_var)
dark_mode_toggle.grid(row=0, column=1, padx=10, pady=10)

# Font Size Slider
font_size_label = tk.Label(settings_frame, text="Font Size")
font_size_label.grid(row=1, column=0, padx=10, pady=10)
font_size_var = tk.DoubleVar()
font_size_var.set(12)  # Default font size
font_size_slider = ttk.Scale(settings_frame, from_=10, to=20, variable=font_size_var, orient="horizontal")
font_size_slider.grid(row=1, column=1, padx=10, pady=10)

# Save Settings Button
def save_settings():
    dark_mode = dark_mode_var.get()
    font_size = font_size_var.get()
    # You can save these settings to a configuration file or database here
    messagebox.showinfo("Settings Saved", "Settings have been saved.")

save_button = tk.Button(settings_frame, text="Save Settings", command=save_settings)
save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()

