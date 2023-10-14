import tkinter as tk
from tkinter import ttk

# root window
app = tk.Tk()
app.geometry('300x120')
app.title('Progressbar Demo')

def update_progress_label(message):
    message = '' if message is None else message
    return f"Current Progress: {pb['value']}%, {message}"

def updateProgress(min_limit, max_limit, message):
    if pb['value'] >= min_limit and pb['value'] < max_limit:
        pb['value'] += 1
        value_label['text'] = update_progress_label(message)
        app.after(10, updateProgress, min_limit, max_limit, message)
    elif pb['value'] == 100:
        value_label['text'] = 'The progress completed!'

def progress():
    if pb['value'] < 30:
        updateProgress(0, 30, 'Bouton 1...')
    elif pb['value'] >= 30 and pb['value'] < 60:
        updateProgress(30, 60, 'Bouton 2...')
    elif pb['value'] >= 60 and pb['value'] < 100:
        updateProgress(60, 100, 'Bouton 3...')

def stop():
    pb.stop()
    value_label['text'] = update_progress_label(None)

pb = ttk.Progressbar(app, orient='horizontal', mode="determinate", length=280)

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=(10,0))

value_label = ttk.Label(app, text=update_progress_label(None))
value_label.grid(column=0, row=1, columnspan=2)
# start button
start_button = ttk.Button(
    app,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    app,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

app.mainloop()