import PySimpleGUI as sg
from database import database_keys, database_video_ids
from data_visualization import show_graphs

def id_extractor(link):
    index = link.find("=")
    return link[index + 1:]

def gui(scraper):
    layout = [
        [sg.T("Youtube Data Scraper", font='DEFAULT 25')],
        [sg.T("New Video Link")],  
        [sg.InputText(key='-LINKIN-')], 
        [sg.B("INSERT DATA", font='_ 14')],
        [sg.T("Browse database")],
        [sg.Combo(database_keys(), key='-DBDD-', readonly=True)],
        [sg.B("GET DATA", font='_ 14')],
        [sg.B("EXIT", font='_ 14')]
    ]   

    window = sg.Window("Youtube Data Scraper", layout, font='_ 16')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "EXIT":  
            break   

        if event == "INSERT DATA":
            video_id = id_extractor(values['-LINKIN-'])
            # print(video_id)
            title = scraper.scrape(video_id)
            window['-DBDD-'].update(title, database_keys())

        if event == "GET DATA":
            # print(values['-DBDD-'])
            video_id = database_video_ids(values['-DBDD-'])
            scraper.scrape(video_id)
            show_graphs(values['-DBDD-'])

    window.close()