import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SocialMediaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HMASocial")
        self.geometry("480x650")

        self.header = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.header.pack(fill="x")
        self.logo = ctk.CTkLabel(
            self.header, text="HMASocial", font=("Roboto", 20, "bold")
        )
        self.logo.pack(side="left", padx=20, pady=10)

        self.post_box = ctk.CTkFrame(self)
        self.post_box.pack(fill="x", padx=15,pady=15)

        self.post_input = ctk.CTkFrame(self)
        self.post_box.pack(fill="x")