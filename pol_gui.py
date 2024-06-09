import tkinter as tk
from tkinter import messagebox
import random

# Граматична інформація
grammar_info = """
Польські іменники відмінюються за сімома відмінками:
1) mianownik - називний (Хто? Що?),
2) dopełniacz - родовий (Кого? Чого?),
3) celownik - давальний (Кому? Чому?),
4) biernik - знахідний (Кого? Що?),
5) narzędnik - орудний (Ким? Чим?),
6) miejscownik - місцевий (На кому? На чому?),
7) wołacz - кличний.

Іменники жіночого роду в польській мові діляться на три групи:
I - іменники з закінченням на -а (з основою на твердий приголосний, м'який або історично м'який приголосний): sowa, kobieta, kreda;
II - іменники з закінченням на -i (з основою на м'який або історично м'який приголосний): pani, sprzedawczyni, gospodyni;
III - іменники з нульовим закінченням і основою на м'який або історично м'який приголосний: rzecz, noc, wieś, dłoń. 
"""

# Дані про слово "kicia" та його граматичні форми
word_data = {
    "kicia": {
        "Називний відмінок однини": "kicia",
        "Родовий відмінок однини": "kici",
        "Давальний відмінок однини": "kici",
        "Знахідний відмінок однини": "kicię",
        "Орудний відмінок однини": "kicią",
        "Місцевий відмінок однини": "kici",
        "Кличний відмінок однини": "kiciu",
        "Називний відмінок множини": "kicie",
        "Родовий відмінок множини": "kić",
        "Давальний відмінок множини": "kiciom",
        "Знахідний відмінок множини": "kicie",
        "Орудний відмінок множини": "kiciami",
        "Місцевий відмінок множини": "kiciach",
        "Кличний відмінок множини": "kicie",
    }
}


def create_quiz():
    key, values = random.choice(list(word_data.items()))
    grammar_case, correct_answer = random.choice(list(values.items()))
    question = f"{grammar_case} слова \"{key}\" це:"
    correct_index = random.randint(0, 3)

    all_forms = [form for form in values.values() if form != correct_answer]
    if len(all_forms) < 3:
        answers = [correct_answer] * 3
    else:
        answers = random.sample(all_forms, 3)
    answers.insert(correct_index, correct_answer)

    return question, answers, correct_index


class LanguageLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Вивчення польської мови")
        self.geometry("500x340")

        # Вікно з теорією
        self.init_grammar_window()

        # Вікно з практикою
        self.init_quiz_window()

    def init_grammar_window(self):
        self.grammar_frame = tk.Frame(self)
        self.grammar_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.grammar_frame, text=grammar_info, wraplength=480).pack(padx=10, pady=10)
        tk.Button(self.grammar_frame, text="Перейти до практики", command=self.show_quiz_window).pack()

    def init_quiz_window(self):
        self.quiz_frame = tk.Frame(self)
        
        self.quiz_question, self.quiz_answers, self.correct_index = create_quiz()
        tk.Label(self.quiz_frame, textvariable=tk.StringVar(value=self.quiz_question), wraplength=480).pack(padx=10, pady=10)
        self.var = tk.IntVar(value=-1)
        for i, answer in enumerate(self.quiz_answers):
            tk.Radiobutton(self.quiz_frame, text=answer, variable=self.var, value=i).pack(anchor='w')
        tk.Button(self.quiz_frame, text="Відповісти", command=self.check_answer).pack(pady=10)
        tk.Button(self.quiz_frame, text="Назад до теорії", command=self.show_grammar_window).pack()

    def show_grammar_window(self):
        self.quiz_frame.pack_forget()
        self.init_grammar_window()

    def show_quiz_window(self):
        self.grammar_frame.pack_forget()
        self.quiz_frame.pack(fill=tk.BOTH, expand=True)

    def check_answer(self):
        if self.var.get() == self.correct_index:
            messagebox.showinfo("Результат", "Правильно!")
        else:
            correct_answer = self.quiz_answers[self.correct_index]
            messagebox.showerror("Результат", f"Ні, правильна відповідь: \"{correct_answer}\"")
        self.refresh_quiz()

    def refresh_quiz(self):
        self.quiz_question, self.quiz_answers, self.correct_index = create_quiz()
        self.show_quiz_window()

if __name__ == "__main__":
    app = LanguageLearningApp()
    app.mainloop()
