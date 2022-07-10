from tkinter import *
import docclass

class EmotionPredictor(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.emoji_dict = {}
        self.initUI(parent)

    def initUI(self, parent):
        self.label_head = Label(self, text = 'Emotion Predictor App', bg = 'lightblue',fg = 'white', anchor = CENTER , font = ('Helvetica', '25', 'bold'))
        self.label_head.pack(fill=X)

        self.label_input_file = Label(self, text = 'Dataset File Path:',font = ('Helvetica', '14'))
        self.label_input_file.pack(pady=(10,0))

        self.file_entry = Entry(self, width = 65,justify="center",font = ('Helvetica', '14'))
        self.file_entry.pack()
        self.file_entry.insert(END,'text_emotion_fixed.csv')

        self.label_input_file2 = Label(self, text='Emoji File Path:', font=('Helvetica', '14'))
        self.label_input_file2.pack(pady=(10,0))

        self.file_entry2 = Entry(self, width=65, justify="center", font=('Helvetica', '14'))
        self.file_entry2.pack()
        self.file_entry2.insert(END, 'emotion_emojis.csv')

        self.upload_button = Button(self, text = 'Upload Dataset', font = ('"Helvetica', '12'), command = self.fit)
        self.upload_button.pack(pady=(10,0))

        self.label_prediction = Label(self, text='Predictions', font=('Helvetica', '14'))
        self.label_prediction.pack(pady=(30,0))

        self.input_entry = Entry(self, width=48, font = ('"Helvetica', '20'),justify = CENTER )
        self.input_entry.insert(0, 'Enter a sentence/word')
        self.input_entry.pack()

        self.predict_button = Button(self, text='Predict Emotion', font=('"Helvetica', '12'), command=self.predict)
        self.predict_button.pack(pady=(10,0))

        self.result_label = Label(self, font=("Helvetica","16"))
        self.result_label.pack()

    def fit(self):
        self.cl = docclass.NaiveBayes(docclass.getwords)
        file_path = self.file_entry.get()
        file_ = open(file_path,'r')
        lines = file_.readlines()
        for line in lines:
            emotion, document = line.split(",")[0], line.split(",")[1]
            self.cl.train(document,emotion)

    def predict(self):
        data = {}
        t = self.cl.categories()
        for emotion in t:
            document = self.input_entry.get()
            temp = self.cl.prob(document, emotion)
            data[emotion] = temp

        emotions = sorted(data.items(), key=lambda value: value[1])
        best_3_emotion, worst_3_emotion = emotions[-3:], emotions[:3]

        best_emotion_str = ""
        for i in best_3_emotion:
            temp_emotion = i[0]
            best_emotion_str = best_emotion_str + temp_emotion + "\n"

        worst_emotion_str = ""
        for i in worst_3_emotion:
            temp_emotion = i[0]
            worst_emotion_str = worst_emotion_str + temp_emotion + "\n"

        emotion_str = "Best Possible Emotions\n%s\nWorst Possible Emotions\n%s"%(best_emotion_str,worst_emotion_str)
        self.result_label.configure(text=emotion_str)

def main():
    root = Tk()
    root.title('Emotion Predictor App')
    root.geometry('800x600')
    app = EmotionPredictor(root)
    app.pack(fill = BOTH, expand=True)
    root.mainloop()

main()
