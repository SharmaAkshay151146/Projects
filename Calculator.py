from tkinter import *
from tkinter import ttk 

class Calculator:

	# Initial value for display
	init_value = 0.0

	div_option = False
	mult_option = False 
	add_option = False 
	sub_option = False

	# Button press for numbers
	def button_press(self, value):
		entry_value = self.number_entry.get()
		entry_value += value 
		# self.number_entry.delete(0,"end") # clears the value
		self.number_entry.insert(0, entry_value)


	# Throw a string input. Put it in try-except block.
	# If the input is a float, then it is okay
	# Otherwise a value error is thrown
	def isFloat(self, input_string):
		try:
			float(input_string)
			return True
		except ValueError:
			return False

	def symbol_press(self, value):
		# I want to do smth, if the value was in entry

		# If we do have a float value inside here
		if self.isFloat(str(self.number_entry.get())):
			# make any previous symbol press to false
			# to cancel their effect
			self.div_option = False
			self.mult_option = False 
			self.add_option = False 
			self.sub_option = False

			# get the value out of the entry box for calculation
			self.init_value = float(self.entry_value.get())

			if value == "/":
				self.div_option = True
			elif value == "*":
				self.mult_option = True
			elif value == "+":
				self.add_option = True
			else:
				self.sub_option = True 

			# Clear the entry box
			self.number_entry.delete(0, "end")

	'''
	Performs an arithmetic operation by taking the number before a symbol 
	is pressed and the current number
	'''

	def equal_press(self):
		# Is a maths symbol clicked yet ?
		solution = 0
		if self.add_option or self.sub_option or self.mult_option or self.div_option:
			try:
				if self.div_option:
					solution = self.init_value / float(self.entry_value.get())
				elif self.mult_option:
					solution = self.init_value * float(self.entry_value.get())
				elif self.add_option:
					solution = self.init_value + float(self.entry_value.get())
				else:
					solution = self.init_value - float(self.entry_value.get())
			except ZeroDivisionError:
				self.number_entry.insert(0,"Illegal Division")
				return 
			else:	
				self.number_entry.delete(0, "end")
				self.number_entry.insert(0,round(solution, 3))

	def clear_press(self, value):
		if value == "AC":
			self.number_entry.delete(0, "end")
				

	def __init__(self, root):
		self.entry_value = StringVar(root, value="")

		root.title("Calculator")

		root.geometry("435x200")

		# The Calc shouldn't be resizable
		root.resizable(width=False, height=False)

		style = ttk.Style()
		style.configure("TButton", font="Garamond 12", padding=5.5)
		style.configure("TEntry", font="Garamond 12", padding=5.5)

		self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=70)

		# We want to change the above value, so we do grid of it separately
		self.number_entry.grid(row=0, columnspan=4) # We have 4 buttons

		# Row 1 - 7 8 9 /
		self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
		self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
		self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)
		self.button_div = ttk.Button(root, text="/", command=lambda: self.symbol_press('/')).grid(row=1, column=3)

		# Row 2 - 4	5 6 *
		self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
		self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
		self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)
		self.button_mult = ttk.Button(root, text="*", command=lambda: self.symbol_press('*')).grid(row=2, column=3)
		
		# Row 3 - 1 2 3 +
		self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
		self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
		self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)
		self.button_add = ttk.Button(root, text="+", command=lambda: self.symbol_press('+')).grid(row=3, column=3)

		# Row 4 - AC 0 = -
		self.button_clear = ttk.Button(root, text="AC", command=lambda: self.clear_press('AC')).grid(row=4, column=0)
		self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
		self.button_equals = ttk.Button(root, text="=", command=lambda: self.equal_press()).grid(row=4, column=2)
		self.button_sub = ttk.Button(root, text="-", command=lambda: self.symbol_press('-')).grid(row=4, column=3)


def main():
	# Start Tkinter
	root = Tk()
	# Start calculator
	calculator = Calculator(root)
	# Run till close is pressed
	root.mainloop()

if __name__=='__main__':
	main()


