import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "กรุณากรอก URL!")
        return
    
    # ให้ผู้ใช้เลือกตำแหน่งและชื่อไฟล์
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    if not file_path:  # ถ้าผู้ใช้กดยกเลิก ไม่ต้องทำอะไรต่อ
        return

    try:
        # สร้าง QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # บันทึกไฟล์
        img.save(file_path)

        # แสดง QR Code บน UI
        img.thumbnail((200, 500))
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk  # ป้องกันการรีเฟรชแล้วภาพหาย

        messagebox.showinfo("สำเร็จ!", f"QR Code ถูกบันทึกที่:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

# ส่วน UI
tk.Label(root, text="กรอก URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

btn_generate = tk.Button(root, text="สร้าง QR Code", font=("Arial", 12), command=generate_qr)
btn_generate.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

# เริ่มต้น GUI
root.mainloop()
