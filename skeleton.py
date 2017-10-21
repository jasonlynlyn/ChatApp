from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class ChatWindow(GridLayout):
	
	def chat(self, enterchat):
		if enterchat:
			try:
				self.display.text=str(ChatWindow)
			except Exception:
				self.display.text="I don't understand you"
	


class MyApp(App):
	def build(self):
		return ChatWindow()
	

if __name__=="__main__":
	MyApp().run()

