from PySide6.QtWidgets import (QMessageBox, QFileDialog, QSizePolicy, QGroupBox, QTableWidgetItem,
                               QHBoxLayout, QFrame, QSizePolicy, QLabel, QVBoxLayout, QHeaderView,
                               QLineEdit, QPushButton, QWidget, QAbstractItemView)
from PySide6.QtCore import QDir, QSize, QEasingCurve, QPropertyAnimation, Qt
from PySide6.QtGui import QIcon, QPainter, QColor
from srt import parse, SRTParseError, compose
from openai import AsyncOpenAI, APIConnectionError, AuthenticationError, embeddings
from qasync import asyncSlot
from asyncio import sleep
import time
import numpy as np
import tiktoken

template_file = None

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

def issue_warning_error(main_window, title, text): 
    QMessageBox.warning(main_window, title, text)

def load_template_file(main_window):
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
    except FileNotFoundError:
        issue_warning_error(main_window, "Warning", "File not found")
    except SRTParseError:
        issue_warning_error(main_window, "Error", "Can't parse the template file\nFile might be corrupted")

def check_inputs(main_window):      
    if not main_window.subtitle_template.text():
        issue_warning_error(main_window, "Warning", "Specify a template file")
    else:
        main_window.StackedWidget.setCurrentWidget(main_window.PostProcessing)
        display_template_content(main_window)


def display_template_content(main_window):
    main_window.data_table.setColumnCount(2)
    main_window.data_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.horizontalHeader().setStretchLastSection(True)
    main_window.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    main_window.data_table.setHorizontalHeaderLabels(["Source Text", "Target Text"])
    main_window.data_table.setRowCount(len(template_file))
    main_window.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    for i, sentence in enumerate(template_file):
        item = QTableWidgetItem(sentence.content)
        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
        main_window.data_table.setItem(i, 0, item)

# Enable or disable the delete button based on row selection
def row_selected(main_window):
    indexes = main_window.data_table.selectionModel().selectedRows()
    if len(indexes) == 0:
        main_window.btn_delete_row.setEnabled(False)
    else:
        main_window.btn_delete_row.setEnabled(True)

# Removes selected row on delete button click
def delete_row(main_window):
    global template_file
    selectedRows = main_window.data_table.selectionModel().selectedRows()
    for index in sorted(selectedRows, reverse=True):
        row_text = main_window.data_table.item(index.row(), 0).text() 
        main_window.data_table.removeRow(index.row())
        for subtitle in template_file:
            if subtitle.content == row_text:
                template_file.remove(subtitle)

def save_template_file(main_window):
    global template_file
    target_lang = main_window.combo_lang.currentText()
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getSaveFileName(None,"Save File", "","Custom Files (*.srt);;All Files (*)", options=options)
    if fileName:
        for i, subtitle in enumerate(template_file):
            table_row_translation = main_window.data_table.item(i, 1)
            if table_row_translation is not None:
                translated_text = table_row_translation.text()
                if target_lang == "Arabic":
                    translated_text = translated_text.replace("\u202B", "").replace("\u202C", "")
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

@asyncSlot()
async def communicate_with_api(main_window):

    # CHANGE SOME BUTTONS' BEHAVIOR
    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-pause.png"))
    main_window.btn_start.setEnabled(False)
    main_window.btn_back.setEnabled(False)
    main_window.btn_settings.setEnabled(False)
    main_window.btn_delete_row.setEnabled(False)
    main_window.btn_save.setEnabled(False)

    main_window.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.NoFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.NoSelection)

    target_lang = main_window.combo_lang.currentText()

    prompt = f"""
    Translate to {target_lang}.
    Please keep the pipe operator | in each sentence.
    {main_window.prompt_edit.toPlainText()}\n
    """
    enc = tiktoken.get_encoding("cl100k_base")
    prompt_tokens = enc.encode(prompt)
    current_tokens = len(prompt_tokens)
    max_tokens = 4000
    sentences_list = []
    sentences = ""
    for i, sentence in enumerate(template_file):
        sen = sentence.content.strip() 
        sen = sen.replace("\n", "|")
        sen = f"{sen}\n"
        tokens = enc.encode(sen)
        if current_tokens + len(tokens) > max_tokens:
            sentences_list.append(sentences)
            sentences = ""
            current_tokens = len(prompt_tokens)
        current_tokens += len(tokens)
        sentences += sen 
    if sentences:
          sentences_list.append(sentences)  
    try:
        translations = ""  
        num_requests_embedding = 0
        num_requests_model = 0
        client = AsyncOpenAI(api_key = main_window.token_edit.toPlainText()) 
        model = main_window.combo_model.currentText()
        if (model == "GPT4"):
            model = "gpt-4"
        else:
            model = "gpt-3.5-turbo"
        
        start_time = time.time()
        for i in range(len(sentences_list)):             
            if (main_window.box_cosine.isChecked()):
                sentences_embeddings = await get_embeddings(client, sentences[i])
                num_requests_embedding += 1
            while True:               
                response =  await client.chat.completions.create (
                    model=model,
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": sentences_list[i]}
                    ]
                )
                num_requests_model += 1
                # Get the translated text
                translations_part = response.choices[0].message.content

                end_time = time.time()
                elapsed_time = end_time - start_time
                if ((num_requests_embedding == 3 or num_requests_model == 3) and elapsed_time < 60):
                    await sleep(60)
                    num_requests_embedding = 0
                    num_requests_model = 0
                elif (elapsed_time >= 60):
                    start_time = time.time()
                    num_requests_embedding = 0
                    num_requests_model = 0

                if (main_window.box_cosine.isChecked()):
                    translations_embeddings = await get_embeddings(client, translations_part)
                    score = cosine_similarity(sentences_embeddings, translations_embeddings)
                    if score > 0.6:
                        translations += translations_part 
                        break
                else:
                    translations += translations_part
                    break
            

        translations_split = translations.split("\n")
        for i, sentence in enumerate(translations_split):
            formatted_text = sentence.replace("|", "\n").strip()
            if target_lang == "Arabic":
                formatted_text = "\u202B" + formatted_text + "\u202C"

            item = QTableWidgetItem(formatted_text)
            main_window.data_table.setItem(i, 1, item)
        
        main_window.btn_save.setEnabled(True)
    except AuthenticationError:
        issue_warning_error(main_window, "Invalid API Key", "Please provide a valid API key")
    except APIConnectionError:
        issue_warning_error(main_window, "No API Key Provide", "Please provide an API key")

    main_window.btn_start.setIcon(QIcon(":/icons/images/icons/cil-media-play.png"))
    main_window.btn_start.setEnabled(True)
    main_window.btn_back.setEnabled(True)
    main_window.btn_settings.setEnabled(True)
    main_window.btn_delete_row.setEnabled(True)

    main_window.data_table.setEditTriggers(QAbstractItemView.AllEditTriggers)
    main_window.data_table.setFocusPolicy(Qt.StrongFocus)
    main_window.data_table.setSelectionMode(QAbstractItemView.ExtendedSelection)


        