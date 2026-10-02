import os
import platform
import subprocess
import sys
import ctypes
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.geteuid() == 0
    except Exception:
        return False

class NetDetoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetDetox - Network Health & Repair")
        self.root.geometry("600x450")
        self.root.minsize(500, 400)
        
        # Configure window background/style
        self.root.configure(bg="#f4f6f9")

        # Title Label
        title_label = tk.Label(
            root, 
            text="🧹 NetDetox Utility", 
            font=("Arial", 16, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50"
        )
        title_label.pack(pady=15)

        # Description
        desc_label = tk.Label(
            root, 
            text="Click below to flush DNS, reset Winsock, and restore network stability.", 
            font=("Arial", 10), 
            bg="#f4f6f9", 
            fg="#555555"
        )
        desc_label.pack(pady=5)

        # Action Button
        self.run_btn = tk.Button(
            root, 
            text="Start Network Detox", 
            font=("Arial", 11, "bold"), 
            bg="#27ae60", 
            fg="white", 
            padx=15, 
            pady=8, 
            relief="flat",
            cursor="hand2",
            command=self.start_detox_thread
        )
        self.run_btn.pack(pady=15)

        # Output Log Box (Scrolled Text)
        self.log_box = scrolledtext.Text(
            root, 
            wrap=tk.WORD, 
            font=("Consolas", 9), 
            bg="#1e1e1e", 
            fg="#d4d4d4",
            insertbackground="white"
        )
        self.log_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.log_box.insert(tk.END, "[System Ready] Click 'Start Network Detox' to begin...\n")
        self.log_box.config(state=tk.DISABLED)

    def log(self, message):
        """Helper to write messages safely to the text box from any thread."""
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.log_box.config(state=tk.DISABLED)

    def run_commands_sequence(self):
        """Executes the network reset commands sequentially."""
        commands = [
            ("ipconfig /flushdns", "Flushing the DNS Resolver Cache"),
            ("nbtstat -R", "Clearing NetBIOS name table cache"),
            ("nbtstat -RR", "Releasing and refreshing NetBIOS names"),
            ("ipconfig /release", "Releasing current IP configuration"),
            ("ipconfig /renew", "Renewing IP address from network adapter"),
            ("netsh winsock reset", "Resetting Winsock Catalog"),
            ("netsh int ip reset", "Resetting TCP/IP Stack")
        ]

        for cmd, desc in commands:
            self.log(f"[*] {desc}...")
            try:
                result = subprocess.run(
                    cmd, 
                    shell=True, 
                    capture_output=True, 
                    text=True, 
                    timeout=30
                )
                if result.returncode == 0:
                    self.log(f"[+] Success: {desc}")
                    if result.stdout.strip():
                        self.log(result.stdout.strip())
                else:
                    self.log(f"[-] Note/Error during {desc}:")
                    self.log(result.stderr.strip() or result.stdout.strip())
            except Exception as e:
                self.log(f"[-] Error: {e}")
            self.log("-" * 40)

        self.log("\n[!] Network detox sequence completed successfully!")
        self.log("[!] Recommendation: Restart your computer for full effect.")
        
        # Re-enable button
        self.run_btn.config(state=tk.NORMAL, bg="#27ae60")
        messagebox.showinfo("NetDetox", "Network repair sequence finished!")

    def start_detox_thread(self):
        """Runs the detox sequence in a background thread to keep UI responsive."""
        if platform.system() != "Windows":
            messagebox.showerror("Unsupported OS", "This tool requires Windows.")
            return

        if not is_admin():
            messagebox.showerror(
                "Admin Required", 
                "Administrative privileges are required to reset network stacks.\n"
                "Please run this app as Administrator."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Detox", 
            "This will temporarily drop your active internet connection to reset network stacks. Proceed?"
        )
        if not confirm:
            return

        # Disable button during execution
        self.run_btn.config(state=tk.DISABLED, bg="#95a5a6")
        self.log_box.config(state=tk.NORMAL)
        self.log_box.delete("1.0", tk.END)
        self.log_box.config(state=tk.DISABLED)

        # Start thread
        threading.Thread(target=self.run_commands_sequence, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = NetDetoxApp(root)
    root.mainloop()
