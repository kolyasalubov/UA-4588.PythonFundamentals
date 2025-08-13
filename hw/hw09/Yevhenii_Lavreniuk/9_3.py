import tkinter as tk
from tkinter import font, messagebox
from pyowm import OWM

# Константи для розмірів вікна
HEIGHT = 450
WIDTH = 550

# API ключ для OpenWeatherMap
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Ініціалізація OWM
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    """Функція для отримання та відображення погоди"""
    try:
        # Отримуємо назву міста з поля вводу
        city = entry_field.get()
        
        # Перевіряємо чи введено назву міста
        if not city:
            label.config(text="Будь ласка, введіть назву міста!", 
                        bg='gold', fg='red')
            return
        
        # Отримуємо дані про погоду
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        
        # Отримуємо температуру в Цельсіях
        temperature = weather.temperature('celsius')
        
        # Формуємо текст для відображення
        weather_info = f"""
Місто: {city}
        
Стан: {weather.detailed_status.title()}

Температура: {temperature['temp']:.1f}°C
Відчувається як: {temperature['feels_like']:.1f}°C
Мін: {temperature['temp_min']:.1f}°C
Макс: {temperature['temp_max']:.1f}°C

Вологість: {weather.humidity}%
Вітер: {weather.wind().get('speed', 'N/A')} м/с

Хмарність: {weather.clouds}%
        """
        
        # Відображаємо інформацію в лейблі
        label.config(text=weather_info, 
                    bg='gold', 
                    fg='black',
                    justify='left')
        
    except Exception as e:
        # Обробка помилок (наприклад, неіснуюче місто)
        error_message = f"Помилка: {str(e)}\n\nПеревірте правильність назви міста"
        label.config(text=error_message, 
                    bg='gold', 
                    fg='red')

# Створення головного вікна
root = tk.Tk()
root.title("Weather Application")
root.resizable(False, False)  # Заборонити зміну розміру

# Створення канвасу
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Верхня рамка для поля вводу та кнопки
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Поле для введення назви міста
entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

# Додаємо можливість натиснути Enter для отримання погоди
entry_field.bind('<Return>', lambda event: get_weather())

# Кнопка для отримання погоди
button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", 
                   fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)  # Видалили lambda
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Нижня рамка для відображення результатів
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Лейбл для відображення інформації про погоду
label = tk.Label(lower_frame, 
                font=('Courier', 10),
                bg='gold',
                wraplength=300,  # Автоматичне перенесення тексту
                justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Початковий текст
label.config(text="Введіть назву міста та натисніть 'Get Weather'")

# Запуск головного циклу додатку
if __name__ == "__main__":
    root.mainloop()