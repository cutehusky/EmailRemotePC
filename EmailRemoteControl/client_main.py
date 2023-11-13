import customtkinter as ctk
import tkinter as tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import resource.variables as variables

smtp_host = variables.smtp_host
smtp_port = variables.smtp_port
USER_EMAIL = variables.CLIENT_EMAIL
USER_PASSWORD = variables.CLIENT_PASSWORD
recipient_mail = variables.USER_EMAIL

cp = {
    'bg': '#08122A',
    'fg': '#111931',
    'button_1': '#66A9A5',  # send
    'button_2': '#E36B6B',  # close/delete mail
}


class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=cp['fg'], height=500, width=325)
        self.commands = ['help',
                         'shutdown',
                         'kill_process',
                         'screenshot',
                         'webcam',
                         'keylog',
                         'list_apps',
                         'list_processes',]
        self.checkboxes = []

        for i in range(len(self.commands)):
            self.checkboxes.append(
                ctk.CTkCheckBox(master=self,
                                text=self.commands[i],
                                corner_radius=12
                                ))
            self.checkboxes[i].grid(
                row=i, column=0, padx=20, pady=10)

        self.placeholder_text = 'Enter PID'
        self.entry = ctk.CTkEntry(
            self, fg_color=cp['bg'], bg_color=cp['fg'], corner_radius=12)
        self.entry.insert(0, self.placeholder_text)
        self.entry.bind('<FocusIn>', self.on_entry_focus_in)
        self.entry.bind('<FocusOut>', self.on_entry_focus_out)
        self.entry.grid(row=2, column=2, padx=20, pady=10)

    def on_entry_focus_in(self, event):
        if self.entry.get() == self.placeholder_text:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, '')
            self.entry.configure(fg_color=cp['fg'])

    def on_entry_focus_out(self, event):
        if self.entry.get() == '':
            self.entry.insert(0, self.placeholder_text)
            self.entry.configure(fg_color=cp['fg'])

    def get(self):
        options = []
        for i, value in enumerate(self.checkboxes):
            if value.get() == 1:
                if self.commands[i] == 'kill_process':
                    text = self.entry.get()
                    options.append(
                        self.checkboxes[i].cget('text') + ' ' + text)
                else:
                    options.append(self.checkboxes[i].cget('text'))
        checked_options = '\n'.join(options)
        return checked_options


class EmailFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color=cp['fg'], width=325, height=350)
        self.grid_columnconfigure(1, weight=1)

        self.icon = ['◢', '◣', '◤', '◥']
        self.index = 0

        self.label = ctk.CTkLabel(
            master=self,
            text=''
        )
        self.label.grid(row=1, column=1, padx=10, pady=10, columnspan=1)
        self.label.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(
            master=self,
            text='Start fetching',
            fg_color=cp['button_1'],
            text_color='black',
            command=self.fetch
        )
        self.button.grid(row=0, column=1, padx=10, pady=10, columnspan=1)

    def waiting(self):
        self.label.configure(text=f'Fetching response {self.icon[self.index]}')
        if self.index == len(self.icon) - 1:
            self.index = 0
        else:
            self.index += 1

    def fetch(self):
        self.button.configure(state='disabled')
        self.waiting()
        self.after(200, self.fetch)

    def get_mail(self):
        pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ERC - Client")
        # self.geometry("740x540")
        self.configure(fg_color=cp['bg'])
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # label
        self.label = ctk.CTkLabel(
            master=self,
            text="Choose commands and click Send",
            fg_color=cp['fg'],
            corner_radius=6, height=60, width=325)
        self.label.grid(row=0, column=0, padx=10, pady=10,
                        columnspan=1, sticky='n')
        self.label.grid_columnconfigure(0, weight=1)
        # mail label
        self.maillabel = ctk.CTkLabel(
            master=self,
            text="Incoming emails",
            fg_color=cp['fg'],
            corner_radius=6,
            height=60, width=350)
        self.maillabel.grid(row=0, column=1, padx=20,
                            pady=10, columnspan=1, sticky='n')
        self.maillabel.grid_columnconfigure(0, weight=1)

        # checkbox frame
        self.checkboxFrame = CheckboxFrame(self)
        self.checkboxFrame.grid(row=1, column=0, padx=10, pady=10)

        # email frame
        self.emailFrame = EmailFrame(self)
        self.emailFrame.grid(row=1, column=1, padx=10, pady=10)

        # send and close button frame
        self.buttonFrame = ctk.CTkFrame(self, fg_color=cp['bg'])
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.buttonFrame.grid_columnconfigure(0, weight=1)
        # send button
        self.button = ctk.CTkButton(
            master=self.buttonFrame,
            text="Send",
            fg_color=cp['button_1'],
            text_color='black',
            command=lambda: self.send(self.checkboxFrame.get()))
        self.button.grid(row=2, column=0, padx=10, pady=10)
        self.button.grid_columnconfigure(1, weight=1)
        # close button
        self.close_button = ctk.CTkButton(
            master=self.buttonFrame,
            text="Close",
            fg_color=cp['button_2'],
            text_color='black',
            command=self.destroy)
        self.close_button.grid(row=2, column=1, padx=10, pady=10)
        self.close_button.grid_columnconfigure(1, weight=1)

    def send(self, checked_options):
        global recipient_mail
        msg = MIMEMultipart()
        msg['From'] = USER_EMAIL
        msg['To'] = recipient_mail
        msg['Subject'] = "Remote Control Command"

        # send plain text
        msg.attach(MIMEText(checked_options, 'plain'))
        if (len(checked_options) == 0):
            self.label.configure(text='Please choose at least one command!')
            return

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


if __name__ == "__main__":
    app = App()
    app.mainloop()
