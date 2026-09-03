
import tkinter as tk
import Day_4_Api
import Day_4_Sqlite
def format_coordinates_lat(lat):
    return f"Lat: {round(float(lat), 2)}"
def format_coordinates_lon(lon):
    return f"Lon: {round(float(lon), 2)}"

def configure_window():
    pos = Day_4_Api.get_iss_position()
    lat = pos['latitude']
    lon = pos['longitude']
    lat = format_coordinates_lat(lat)
    lon = format_coordinates_lon(lon)

    root = tk.Tk()
    root.title('ISS Tracker')
    pos_label = tk.Label(root, text='No position logged currently\nIf positions have been logged it will appear here')
    pos_label.pack(pady=15)
    frame = tk.Frame(root)
    pp_box = tk.Listbox(frame, width=40)
    pp_box.pack(pady=20)
    pp_box.insert(0, f'Latitude: {lat}, Longitude: {lon}')
    def show():
        frame.pack(pady=10)
    def hide():
        frame.pack_forget()
    def click_Check():
        new_lon = Day_4_Api.get_iss_position()['longitude']
        new_lat = Day_4_Api.get_iss_position()['latitude']
        pos_label.config(text= f'Latitude: {new_lat}, Longitude: {new_lon}')
        pp_box.insert(0, f'Latitude: {new_lat}, Longitude: {new_lon}')
    check_pos = tk.Button(root, text='Check Iss position', command=click_Check)
    check_pos.pack(pady=10)
    display_position_button = tk.Button(root, text='Display logged positions', command=show)
    display_position_button.pack(pady=10)
    hide_position_button = tk.Button(root, text='Hide logged positions', command=hide)
    hide_position_button.pack(pady=10)
    root.config(bg='light blue')
    root.mainloop()
    


configure_window()