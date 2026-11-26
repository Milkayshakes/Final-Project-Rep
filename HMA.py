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
        self.post_box.pack(fill="x", padx=15, pady=15)

        self.post_input = ctk.CTkFrame(self)
        self.post_box.pack(fill="x", padx=10, pady=(10, 5))
        

        self.post_btn = ctk.CTkButton(
            self.post_box, text="Post", width=80, command=self.publish_post
        )
        self.post_btn.pack(anchor="e", padx=10, pady=(0,10))

        self.feed = ctk.CTkScrollableFrame(self, label_text="Home Feed")
        self.feed.pack(fill="both", expand=True, padx=15, pady=(0,15))

        self.add_post_card("@MilkayShakes", "Looking for a artist for my illustration book idea.", 12)
        self.add_post_card("@Sproket", "Looking for a writer to help create a script for a illistration book I'm making.", 34)

    def publish_post(self):
        content = self.post_input.get("0.0", "end").strip()
        if content and content != "Hello! Are you an artist or writer?":
            self.add_post_card("@you", content, 0, top=True)
            self.post_input.delete("0.0", "end")

    def add_post_card(self, username, content, initial_likes, top=False):
        card = ctk.CTkFrame(self.feed)
        card.pack(fill="x", pady=6, padx=5)

        user_lbl = ctk.CTkLabel(
            card, text=username, font=("Roboto", 13, "bold"), text_color="#006E90"
        
        )
        user_lbl.pack(anchor="w", padx=12, pady=(0,8))

        likes = [initial_likes]
        def toggle_like():
            likes[0] += 1
            like_btn.configure(text=f":heart: {likes[0]} ")

        like_btn = ctk.CTkButton(
            card,
            text=f":heart: {likes[0]}",
            width=65,
            height=26,
            fg_color="transparent",
            border_width=1,
            command=toggle_like,
        )
        like_btn.pack(anchor="w", padx=12, pady=(0,10))

if __name__ == "__main__":
    app = SocialMediaApp()
    app.mainloop()
    