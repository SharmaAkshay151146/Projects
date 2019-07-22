from tkinter import *
import tkinter.filedialog

class Editor:

	@staticmethod
	def quit_app(event=None):
		root.quit()

	def open_file(self, event=None):
		text_file = tkinter.filedialog.askopenfilename(parent=root, initialdir='C:/Users/Sharma/Documents/')

		if text_file:
			self.text_area.delete(1.0,END)
			with open(text_file) as _file:
				self.text_area.insert(1.0, _file.read())
				root.update_idletasks()

	def save_file(self, event=None):
			# Opens the save as dialogue box
		file = tkinter.filedialog.asksaveasfile(mode='w')
		if file != None:
			# Get text in the text widget and delete the last newline
			data = self.text_area.get('1.0', END + '-1c')

			# Write the text and close
			file.write(data)
			file.close()

	def __init__(self):
		self.text_to_write = ""
		
		root.title("Editor")
		root.geometry("640x480")
		
		frame = Frame(root, width=480, height=640)
		
		scrollbar = Scrollbar(frame)
		
		self.text_area = Text(frame, width=480, height=640, yscrollcommand=scrollbar.set, padx=10, pady=10)

		scrollbar.config(command=self.text_area.yview)

		# Scrollbar should be on the right
		scrollbar.pack(side="right", fill="y")

		self.text_area.pack(side="left", fill="both", expand=True)
		frame.pack()

		# Create a menu object
		menu = Menu(root)

		# Pull down
		file_menu = Menu(menu, tearoff=0)

		# Add items to the menu that show when clicked
		# Compound allows you to add an image
		file_menu.add_command(label="Open", command=self.open_file)
		file_menu.add_command(label="Save", command=self.save_file)

		# Add a hz bar to group similar commands
		file_menu.add_separator()

		# Call for the function to execute when clicked
		file_menu.add_command(label="Quit", command=self.quit_app)

		# Add the pull down menu to the menu bar
		menu.add_cascade(label="File", menu=file_menu)

		root.config(menu=menu)

root = Tk()
text_editor = Editor()
root.mainloop()