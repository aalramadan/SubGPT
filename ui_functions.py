from PySide6.QtWidgets import (QMessageBox, QFileDialog, QTableWidgetItem,
                               QHeaderView,QAbstractItemView)
from PySide6.QtCore import QSize, QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QIcon, QMovie 
from srt import parse, SRTParseError, compose
from openai import AsyncOpenAI, APIConnectionError, AuthenticationError
from qasync import asyncSlot
from asyncio import sleep
import numpy as np
import tiktoken
import json
import re

template_file = None # Stores the loaded .srt file
template_loaded = False # Checked if template is loaded. Needed so that "Next" button doesn't keep loading the same file.
async_signal_used = False # Needed for the Start/Pause button

class Settings:
    EXPAND_WIDTH = 360
    TIME_ANIMATION = 500

    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0.2 rgb(0, 128, 255), stop:0.201 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    background-position: left center;
    """

def button_click(main_window, btn):
    btn_name = btn.objectName()
    if btn_name == "btn_back":
        main_window.StackedWidget.setCurrentWidget(main_window.Home)

def expand_settings(main_window):
    width = main_window.SettingsExpand.width()
    if width == 0:
        widthExtended = Settings.EXPAND_WIDTH 
    else:
        widthExtended = 0   
    main_window.left_box = QPropertyAnimation(main_window.SettingsExpand, b"minimumWidth")
    main_window.left_box.setDuration(Settings.TIME_ANIMATION)
    main_window.left_box.setStartValue(width)
    main_window.left_box.setEndValue(widthExtended)
    main_window.left_box.setEasingCurve(QEasingCurve.InOutQuart)
    main_window.left_box.start()

def on_box_cosine_changed(main_window, check_box):
    if check_box.isChecked():
        main_window.threshold_edit.setEnabled(True)
    else:
        main_window.threshold_edit.setEnabled(False)

def expand_about(main_window):
    width = main_window.AboutFrame.width()
    if width == 0:
        widthExtended = Settings.EXPAND_WIDTH 
    else:
        widthExtended = 0   
    main_window.left_box = QPropertyAnimation(main_window.AboutFrame, b"minimumWidth")
    main_window.left_box.setDuration(Settings.TIME_ANIMATION)
    main_window.left_box.setStartValue(width)
    main_window.left_box.setEndValue(widthExtended)
    main_window.left_box.setEasingCurve(QEasingCurve.InOutQuart)
    main_window.left_box.start()

def issue_warning_error(main_window, title, text): 
    QMessageBox.warning(main_window, title, text)

def load_template_file(main_window):
    global template_loaded
    dialog = QFileDialog()
    dialog.setNameFilters(["Custom Files (*.srt)", "All Files (*)"])
    selected_file = ""
    if dialog.exec_(): # Open a dialog window and waits. Finishes when file is selected.
        selected_file = dialog.selectedFiles()[0]
    try:
        if selected_file != "": # Needed in case dialog was simply opened and closed without selecting a file
            with open(selected_file, 'r', encoding='utf-8') as file: # Could throw FileNotFoundError
                template_content = file.read() 
            global template_file
            template_file = list(parse(template_content)) # Could throw SRTParseError
            template_file = [sentence for sentence in template_file if sentence.content.strip()] # Removes empty sentences
            main_window.subtitle_template.setText(selected_file)
            
            template_loaded = True
    except FileNotFoundError:
        issue_warning_error(main_window, "Warning", "File not found")
    except SRTParseError:
        issue_warning_error(main_window, "Error", "Can't parse the template file\nFile might be corrupted")

def check_inputs(main_window):
    global template_loaded      
    if not main_window.target_language.text():
        issue_warning_error(main_window, "Warning", "Specify a template file")    
    elif not main_window.subtitle_template.text():
        issue_warning_error(main_window, "Warning", "Specify a target language")
    else:
        main_window.StackedWidget.setCurrentWidget(main_window.PostProcessing)
        if template_loaded == True:
            display_template_content(main_window)
            template_loaded = False


def display_template_content(main_window):
    main_window.data_table.setRowCount(0)
    main_window.data_table.setColumnCount(2)
    main_window.data_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.horizontalHeader().setStretchLastSection(True)
    main_window.data_table.setHorizontalHeaderLabels(["Source Text", "Target Text"])
    main_window.data_table.setRowCount(len(template_file))
    for i, sentence in enumerate(template_file):
        item = QTableWidgetItem(sentence.content)
        main_window.data_table.setItem(i, 0, item)

# Enable or disable the delete button based on row selection
def items_selected(main_window):
    indexes = main_window.data_table.selectedItems()
    if len(indexes) == 0:
        main_window.btn_delete_row.setEnabled(False)
    else:
        main_window.btn_delete_row.setEnabled(True)


def shift_items_up(main_window):
    for j in range(main_window.data_table.columnCount()):
        items = [main_window.data_table.item(i, j).text() for i in range(main_window.data_table.rowCount()) if main_window.data_table.item(i, j)]
        for i in range(main_window.data_table.rowCount()):
            if i < len(items):
                main_window.data_table.setItem(i, j, QTableWidgetItem(items[i]))
            else:
                main_window.data_table.setItem(i, j, None)


# Removes selected row on delete button click
def delete_row(main_window):
    global template_file
    selectedItems = main_window.data_table.selectedItems()
    for item in selectedItems:    
        if item.column() == 0:
            item_text = item.text()
            for subtitle in template_file:
                if subtitle.content == item_text:
                    template_file.remove(subtitle)
        main_window.data_table.setItem(item.row(), item.column(), None)
    shift_items_up(main_window)

def save_template_file(main_window):
    global template_file
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getSaveFileName(None,"Save File", "","Custom Files (*.srt);;All Files (*)", options=options)
    if fileName:
        for i, subtitle in enumerate(template_file):
            table_row_translation = main_window.data_table.item(i, 1)
            if table_row_translation is not None:
                translated_text = table_row_translation.text()
                subtitle.content = translated_text.strip()

        with open(fileName, 'w', encoding="utf-8") as file:
            file.write(compose(template_file))
        
        QMessageBox.information(main_window, "File Saved", "File was written successfully!")

@asyncSlot() 
async def get_embeddings(client, text):
    embeddings_response = await client.embeddings.create(
        model='text-embedding-ada-002',
        input=text
    )
    return np.array(embeddings_response.data[0].embedding)


def cosine_similarity(sentences_embeddings, translations_embeddings):
    dot_product = np.dot(sentences_embeddings, translations_embeddings)

    # Compute the L2 norms (Euclidean lengths) of a and b
    norm_a = np.linalg.norm(sentences_embeddings)
    norm_b = np.linalg.norm(translations_embeddings)

    # Compute cosine similarity
    similarity = dot_product / (norm_a * norm_b)

    return similarity


def create_sentences_dictionaries(prompt, max_tokens, target_lang):
    enc = tiktoken.get_encoding("cl100k_base")
    prompt_tokens = enc.encode(prompt)
    current_tokens = len(prompt_tokens)

    sentences_list = {}
    num_dictionaries = 0
    sentences_list[f"{num_dictionaries}"] = {}

    for i, sentence in enumerate(template_file):         
        sen = sentence.content.strip()

        # Remove unicode characters if any
        sen = sen.replace("\u202b", "").replace("\u202c", "")

        # Replace multiple spaces with a single space
        tokens = enc.encode(sen)

        if current_tokens + len(tokens) > max_tokens:
            current_tokens = len(prompt_tokens)
            num_dictionaries = num_dictionaries + 1
            sentences_list[f"{num_dictionaries}"] = {}
        
        sentences_list[f"{num_dictionaries}"][f"s_{i}"] = sen
        current_tokens += len(tokens)

    return sentences_list


def disable_some_buttons(main_window):
    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-pause.png"))
    main_window.btn_start.setText("Pause")
    main_window.btn_back.setEnabled(False)
    main_window.btn_settings.setEnabled(False)
    main_window.btn_delete_row.setEnabled(False)
    main_window.btn_save.setEnabled(False)
    main_window.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.NoFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.NoSelection)


def enable_some_buttons(main_window):
    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
    main_window.btn_start.setText("Start")
    main_window.btn_back.setEnabled(True)
    main_window.btn_settings.setEnabled(True)
    main_window.btn_delete_row.setEnabled(True)
    main_window.btn_save.setEnabled(True)

    main_window.data_table.setEditTriggers(QAbstractItemView.AllEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.StrongFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.ExtendedSelection)

    
@asyncSlot()
async def communicate_with_api(main_window):
    global async_signal_used
    if not async_signal_used and main_window.btn_start.isChecked():
        async_signal_used = True
        disable_some_buttons(main_window)
         
        width = main_window.SettingsExpand.width()
        if width == Settings.EXPAND_WIDTH:
            expand_settings(main_window)

        movie = QMovie(":/gifs/images/loading.gif") 
        movie.setScaledSize(QSize(45, 45))
        main_window.loading_gif.setMovie(movie) 
        main_window.loading_gif.show()
        movie.start()

        client = AsyncOpenAI(api_key = main_window.token_edit.toPlainText()) 

        target_lang = main_window.target_language.text()

        prompt = f"""
        {main_window.prompt_edit.toPlainText()}
        The target language of translation is {target_lang}.
        This input is a JSON string. Please keep it as is and only replace the values with the translations.
        """
        max_tokens = int(main_window.max_tokens.text())
        sentences_list = create_sentences_dictionaries(prompt, max_tokens, target_lang)

        model = main_window.combo_model.currentText()

        if (model == "GPT4"):
            model = "gpt-4"
        else:
            model = "gpt-3.5-turbo" 

        row = 0 
        for _, outer_value in sentences_list.items():
            json_string = json.dumps(outer_value)                    
            try:   
                if main_window.box_cosine.isChecked():
                    sentences_embeddings = await get_embeddings(client, json_string) 
                while True:       
                    response =  await client.chat.completions.create (
                        model=model,
                        messages=[
                            {"role": "system", "content": prompt},
                            {"role": "user", "content": json_string}
                        ]
                    )         
                    dict_sentences = response.choices[0].message.content

                    try:
                        values = list(json.loads(dict_sentences).values())
                    except:
                        values = re.findall(r'": "(.*?)(?="[,}])', dict_sentences)
                
                    if main_window.alignment_box.isChecked():
                        if len(values) != len(outer_value.values()):
                            continue
                
                    if (main_window.box_cosine.isChecked()):
                        translations_embeddings = await get_embeddings(client, dict_sentences)
                        score = cosine_similarity(sentences_embeddings, translations_embeddings)
                        if score < float(main_window.threshold_edit.text()):
                            continue
                
                    for _, sentence in enumerate(values):
                        if target_lang == "Arabic":
                            sentence = "\u202b" + sentence + "\u202c"

                        item = QTableWidgetItem(sentence)
                        main_window.data_table.setItem(row, 1, item)
                        row = row + 1
                    main_window.repaint()
                    break
                
                if not main_window.btn_start.isChecked():
                    enable_some_buttons(main_window)
                    main_window.btn_settings.setEnabled(False)
                    main_window.btn_back.setEnabled(False)
                    movie.stop()
                    main_window.loading_gif.hide()
                    main_window.btn_start.setEnabled(True)
                    while not main_window.btn_start.isChecked():
                        await sleep(1)
                    disable_some_buttons(main_window)
                    main_window.loading_gif.setMovie(movie) 
                    main_window.loading_gif.show()
                    movie.start()         
            except AuthenticationError:
                issue_warning_error(main_window, "Invalid API Key", "Please provide a valid API key")
                enable_some_buttons(main_window)
                movie.stop()
                main_window.loading_gif.hide()
                return
            except APIConnectionError:
                issue_warning_error(main_window, "No API Key Provide", "Please provide an API key")
                enable_some_buttons(main_window)
                movie.stop()
                main_window.loading_gif.hide()
                return
            except Exception as e:
                issue_warning_error(main_window, "Error",f"Something happened: {e}")
                enable_some_buttons(main_window)
                movie.stop()
                main_window.loading_gif.hide()
                return
                
        enable_some_buttons(main_window)
        async_signal_used = True
        movie.stop() 
        main_window.loading_gif.hide()
    else:
        pass

        