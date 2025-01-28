import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import json

def split_audio(file_path, output_dir, segment_length=15 * 60):
    """Split audio file into smaller segments."""
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    segment_dir = os.path.join(output_dir, f"{file_name}_segments")
    os.makedirs(segment_dir, exist_ok=True)

    try:
        command = [
            "ffmpeg", "-i", file_path, "-f", "segment", "-segment_time",
            str(segment_length), "-c", "copy",
            os.path.join(segment_dir, f"{file_name}_%03d.wav")
        ]
        subprocess.run(command, check=True)
        return [os.path.join(segment_dir, f) for f in sorted(os.listdir(segment_dir))]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to split audio: {e}")
        return []

def transcribe_segment(segment_path, model, output_dir):
    """Transcribe a single audio segment using Whisper AI."""
    try:
        command = [
            "whisper", segment_path, "--model", model, "--output_dir", output_dir, "--output_format", "json"
        ]
        subprocess.run(command, check=True)
        json_path = os.path.join(output_dir, os.path.splitext(os.path.basename(segment_path))[0] + ".json")
        return json_path if os.path.exists(json_path) else None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to transcribe segment {segment_path}: {e}")
        return None

def save_combined_transcription(segment_transcriptions, output_txt_file, include_timestamps):
    """Combine and save transcriptions with or without timestamps."""
    with open(output_txt_file, 'w') as txt_f:
        for transcription_path in segment_transcriptions:
            with open(transcription_path, 'r') as f:
                data = json.load(f)
                for segment in data.get('segments', []):
                    text = segment['text']
                    if include_timestamps:
                        start_time = segment['start']
                        end_time = segment['end']
                        txt_f.write(f"[{start_time:.2f} - {end_time:.2f}] {text}\n")
                    else:
                        txt_f.write(f"{text}\n")

    # Post-process the file to adjust line breaks
    with open(output_txt_file, 'r') as txt_f:
        content = txt_f.read()

    # Remove extra CR+LF pairs and add line breaks after punctuation
    content = content.replace("\r\n\r\n", "\n")
    content = content.replace(".\n", ".\r\n").replace("!\n", "!\r\n").replace("?\n", "?\r\n")

    with open(output_txt_file, 'w') as txt_f:
        txt_f.write(content)

# Initialize the main application window
root = tk.Tk()
root.title("Whisper AI GUI")
root.geometry("600x500")

selected_model = tk.StringVar(value="base")
selected_file = tk.StringVar(value="No file selected")
output_dir = tk.StringVar(value=os.getcwd())
output_file_name = tk.StringVar(value="transcription_with_timestamps")
include_timestamps = tk.BooleanVar(value=True)

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")])
    if file_path:
        selected_file.set(file_path)

def choose_output_dir():
    directory = filedialog.askdirectory()
    if directory:
        output_dir.set(directory)

def run_transcription():
    file_path = selected_file.get()
    model = selected_model.get()
    out_dir = output_dir.get()
    custom_file_name = output_file_name.get().strip()

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Please select a valid audio file.")
        return

    if not custom_file_name:
        messagebox.showerror("Error", "Please provide a valid name for the output file.")
        return

    try:
        segments = split_audio(file_path, out_dir)
        if not segments:
            return

        segment_transcriptions = []
        for segment in segments:
            json_path = transcribe_segment(segment, model, out_dir)
            if json_path:
                segment_transcriptions.append(json_path)

        txt_output_path = os.path.join(out_dir, f"{custom_file_name}.txt")
        save_combined_transcription(segment_transcriptions, txt_output_path, include_timestamps.get())

        messagebox.showinfo("Success", f"Transcription completed!\nOutput saved in {out_dir}\nFile: {custom_file_name}.txt")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Components
tk.Label(root, text="Whisper AI GUI", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Select Model:").pack(anchor="w", padx=10)
tk.OptionMenu(root, selected_model, "tiny", "base", "medium", "large", "large-v2", "large-v3", "turbo").pack(fill="x", padx=10)
tk.Label(root, text="Select Audio File:").pack(anchor="w", padx=10)
tk.Button(root, text="Choose File", command=choose_file).pack(pady=5, padx=10, anchor="w")
tk.Label(root, textvariable=selected_file, wraplength=450, fg="blue").pack(anchor="w", padx=20)
tk.Label(root, text="Select Output Directory:").pack(anchor="w", padx=10)
tk.Button(root, text="Choose Directory", command=choose_output_dir).pack(pady=5, padx=10, anchor="w")
tk.Label(root, textvariable=output_dir, wraplength=450, fg="blue").pack(anchor="w", padx=20)
tk.Label(root, text="Custom Output File Name:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=output_file_name).pack(fill="x", padx=10, pady=5)
tk.Checkbutton(root, text="Include Timestamps", variable=include_timestamps).pack(anchor="w", padx=10, pady=5)
tk.Button(root, text="Run Transcription", command=run_transcription).pack(pady=10)

root.mainloop()