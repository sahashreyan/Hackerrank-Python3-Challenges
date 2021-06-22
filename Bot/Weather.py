from tkinter import *
import requests
def find_weather():
    ADDRESS = f"http://api.openweathermap.org/data/2.5/weather?q={city.get()}&APPID=d879846ec0eca9455c52f47f3f3a3191&units=metric"
    res = requests.get(ADDRESS)
    data = res.json()
    global description
    global t
    global t_min
    global t_max
    description = Label(window, text=data['weather'][0]['main'])
    description.grid(row=2, column=1)
    t = Label(window, text=str(data['main']['temp'])+"∘C")
    t.grid(row=3, column=1)
    t = Label(window, text=str(data['main']['temp_min'])+"∘C")
    t.grid(row=4, column=1)
    t = Label(window, text=str(data['main']['temp_max'])+"∘C")
    t.grid(row=5, column=1)
    
def delete():
    description.destroy()
    t.destroy()
    t_min.destroy()
    t_max.destroy()
    
window = Tk()
window.title("Weather App")
city_name = Label(window, text='City:')
city_name.grid(row=1, column=0, padx=45, pady=50)
city = Entry(window, width=40)
city.grid(row=1, column=1)
city.focus()
search = Button(window, text='Search', command=find_weather)
search.grid(row=1, column=2, padx=15, pady=5)
clear = Button(window, text='Clear', command=delete)
clear.grid(row=1, column=3, padx=15, pady=5)
desc = Label(window, text='Description:')
desc.grid(row=2, column=0)
temp = Label(window, text='Temperature:')
temp.grid(row=3,  column=0)
temp_min = Label(window, text="Temperature Min:")
temp_min.grid(row=4, column=0)
temp_max = Label(window, text="Temperature Max:")
temp_max.grid(row=5, column=0)

window.mainloop()

