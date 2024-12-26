'''

Challenge 14 by Arish Bawani


'''

import tkinter

class HollywoodStar:
    def __init__(self):
        # main tk window
        self.root_window = tkinter.Tk()
        self.root_window.title("My Star on Hollywood Walk of Fame")
        
        # create canvas for star
        self.drawing_area = tkinter.Canvas(self.root_window, width=400, height=400, bg="white")
        
        # draw star
        self.star_shape = self.drawing_area.create_polygon(
            200, 100, 220, 160, 280, 160, 240, 200, 260, 260, 
            200, 230, 140, 260, 160, 200, 120, 160, 180, 160,
            fill="white", outline="black")
        
        # button with name
        self.name_button = tkinter.Button(self.root_window, text="Arish Bawani", command=self.toggle_star_colors)
        self.button_position = self.drawing_area.create_window(200, 200, window=self.name_button)
        
        # show canvas
        self.drawing_area.pack()
        
        # start loop
        tkinter.mainloop()

    def toggle_star_colors(self):
        # invert colors
        self.drawing_area.itemconfig(self.star_shape, fill="black")
        self.name_button.config(bg="black", fg="white")

# main
if __name__ == "__main__":
    my_gui = HollywoodStar()
