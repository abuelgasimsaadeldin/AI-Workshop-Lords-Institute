import tkinter as tk
from transformers import pipeline

# -----------------------------
# Load the GPT-2 text generator
# -----------------------------
# Using GPT-2 as a lightweight example.
# For bigger models, consider using microsoft/phi-2 (not recommended on CPU).
# It is not a real chatbot model but works for demo purposes.
generator = pipeline("text-generation", model="gpt2")

# -----------------------------
# Function to generate AI response
# -----------------------------
def generate_text(user_input):
    output = generator(
        user_input,
        max_length=60,
        num_return_sequences=1,
        pad_token_id=50256
    )
    return output[0]["generated_text"]

# Function to handle sending text
def send_prompt(event=None):
    user_input = entry.get()
    if user_input.strip():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_input}\n", "user")
        chat_area.insert(tk.END, "\n")
        chat_area.yview(tk.END)
        chat_area.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

        model_response = generate_text(user_input)

        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"AI: {model_response}\n", "ai")
        chat_area.insert(tk.END, "\n")
        chat_area.yview(tk.END)
        chat_area.config(state=tk.DISABLED)

root = tk.Tk()
root.title("🤖 Simple Chatbot (GPT-2)")
root.geometry("650x550")
root.minsize(550, 420)
root.configure(bg="#f0f2f5")

chat_area = tk.Text(
    root,
    wrap=tk.WORD,
    width=65,
    height=22,
    state=tk.DISABLED,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#333333"
)
chat_area.grid(row=0, column=0, columnspan=2, padx=12, pady=12, sticky="nsew")

# Left for user, right for AI
chat_area.tag_configure("user", justify="left", foreground="#0b5394")
chat_area.tag_configure("ai", justify="right", foreground="#3d3d3d")

entry = tk.Entry(root, font=("Segoe UI", 11), bg="#ffffff", fg="#333333", relief="solid", bd=1)
entry.grid(row=1, column=0, padx=12, pady=12, sticky="ew")
entry.bind("<Return>", send_prompt)

send_button = tk.Button(
    root,
    text="Send",
    command=send_prompt,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    padx=18,
    pady=6,
    relief="flat",
    cursor="hand2"
)
send_button.grid(row=1, column=1, padx=12, pady=12, sticky="ew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
