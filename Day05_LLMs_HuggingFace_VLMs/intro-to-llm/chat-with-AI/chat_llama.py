import tkinter as tk
from huggingface_hub import InferenceClient

# Initialize the Hugging Face API client
client = InferenceClient(token="YOUR TOKEN HERE")

# Function to get response from LLaMA model
def get_response(user_input):
    completion = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[{"role": "user", "content": user_input}],
    )
    return completion.choices[0].message.content

# Function to handle sending a message
def send_message(event=None):
    user_input = entry.get()
    if user_input.strip():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_input}\n", "user")
        chat_area.insert(tk.END, "\n")
        chat_area.yview(tk.END)
        chat_area.config(state=tk.DISABLED)

        model_response = get_response(user_input)

        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"AI: {model_response}\n", "ai")
        chat_area.insert(tk.END, "\n")
        chat_area.yview(tk.END)
        chat_area.config(state=tk.DISABLED)

        entry.delete(0, tk.END)

root = tk.Tk()
root.title("🤖 Chat with AI")
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

# Styling for user (left) and AI (right)
chat_area.tag_configure("user", justify="left", foreground="#0b5394")
chat_area.tag_configure("ai", justify="right", foreground="#3d3d3d")

entry = tk.Entry(root, font=("Segoe UI", 11), bg="#ffffff", fg="#333333", relief="solid", bd=1)
entry.grid(row=1, column=0, padx=12, pady=12, sticky="ew")
entry.bind("<Return>", send_message)

send_button = tk.Button(
    root,
    text="Send",
    command=send_message,
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


