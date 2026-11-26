import customtkinter as ctk
import requests
import os
import shutil
import uuid
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory= "static"), name="static")

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}

@app.post("/posts")
async def create_post(
    caption: str = Form(...),
    image: UploadFile = File(...)
):
    if image.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Invalid image format")
    ext = os.path.splittext(image.filename[1])
    unique_filename = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(UPLOAD_DIR, unique_filename)

    image_url = f"/static/uploads/{unique_filename}"
    return{
        "caption": caption,
        "image_url": image_url,
        "status": "published"
    }
    
url = "https://www.instagram.com/?hl=en"
print("Current working directory:", os.getcwd())
print("Files in this folder:", os.listdir())
with open("photo.jpg", "rb") as img_file:
    files = {"image":("photo.jpg", img_file, "image/jpeg")}
    data = {"caption": "Hello world!"}

    response = requests.post(url, data=data, files=files)
    print(response.json())





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
    