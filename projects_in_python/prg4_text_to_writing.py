import pywhatkit as pw

text = input("enter the text you want to convert: ")
pw.text_to_handwriting(text,"demo1.png",[0,0,138])
print("end")