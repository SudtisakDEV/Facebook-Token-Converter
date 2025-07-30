import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
import json
from datetime import datetime, timedelta
import threading
import pyperclip
from tkinter import messagebox
import tkinter as tk

class HackerTokenConverter:
    def __init__(self):
        # Create main window with dark hacker theme
        self.root = ttk.Window(
            title="🚀 FB Token Converter | HACKER EDITION",
            themename="superhero",  # Dark hacker theme
            size=(900, 800),
            resizable=(True, True)
        )
        
        # Set window properties
        self.root.configure(bg='#0d1117')
        
        # Initialize variables
        self.conversion_running = False
        
        # Create GUI
        self.create_header()
        self.create_input_section()
        self.create_action_section()
        self.create_terminal_output()
        self.create_footer()
        
        # Start terminal animation
        self.start_terminal_animation()
    
    def create_header(self):
        # Header frame with hacker aesthetic
        header_frame = ttk.Frame(self.root, bootstyle="dark")
        header_frame.pack(fill=X, padx=20, pady=(20, 10))
        
        # ASCII Art Header
        ascii_art = """
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
███████║███████║██║     █████╔╝ █████╗  ██████╔╝       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
        """
        
        ascii_label = ttk.Label(
            header_frame,
            text=ascii_art,
            font=('Courier New', 6, 'bold'),
            bootstyle="success",
            justify=CENTER
        )
        ascii_label.pack(pady=(0, 10))
        
        # Subtitle with hacker vibe
        subtitle = ttk.Label(
            header_frame,
            text="🔥 FACEBOOK TOKEN CONVERTER v2.0 🔥\n[ CONVERTING SHORT-LIVED TOKENS TO LONG-LIVED TOKENS ]",
            font=('Courier New', 10, 'bold'),
            bootstyle="warning",
            justify=CENTER
        )
        subtitle.pack()
        
        # Animated separator
        separator = ttk.Separator(header_frame, bootstyle="success")
        separator.pack(fill=X, pady=10)
    
    def create_input_section(self):
        # Main input container
        input_container = ttk.LabelFrame(
            self.root,
            text="🔐 AUTHENTICATION CREDENTIALS",
            bootstyle="primary",
            padding=20
        )
        input_container.pack(fill=X, padx=20, pady=10)
        
        # App ID Section
        app_id_frame = ttk.Frame(input_container)
        app_id_frame.pack(fill=X, pady=(0, 15))
        
        ttk.Label(
            app_id_frame,
            text="📱 APP_ID:",
            font=('Courier New', 11, 'bold'),
            bootstyle="info"
        ).pack(anchor=W)
        
        self.app_id_var = ttk.StringVar()
        self.app_id_entry = ttk.Entry(
            app_id_frame,
            textvariable=self.app_id_var,
            font=('Courier New', 10),
            bootstyle="dark",
            width=70
        )
        self.app_id_entry.pack(fill=X, pady=(5, 0))
        
        # App Secret Section
        app_secret_frame = ttk.Frame(input_container)
        app_secret_frame.pack(fill=X, pady=(0, 15))
        
        secret_label_frame = ttk.Frame(app_secret_frame)
        secret_label_frame.pack(fill=X)
        
        ttk.Label(
            secret_label_frame,
            text="🔑 APP_SECRET:",
            font=('Courier New', 11, 'bold'),
            bootstyle="info"
        ).pack(side=LEFT)
        
        self.show_secret_var = ttk.BooleanVar()
        show_check = ttk.Checkbutton(
            secret_label_frame,
            text="SHOW",
            variable=self.show_secret_var,
            command=self.toggle_secret_visibility,
            bootstyle="success"
        )
        show_check.pack(side=RIGHT)
        
        self.app_secret_var = ttk.StringVar()
        self.app_secret_entry = ttk.Entry(
            app_secret_frame,
            textvariable=self.app_secret_var,
            font=('Courier New', 10),
            bootstyle="dark",
            show="*",
            width=70
        )
        self.app_secret_entry.pack(fill=X, pady=(5, 0))
        
        # Short Token Section
        token_frame = ttk.Frame(input_container)
        token_frame.pack(fill=X)
        
        token_label_frame = ttk.Frame(token_frame)
        token_label_frame.pack(fill=X)
        
        ttk.Label(
            token_label_frame,
            text="⏱️ SHORT_LIVED_TOKEN:",
            font=('Courier New', 11, 'bold'),
            bootstyle="info"
        ).pack(side=LEFT)
        
        paste_btn = ttk.Button(
            token_label_frame,
            text="📋 PASTE",
            command=self.paste_token,
            bootstyle="success",
            width=10
        )
        paste_btn.pack(side=RIGHT)
        
        self.token_text = tk.Text(
            token_frame,
            height=4,
            font=('Courier New', 9),
            bg='#21262d',
            fg='#c9d1d9',
            insertbackground='#58a6ff',
            selectbackground='#264f78',
            relief='solid',
            bd=1,
            wrap='word'
        )
        self.token_text.pack(fill=X, pady=(5, 0))
        
        # Add scrollbar to token text
        token_scroll = ttk.Scrollbar(self.token_text, orient=VERTICAL, bootstyle="dark")
        self.token_text.configure(yscrollcommand=token_scroll.set)
        token_scroll.configure(command=self.token_text.yview)
    
    def create_action_section(self):
        action_frame = ttk.Frame(self.root)
        action_frame.pack(fill=X, padx=20, pady=20)
        
        # Convert Button
        self.convert_btn = ttk.Button(
            action_frame,
            text="🚀 INITIATE TOKEN CONVERSION",
            command=self.start_conversion,
            bootstyle="success",
            width=40
        )
        self.convert_btn.pack(side=LEFT, padx=(0, 10))
        
        # Clear Button
        clear_btn = ttk.Button(
            action_frame,
            text="🗑️ CLEAR ALL",
            command=self.clear_all,
            bootstyle="danger",
            width=15
        )
        clear_btn.pack(side=LEFT, padx=(0, 10))
        
        # Progress Bar
        self.progress = ttk.Progressbar(
            action_frame,
            mode="indeterminate",
            bootstyle="success-striped",
            length=200
        )
        self.progress.pack(side=RIGHT)
        
        # Status Label
        self.status_label = ttk.Label(
            self.root,
            text="⚡ STATUS: READY FOR CONVERSION",
            font=('Courier New', 10, 'bold'),
            bootstyle="warning"
        )
        self.status_label.pack(pady=(0, 10))
    
    def create_terminal_output(self):
        # Terminal-style output
        terminal_frame = ttk.LabelFrame(
            self.root,
            text="💻 TERMINAL OUTPUT",
            bootstyle="secondary",
            padding=10
        )
        terminal_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 10))
        
        # Terminal text area
        terminal_container = ttk.Frame(terminal_frame)
        terminal_container.pack(fill=BOTH, expand=True)
        
        self.terminal = tk.Text(
            terminal_container,
            font=('Courier New', 10),
            bg='#0d1117',
            fg='#58a6ff',
            insertbackground='#58a6ff',
            selectbackground='#264f78',
            relief='flat',
            wrap='word',
            state='disabled'
        )
        self.terminal.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Terminal scrollbar
        terminal_scroll = ttk.Scrollbar(
            terminal_container,
            orient=VERTICAL,
            bootstyle="secondary"
        )
        terminal_scroll.pack(side=RIGHT, fill=Y)
        
        self.terminal.configure(yscrollcommand=terminal_scroll.set)
        terminal_scroll.configure(command=self.terminal.yview)
        
        # Copy result button
        copy_frame = ttk.Frame(terminal_frame)
        copy_frame.pack(fill=X, pady=(10, 0))
        
        self.copy_token_btn = ttk.Button(
            copy_frame,
            text="📋 COPY LONG-LIVED TOKEN",
            command=self.copy_long_token,
            bootstyle="info",
            state="disabled"
        )
        self.copy_token_btn.pack(side=LEFT)
        
        copy_all_btn = ttk.Button(
            copy_frame,
            text="📋 COPY ALL OUTPUT",
            command=self.copy_all_output,
            bootstyle="secondary"
        )
        copy_all_btn.pack(side=LEFT, padx=(10, 0))
    
    def create_footer(self):
        footer_frame = ttk.Frame(self.root, bootstyle="dark")
        footer_frame.pack(fill=X, padx=20, pady=(0, 20))
        
        ttk.Separator(footer_frame, bootstyle="secondary").pack(fill=X, pady=(0, 10))
        
        footer_text = """
🔥 HACKER EDITION FEATURES 🔥
• LONG-LIVED TOKENS: 60 DAYS LIFESPAN • SECURE CLIPBOARD OPERATIONS • REAL-TIME STATUS UPDATES
• TERMINAL-STYLE OUTPUT • AUTO-SCROLL • COPY FUNCTIONALITY • ERROR HANDLING & DEBUGGING
        """
        
        ttk.Label(
            footer_frame,
            text=footer_text,
            font=('Courier New', 8),
            bootstyle="secondary",
            justify=CENTER
        ).pack()
    
    def toggle_secret_visibility(self):
        if self.show_secret_var.get():
            self.app_secret_entry.configure(show="")
        else:
            self.app_secret_entry.configure(show="*")
    
    def paste_token(self):
        try:
            clipboard_content = pyperclip.paste()
            self.token_text.delete(1.0, tk.END)
            self.token_text.insert(1.0, clipboard_content)
            self.log_to_terminal("📋 Token pasted from clipboard successfully", "success")
        except Exception as e:
            self.log_to_terminal(f"❌ Clipboard paste failed: {str(e)}", "error")
    
    def clear_all(self):
        self.app_id_var.set("")
        self.app_secret_var.set("")
        self.token_text.delete(1.0, tk.END)
        self.terminal.configure(state='normal')
        self.terminal.delete(1.0, tk.END)
        self.terminal.configure(state='disabled')
        self.copy_token_btn.configure(state="disabled")
        self.status_label.configure(text="⚡ STATUS: CLEARED - READY FOR NEW CONVERSION")
        self.log_to_terminal("🧹 All fields cleared. Ready for new conversion.", "info")
    
    def log_to_terminal(self, message, log_type="info"):
        self.terminal.configure(state='normal')
        
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        # Color coding based on log type
        colors = {
            "info": "#58a6ff",
            "success": "#3fb950", 
            "warning": "#d29922",
            "error": "#f85149",
            "system": "#a5a5a5"
        }
        
        color = colors.get(log_type, "#58a6ff")
        
        # Insert timestamp
        self.terminal.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        # Insert message with color
        self.terminal.insert(tk.END, f"{message}\n", log_type)
        
        # Configure tags for colors
        self.terminal.tag_configure("timestamp", foreground="#a5a5a5")
        self.terminal.tag_configure(log_type, foreground=color)
        
        self.terminal.configure(state='disabled')
        self.terminal.see(tk.END)
        self.root.update()
    
    def start_terminal_animation(self):
        welcome_messages = [
            "🔥 HACKER TOKEN CONVERTER INITIALIZED",
            "💻 System ready for Facebook token conversion",
            "🛡️ Security protocols activated",
            "⚡ Awaiting user input...",
            ""
        ]
        
        for msg in welcome_messages:
            self.log_to_terminal(msg, "system")
    
    def update_status(self, message, status_type="info"):
        status_colors = {
            "info": "warning",
            "success": "success", 
            "error": "danger",
            "working": "primary"
        }
        
        self.status_label.configure(
            text=f"⚡ STATUS: {message}",
            bootstyle=status_colors.get(status_type, "warning")
        )
        self.root.update()
    
    def start_conversion(self):
        if self.conversion_running:
            return
            
        # Validate inputs
        app_id = self.app_id_var.get().strip()
        app_secret = self.app_secret_var.get().strip()
        short_token = self.token_text.get(1.0, tk.END).strip()
        
        if not all([app_id, app_secret, short_token]):
            self.log_to_terminal("❌ ERROR: Missing required fields", "error")
            messagebox.showerror("Input Error", "Please fill in all required fields!")
            return
        
        # Start conversion in thread
        self.conversion_running = True
        thread = threading.Thread(target=self.convert_token, daemon=True)
        thread.start()
    
    def convert_token(self):
        try:
            # Update UI
            self.convert_btn.configure(state="disabled", text="🔄 CONVERTING...")
            self.progress.start()
            self.update_status("CONVERSION IN PROGRESS", "working")
            
            # Log conversion start
            self.log_to_terminal("🚀 Starting token conversion process", "info")
            self.log_to_terminal("🔐 Validating credentials...", "info")
            
            # Get values
            app_id = self.app_id_var.get().strip()
            app_secret = self.app_secret_var.get().strip()
            short_token = self.token_text.get(1.0, tk.END).strip()
            
            # API call
            self.log_to_terminal("📡 Sending request to Facebook Graph API...", "info")
            
            url = "https://graph.facebook.com/oauth/access_token"
            params = {
                'grant_type': 'fb_exchange_token',
                'client_id': app_id,
                'client_secret': app_secret,
                'fb_exchange_token': short_token
            }
            
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                
                # Success logging
                self.log_to_terminal("✅ API Request successful!", "success")
                self.log_to_terminal("🔑 Long-lived token generated successfully", "success")
                
                # Parse response
                long_token = data.get('access_token', 'N/A')
                token_type = data.get('token_type', 'N/A')
                expires_in = data.get('expires_in', 0)
                
                # Calculate expiry
                if expires_in:
                    expiry_date = datetime.now() + timedelta(seconds=expires_in)
                    expiry_str = expiry_date.strftime("%Y-%m-%d %H:%M:%S")
                    days = expires_in // 86400
                else:
                    expiry_str = "Never expires"
                    days = "∞"
                
                # Display results
                self.log_to_terminal("", "info")
                self.log_to_terminal("=" * 80, "success")
                self.log_to_terminal("🎉 TOKEN CONVERSION COMPLETED SUCCESSFULLY", "success")
                self.log_to_terminal("=" * 80, "success")
                self.log_to_terminal(f"📋 LONG-LIVED TOKEN:", "info")
                self.log_to_terminal(f"{long_token}", "success")
                self.log_to_terminal("", "info")
                self.log_to_terminal(f"📊 TOKEN TYPE: {token_type}", "info")
                self.log_to_terminal(f"⏰ EXPIRES IN: {expires_in} seconds ({days} days)", "info") 
                self.log_to_terminal(f"📅 EXPIRY DATE: {expiry_str}", "info")
                self.log_to_terminal("=" * 80, "success")
                
                # Store token for copying
                self.long_lived_token = long_token
                self.copy_token_btn.configure(state="normal")
                self.update_status("CONVERSION COMPLETED SUCCESSFULLY", "success")
                
            else:
                # Error handling
                error_data = response.json() if response.content else {"error": {"message": "Unknown error"}}
                error_msg = error_data.get('error', {}).get('message', 'Unknown error')
                
                self.log_to_terminal("❌ API Request failed!", "error")
                self.log_to_terminal(f"🔍 HTTP Status: {response.status_code}", "error")
                self.log_to_terminal(f"💥 Error Message: {error_msg}", "error")
                self.log_to_terminal("", "error")
                self.log_to_terminal("🛠️ TROUBLESHOOTING TIPS:", "warning")
                self.log_to_terminal("• Check your App ID and App Secret", "warning")
                self.log_to_terminal("• Ensure your short-lived token is valid", "warning")
                self.log_to_terminal("• Verify your app has proper permissions", "warning")
                self.log_to_terminal("• Generate a fresh short-lived token", "warning")
                
                self.update_status("CONVERSION FAILED", "error")
                
        except requests.exceptions.Timeout:
            self.log_to_terminal("⏰ Request timeout! Check your connection.", "error")
            self.update_status("CONNECTION TIMEOUT", "error")
            
        except Exception as e:
            self.log_to_terminal(f"💥 Unexpected error: {str(e)}", "error")
            self.update_status("UNEXPECTED ERROR", "error")
            
        finally:
            # Reset UI
            self.convert_btn.configure(state="normal", text="🚀 INITIATE TOKEN CONVERSION")
            self.progress.stop()
            self.conversion_running = False
    
    def copy_long_token(self):
        if hasattr(self, 'long_lived_token'):
            try:
                pyperclip.copy(self.long_lived_token)
                self.log_to_terminal("📋 Long-lived token copied to clipboard!", "success")
                self.update_status("TOKEN COPIED TO CLIPBOARD", "success")
            except Exception as e:
                self.log_to_terminal(f"❌ Copy failed: {str(e)}", "error")
    
    def copy_all_output(self):
        try:
            output = self.terminal.get(1.0, tk.END)
            pyperclip.copy(output)
            self.log_to_terminal("📋 All terminal output copied to clipboard!", "success")
        except Exception as e:
            self.log_to_terminal(f"❌ Copy failed: {str(e)}", "error")
    
    def run(self):
        self.root.mainloop()

def main():
    # Install required packages if not available
    required_packages = ['ttkbootstrap', 'requests', 'pyperclip']
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            import subprocess
            subprocess.check_call(['pip', 'install', package])
    
    # Create and run application
    app = HackerTokenConverter()
    app.run()

if __name__ == "__main__":
    main()
