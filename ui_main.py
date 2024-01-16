# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainilDzNi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 732)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setWindowTitle(u"SubGPT")
        icon = QIcon()
        icon.addFile(u":/images/images/images/title_bar_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.CentralWidget.setFont(font)
        self.CentralWidget.setStyleSheet(u"/*\n"
"A child object is stored inside its parent object, but it doesn\u2019t necessarily inherit from it. \n"
"For example, if a QPushButton is inside a QFrame, then QPushButton doesn't inherit from QFrame, but it is an object inside that QFrame object.\n"
"https://doc.qt.io/qt-6/stylesheet-syntax.html\n"
"*/\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"* {\n"
"    border: none;\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget { \n"
"   background-color: transparent;\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QPushButton {\n"
"	background-repeat: no-repeat; \n"
"	background-position: center;\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 128, 255)"
                        "; /* Light blue*/\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	color: gray;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QComboBox{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QTableWidget::item{\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(0, 128, 255);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 4px;\n"
"    border: 1px so"
                        "lid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: rgb(33, 37, 43);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 86);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////*/\n"
" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background-color: rgb(153, 204, 255);\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    background: rgb(55, 63, 77);\n"
"    hei"
                        "ght: 10px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    background: rgb(55, 63, 77);\n"
"    height: 10px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background-color: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background-color: none;\n"
" }\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(153, 204, 255);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 10px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   "
                        " border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 10px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////"
                        "////////////// */\n"
"QFrame#IconFrame {\n"
"	border-image: url(:/images/images/images/icon.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QWidget#CentralWidget {	\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QFrame#LeftMenuBar, #ContentTop, #BottomBar  {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPlainTextEdit#prompt_edit {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.CentralWidget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.LeftMenuBar = QFrame(self.CentralWidget)
        self.LeftMenuBar.setObjectName(u"LeftMenuBar")
        self.LeftMenuBar.setMinimumSize(QSize(60, 0))
        self.LeftMenuBar.setMaximumSize(QSize(60, 16777215))
        self.LeftMenuBar.setFrameShape(QFrame.NoFrame)
        self.LeftMenuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftMenuBar)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.MenuFrame = QFrame(self.LeftMenuBar)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setFrameShape(QFrame.NoFrame)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.MenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.BottomMenu = QFrame(self.MenuFrame)
        self.BottomMenu.setObjectName(u"BottomMenu")
        sizePolicy.setHeightForWidth(self.BottomMenu.sizePolicy().hasHeightForWidth())
        self.BottomMenu.setSizePolicy(sizePolicy)
        self.BottomMenu.setFrameShape(QFrame.NoFrame)
        self.BottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.BottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.BottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon1)

        self.verticalLayout_9.addWidget(self.btn_settings)

        self.btn_info = QPushButton(self.BottomMenu)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.btn_info)


        self.verticalMenuLayout.addWidget(self.BottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.MenuFrame)


        self.horizontalLayout_2.addWidget(self.LeftMenuBar)

        self.SettingsExpand = QFrame(self.CentralWidget)
        self.SettingsExpand.setObjectName(u"SettingsExpand")
        sizePolicy.setHeightForWidth(self.SettingsExpand.sizePolicy().hasHeightForWidth())
        self.SettingsExpand.setSizePolicy(sizePolicy)
        self.SettingsExpand.setMinimumSize(QSize(0, 0))
        self.SettingsExpand.setMaximumSize(QSize(0, 16777215))
        self.SettingsExpand.setStyleSheet(u"")
        self.SettingsExpand.setFrameShape(QFrame.NoFrame)
        self.SettingsExpand.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SettingsExpand)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.IconFrame = QFrame(self.SettingsExpand)
        self.IconFrame.setObjectName(u"IconFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IconFrame.sizePolicy().hasHeightForWidth())
        self.IconFrame.setSizePolicy(sizePolicy1)
        self.IconFrame.setMinimumSize(QSize(0, 150))
        self.IconFrame.setFrameShape(QFrame.StyledPanel)
        self.IconFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.IconFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout_7.addWidget(self.IconFrame)

        self.TokenFrame = QFrame(self.SettingsExpand)
        self.TokenFrame.setObjectName(u"TokenFrame")
        sizePolicy1.setHeightForWidth(self.TokenFrame.sizePolicy().hasHeightForWidth())
        self.TokenFrame.setSizePolicy(sizePolicy1)
        self.TokenFrame.setMinimumSize(QSize(0, 0))
        self.TokenFrame.setMaximumSize(QSize(16777215, 16777215))
        self.TokenFrame.setFrameShape(QFrame.StyledPanel)
        self.TokenFrame.setFrameShadow(QFrame.Raised)
        self.TokenFrame.setLineWidth(1)
        self.verticalLayout_11 = QVBoxLayout(self.TokenFrame)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.lbl_token = QLabel(self.TokenFrame)
        self.lbl_token.setObjectName(u"lbl_token")
        self.lbl_token.setFont(font)

        self.verticalLayout_11.addWidget(self.lbl_token)

        self.token_edit = QPlainTextEdit(self.TokenFrame)
        self.token_edit.setObjectName(u"token_edit")
        sizePolicy.setHeightForWidth(self.token_edit.sizePolicy().hasHeightForWidth())
        self.token_edit.setSizePolicy(sizePolicy)
        self.token_edit.setMinimumSize(QSize(0, 0))
        self.token_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.token_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_11.addWidget(self.token_edit)

        self.lbl_tokeb_info = QLabel(self.TokenFrame)
        self.lbl_tokeb_info.setObjectName(u"lbl_tokeb_info")

        self.verticalLayout_11.addWidget(self.lbl_tokeb_info)

        self.lbl_api_url = QLabel(self.TokenFrame)
        self.lbl_api_url.setObjectName(u"lbl_api_url")

        self.verticalLayout_11.addWidget(self.lbl_api_url)


        self.verticalLayout_7.addWidget(self.TokenFrame)

        self.ModelFrame = QFrame(self.SettingsExpand)
        self.ModelFrame.setObjectName(u"ModelFrame")
        sizePolicy1.setHeightForWidth(self.ModelFrame.sizePolicy().hasHeightForWidth())
        self.ModelFrame.setSizePolicy(sizePolicy1)
        self.ModelFrame.setFrameShape(QFrame.StyledPanel)
        self.ModelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.ModelFrame)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.lbl_model = QLabel(self.ModelFrame)
        self.lbl_model.setObjectName(u"lbl_model")
        sizePolicy1.setHeightForWidth(self.lbl_model.sizePolicy().hasHeightForWidth())
        self.lbl_model.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.lbl_model)

        self.combo_model = QComboBox(self.ModelFrame)
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.setObjectName(u"combo_model")
        sizePolicy1.setHeightForWidth(self.combo_model.sizePolicy().hasHeightForWidth())
        self.combo_model.setSizePolicy(sizePolicy1)
        self.combo_model.setMinimumSize(QSize(0, 40))
        self.combo_model.setMaximumSize(QSize(16777215, 16777215))
        self.combo_model.setFont(font)

        self.verticalLayout_10.addWidget(self.combo_model)


        self.verticalLayout_7.addWidget(self.ModelFrame)

        self.CosineFrame = QFrame(self.SettingsExpand)
        self.CosineFrame.setObjectName(u"CosineFrame")
        sizePolicy1.setHeightForWidth(self.CosineFrame.sizePolicy().hasHeightForWidth())
        self.CosineFrame.setSizePolicy(sizePolicy1)
        self.CosineFrame.setFrameShape(QFrame.StyledPanel)
        self.CosineFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.CosineFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.box_cosine = QCheckBox(self.CosineFrame)
        self.box_cosine.setObjectName(u"box_cosine")

        self.verticalLayout_12.addWidget(self.box_cosine)

        self.label = QLabel(self.CosineFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_12.addWidget(self.label)

        self.label_2 = QLabel(self.CosineFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_12.addWidget(self.label_2)


        self.verticalLayout_7.addWidget(self.CosineFrame)


        self.horizontalLayout_2.addWidget(self.SettingsExpand)

        self.ContentBox = QFrame(self.CentralWidget)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.NoFrame)
        self.ContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 9, 9)
        self.ContentTop = QFrame(self.ContentBox)
        self.ContentTop.setObjectName(u"ContentTop")
        self.ContentTop.setMinimumSize(QSize(0, 50))
        self.ContentTop.setMaximumSize(QSize(16777215, 50))
        self.ContentTop.setFrameShape(QFrame.NoFrame)
        self.ContentTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ContentTop)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_title = QLabel(self.ContentTop)
        self.lbl_title.setObjectName(u"lbl_title")

        self.horizontalLayout.addWidget(self.lbl_title)


        self.verticalLayout_2.addWidget(self.ContentTop)

        self.ContentBottom = QFrame(self.ContentBox)
        self.ContentBottom.setObjectName(u"ContentBottom")
        self.ContentBottom.setFrameShape(QFrame.NoFrame)
        self.ContentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.PagesContainer = QFrame(self.ContentBottom)
        self.PagesContainer.setObjectName(u"PagesContainer")
        self.PagesContainer.setFrameShape(QFrame.NoFrame)
        self.PagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.PagesContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget = QStackedWidget(self.PagesContainer)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout = QVBoxLayout(self.Home)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.GridLayout = QGridLayout()
        self.GridLayout.setSpacing(6)
        self.GridLayout.setObjectName(u"GridLayout")
        self.GridLayout.setContentsMargins(9, 9, 9, 9)
        self.lbl_input = QLabel(self.Home)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setFont(font)

        self.GridLayout.addWidget(self.lbl_input, 0, 0, 1, 1)

        self.btn_open = QPushButton(self.Home)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QSize(0, 30))
        self.btn_open.setMaximumSize(QSize(150, 30))
        self.btn_open.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open.setIcon(icon3)

        self.GridLayout.addWidget(self.btn_open, 1, 1, 1, 1)

        self.subtitle_template = QLineEdit(self.Home)
        self.subtitle_template.setObjectName(u"subtitle_template")
        self.subtitle_template.setEnabled(True)
        sizePolicy.setHeightForWidth(self.subtitle_template.sizePolicy().hasHeightForWidth())
        self.subtitle_template.setSizePolicy(sizePolicy)
        self.subtitle_template.setMinimumSize(QSize(0, 30))
        self.subtitle_template.setDragEnabled(True)
        self.subtitle_template.setReadOnly(True)

        self.GridLayout.addWidget(self.subtitle_template, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout)

        self.GridLayout2 = QGridLayout()
        self.GridLayout2.setSpacing(6)
        self.GridLayout2.setObjectName(u"GridLayout2")
        self.GridLayout2.setContentsMargins(9, 9, 9, 9)
        self.lbl_language = QLabel(self.Home)
        self.lbl_language.setObjectName(u"lbl_language")

        self.GridLayout2.addWidget(self.lbl_language, 0, 0, 1, 1)

        self.combo_lang = QComboBox(self.Home)
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.combo_lang.setObjectName(u"combo_lang")
        self.combo_lang.setMinimumSize(QSize(0, 30))

        self.GridLayout2.addWidget(self.combo_lang, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout2)

        self.GridLayout3 = QGridLayout()
        self.GridLayout3.setSpacing(6)
        self.GridLayout3.setObjectName(u"GridLayout3")
        self.GridLayout3.setContentsMargins(9, 9, 9, 9)
        self.lbl_prompt = QLabel(self.Home)
        self.lbl_prompt.setObjectName(u"lbl_prompt")

        self.GridLayout3.addWidget(self.lbl_prompt, 0, 0, 1, 1)

        self.prompt_edit = QPlainTextEdit(self.Home)
        self.prompt_edit.setObjectName(u"prompt_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prompt_edit.sizePolicy().hasHeightForWidth())
        self.prompt_edit.setSizePolicy(sizePolicy2)
        self.prompt_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.prompt_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.prompt_edit.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.GridLayout3.addWidget(self.prompt_edit, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.GridLayout3)

        self.btn_next = QPushButton(self.Home)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QSize(150, 50))
        self.btn_next.setMaximumSize(QSize(150, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_next, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.StackedWidget.addWidget(self.Home)
        self.PostProcessing = QWidget()
        self.PostProcessing.setObjectName(u"PostProcessing")
        self.verticalLayout_4 = QVBoxLayout(self.PostProcessing)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ScrollArea = QScrollArea(self.PostProcessing)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollAreaWidgetContents = QWidget()
        self.ScrollAreaWidgetContents.setObjectName(u"ScrollAreaWidgetContents")
        self.ScrollAreaWidgetContents.setGeometry(QRect(0, 0, 871, 568))
        self.verticalLayout_5 = QVBoxLayout(self.ScrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.data_table = QTableWidget(self.ScrollAreaWidgetContents)
        self.data_table.setObjectName(u"data_table")
        sizePolicy.setHeightForWidth(self.data_table.sizePolicy().hasHeightForWidth())
        self.data_table.setSizePolicy(sizePolicy)
        self.data_table.setMinimumSize(QSize(0, 0))
        self.data_table.horizontalHeader().setStretchLastSection(False)
        self.data_table.verticalHeader().setVisible(True)
        self.data_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.data_table)

        self.ScrollArea.setWidget(self.ScrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.ScrollArea)

        self.NavBox = QFrame(self.PostProcessing)
        self.NavBox.setObjectName(u"NavBox")
        sizePolicy.setHeightForWidth(self.NavBox.sizePolicy().hasHeightForWidth())
        self.NavBox.setSizePolicy(sizePolicy)
        self.NavBox.setMinimumSize(QSize(0, 30))
        self.NavBox.setFrameShape(QFrame.StyledPanel)
        self.NavBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NavBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back = QPushButton(self.NavBox)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(0, 30))
        self.btn_back.setMaximumSize(QSize(150, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.btn_delete_row = QPushButton(self.NavBox)
        self.btn_delete_row.setObjectName(u"btn_delete_row")
        self.btn_delete_row.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_delete_row.sizePolicy().hasHeightForWidth())
        self.btn_delete_row.setSizePolicy(sizePolicy)
        self.btn_delete_row.setMinimumSize(QSize(0, 30))
        self.btn_delete_row.setMaximumSize(QSize(150, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_row.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.btn_delete_row)

        self.btn_start = QPushButton(self.NavBox)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 30))
        self.btn_start.setMaximumSize(QSize(150, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.btn_start)

        self.btn_save = QPushButton(self.NavBox)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 30))
        self.btn_save.setMaximumSize(QSize(150, 33))
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.btn_save)


        self.verticalLayout_4.addWidget(self.NavBox)

        self.StackedWidget.addWidget(self.PostProcessing)

        self.horizontalLayout_4.addWidget(self.StackedWidget)


        self.verticalLayout_6.addWidget(self.PagesContainer)


        self.verticalLayout_2.addWidget(self.ContentBottom)


        self.horizontalLayout_2.addWidget(self.ContentBox)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.LeftMenuBar.raise_()
        self.ContentBox.raise_()
        self.SettingsExpand.raise_()

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.btn_settings.setText("")
        self.btn_info.setText("")
        self.lbl_token.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">API Key:</span></p></body></html>", None))
        self.lbl_tokeb_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#a1a1a1;\">You can get the API keys from here:</span></p></body></html>", None))
        self.lbl_api_url.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://platform.openai.com/api-keys\"><span style=\" text-decoration: underline; color:#739ef7;\">https://platform.openai.com/api-keys</span></a></p></body></html>", None))
        self.lbl_model.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Model:</span></p></body></html>", None))
        self.combo_model.setItemText(0, QCoreApplication.translate("MainWindow", u"GPT4", None))
        self.combo_model.setItemText(1, QCoreApplication.translate("MainWindow", u"GPT3", None))

        self.box_cosine.setText(QCoreApplication.translate("MainWindow", u"Cosine Similarty", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Used to compare input to output embeddings.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Could improve accuracy at the expense of more tokens and time.</span></p></body></html>", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"Automated Translation of Subtitle Templates using ChatGPT", None))
        self.lbl_input.setText(QCoreApplication.translate("MainWindow", u"Subtitle Template", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.subtitle_template.setText("")
        self.subtitle_template.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click Open to choose a file", None))
        self.lbl_language.setText(QCoreApplication.translate("MainWindow", u"Target Language", None))
        self.combo_lang.setItemText(0, QCoreApplication.translate("MainWindow", u"Arabic", None))
        self.combo_lang.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.lbl_prompt.setText(QCoreApplication.translate("MainWindow", u"Edit Prompt", None))
        self.prompt_edit.setPlainText(QCoreApplication.translate("MainWindow", u"As an expert subtitle translator, your task is to translate the provided subtitles.\n"
"Please adhere to the following guidelines:\n"
"1] Maintain the integrity of each sentence - do not merge them.\n"
"2] Ensure that the translated subtitles retain the same order and length as the original.\n"
"3] Aim for fluency in your translations, paraphrasing where necessary for a natural flow.\n"
"Remember, your role is solely translation. No additional responses are required. Keep it as simple as possible. ", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btn_delete_row.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        pass
    # retranslateUi

