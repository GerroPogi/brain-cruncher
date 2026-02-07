import customtkinter

dark_theme = customtkinter.Theme(
    primary_color="#262626",
    secondary_color="#3B3B3B",
    accent_color="#D75A4A",
    background_color="#1E1E1E",
    text_color="#FFFFFF",
    font=("Helvetica", 12),
    geometry="700x345",
    title="Brain Cruncher"
)

main = customtkinter.Window(dark_theme)

start_button = customtkinter.Button(
    master=main,
    text="Start",
    command=lambda: print("Start Button Clicked")
)
start_button.pack(pady=10)

quit_button = customtkinter.Button(
    master=main,
    text="Quit",
    command=lambda: main.destroy()
)
quit_button.pack(pady=10)

settings_button = customtkinter.Button(
    master=main,
    text="Settings",
    command=lambda: print("Settings Button Clicked")
)
settings_button.pack(pady=10)

main.mainloop()
