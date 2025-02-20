import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "กรุณากรอก URL!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    if not file_path:
        return

    try:
        # QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        img.save(file_path)

        img.thumbnail((200, 500))
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

        messagebox.showinfo("สำเร็จ!", f"QR Code ถูกบันทึกที่:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

# UI
tk.Label(root, text="กรอก URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

btn_generate = tk.Button(root, text="สร้าง QR Code", font=("Arial", 12), command=generate_qr)
btn_generate.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
