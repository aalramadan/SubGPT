# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjfyrIP.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1515, 714)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1150, 650))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(u"SubGPT")
        icon = QIcon()
        icon.addFile(u":/images/images/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.CentralWidget.setFont(font1)
        self.CentralWidget.setStyleSheet(u"* {\n"
"    border: none;\n"
"	border-radius: 8px;\n"
"	font: 13pt \"Tahoma\";\n"
"}\n"
"QWidget { \n"
"   background-color: transparent;\n"
"   color: rgb(221, 221, 221);\n"
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
"	background-color: rgb(0, 128, 255); /* Light blue*/\n"
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
"	background-image: url(:/icons/images/icons/cil"
                        "-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QTableWidget {\n"
"    gridline-color: rgb(33, 37, 43); \n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 4px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
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
"	backg"
                        "round-color: rgb(33, 37, 43);\n"
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
"	min-height: 40px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    background: rgb(55, 63, 77);\n"
"    height: 10px;\n"
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
""
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
"	min-width: 40px;\n"
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
"    border: none;\n"
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
"/* //////////////////////"
                        "/////////////////////////////////////////////////////////////////////////// */\n"
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
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QFrame#IconFrame {\n"
"	border-image: url(:/images/images/images/icon.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QWidget#CentralWidget {	\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QFrame#LeftMenuBar, #ContentTop, #BottomBar  {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}"
                        "\n"
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
        self.LeftMenuBar.setFrameShape(QFrame.Shape.NoFrame)
        self.LeftMenuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.LeftMenuBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MenuFrame = QFrame(self.LeftMenuBar)
        self.MenuFrame.setObjectName(u"MenuFrame")
        self.MenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.MenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.MenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.BottomMenu = QFrame(self.MenuFrame)
        self.BottomMenu.setObjectName(u"BottomMenu")
        sizePolicy.setHeightForWidth(self.BottomMenu.sizePolicy().hasHeightForWidth())
        self.BottomMenu.setSizePolicy(sizePolicy)
        self.BottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.BottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.BottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.BottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font1)
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.btn_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_settings.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)

        self.verticalLayout_9.addWidget(self.btn_settings)

        self.btn_info = QPushButton(self.BottomMenu)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_info.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.btn_info)


        self.verticalMenuLayout.addWidget(self.BottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.MenuFrame)


        self.horizontalLayout_2.addWidget(self.LeftMenuBar)

        self.SettingsExpand = QFrame(self.CentralWidget)
        self.SettingsExpand.setObjectName(u"SettingsExpand")
        sizePolicy.setHeightForWidth(self.SettingsExpand.sizePolicy().hasHeightForWidth())
        self.SettingsExpand.setSizePolicy(sizePolicy)
        self.SettingsExpand.setMinimumSize(QSize(0, 0))
        self.SettingsExpand.setMaximumSize(QSize(0, 16777215))
        self.SettingsExpand.setStyleSheet(u"")
        self.SettingsExpand.setFrameShape(QFrame.Shape.NoFrame)
        self.SettingsExpand.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.SettingsExpand)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TokenFrame = QFrame(self.SettingsExpand)
        self.TokenFrame.setObjectName(u"TokenFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TokenFrame.sizePolicy().hasHeightForWidth())
        self.TokenFrame.setSizePolicy(sizePolicy1)
        self.TokenFrame.setMinimumSize(QSize(360, 0))
        self.TokenFrame.setMaximumSize(QSize(16777215, 16777215))
        self.TokenFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TokenFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.TokenFrame.setLineWidth(1)
        self.verticalLayout_11 = QVBoxLayout(self.TokenFrame)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_token = QLabel(self.TokenFrame)
        self.lbl_token.setObjectName(u"lbl_token")
        sizePolicy.setHeightForWidth(self.lbl_token.sizePolicy().hasHeightForWidth())
        self.lbl_token.setSizePolicy(sizePolicy)
        self.lbl_token.setFont(font1)

        self.verticalLayout_11.addWidget(self.lbl_token)

        self.token_edit = QLineEdit(self.TokenFrame)
        self.token_edit.setObjectName(u"token_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.token_edit.sizePolicy().hasHeightForWidth())
        self.token_edit.setSizePolicy(sizePolicy2)
        self.token_edit.setMinimumSize(QSize(0, 50))
        self.token_edit.setMaximumSize(QSize(16777215, 100))
        self.token_edit.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.token_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.token_edit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_11.addWidget(self.token_edit)

        self.api_url_text = QTextBrowser(self.TokenFrame)
        self.api_url_text.setObjectName(u"api_url_text")
        sizePolicy2.setHeightForWidth(self.api_url_text.sizePolicy().hasHeightForWidth())
        self.api_url_text.setSizePolicy(sizePolicy2)
        self.api_url_text.setMinimumSize(QSize(0, 80))
        self.api_url_text.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_11.addWidget(self.api_url_text)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.max_tokens = QLineEdit(self.TokenFrame)
        self.max_tokens.setObjectName(u"max_tokens")
        sizePolicy2.setHeightForWidth(self.max_tokens.sizePolicy().hasHeightForWidth())
        self.max_tokens.setSizePolicy(sizePolicy2)
        self.max_tokens.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.max_tokens, 1, 1, 1, 1)

        self.lbl_max_tokens = QLabel(self.TokenFrame)
        self.lbl_max_tokens.setObjectName(u"lbl_max_tokens")
        sizePolicy.setHeightForWidth(self.lbl_max_tokens.sizePolicy().hasHeightForWidth())
        self.lbl_max_tokens.setSizePolicy(sizePolicy)
        self.lbl_max_tokens.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lbl_max_tokens, 1, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_2)

        self.alignment_box = QCheckBox(self.TokenFrame)
        self.alignment_box.setObjectName(u"alignment_box")
        sizePolicy.setHeightForWidth(self.alignment_box.sizePolicy().hasHeightForWidth())
        self.alignment_box.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.alignment_box)

        self.alignment_fix_info = QTextBrowser(self.TokenFrame)
        self.alignment_fix_info.setObjectName(u"alignment_fix_info")
        sizePolicy2.setHeightForWidth(self.alignment_fix_info.sizePolicy().hasHeightForWidth())
        self.alignment_fix_info.setSizePolicy(sizePolicy2)
        self.alignment_fix_info.setMinimumSize(QSize(0, 80))
        self.alignment_fix_info.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_11.addWidget(self.alignment_fix_info)

        self.lbl_model = QLabel(self.TokenFrame)
        self.lbl_model.setObjectName(u"lbl_model")
        sizePolicy.setHeightForWidth(self.lbl_model.sizePolicy().hasHeightForWidth())
        self.lbl_model.setSizePolicy(sizePolicy)
        self.lbl_model.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_11.addWidget(self.lbl_model)

        self.combo_model = QComboBox(self.TokenFrame)
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.setObjectName(u"combo_model")
        sizePolicy.setHeightForWidth(self.combo_model.sizePolicy().hasHeightForWidth())
        self.combo_model.setSizePolicy(sizePolicy)
        self.combo_model.setMinimumSize(QSize(0, 50))
        self.combo_model.setMaximumSize(QSize(16777215, 16777215))
        self.combo_model.setFont(font1)

        self.verticalLayout_11.addWidget(self.combo_model)

        self.horizontalSpacer = QSpacerItem(40, 60, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer)

        self.box_cosine = QCheckBox(self.TokenFrame)
        self.box_cosine.setObjectName(u"box_cosine")
        sizePolicy.setHeightForWidth(self.box_cosine.sizePolicy().hasHeightForWidth())
        self.box_cosine.setSizePolicy(sizePolicy)
        self.box_cosine.setMinimumSize(QSize(0, 30))
        self.box_cosine.setMaximumSize(QSize(16777215, 16777215))
        self.box_cosine.setFont(font1)

        self.verticalLayout_11.addWidget(self.box_cosine)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_threshold = QLabel(self.TokenFrame)
        self.lbl_threshold.setObjectName(u"lbl_threshold")
        self.lbl_threshold.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lbl_threshold.sizePolicy().hasHeightForWidth())
        self.lbl_threshold.setSizePolicy(sizePolicy)
        self.lbl_threshold.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lbl_threshold, 1, 0, 1, 1)

        self.threshold_edit = QLineEdit(self.TokenFrame)
        self.threshold_edit.setObjectName(u"threshold_edit")
        self.threshold_edit.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.threshold_edit.sizePolicy().hasHeightForWidth())
        self.threshold_edit.setSizePolicy(sizePolicy2)
        self.threshold_edit.setMinimumSize(QSize(0, 50))
        self.threshold_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.threshold_edit.setReadOnly(False)

        self.gridLayout.addWidget(self.threshold_edit, 1, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout)

        self.cosine_info = QTextBrowser(self.TokenFrame)
        self.cosine_info.setObjectName(u"cosine_info")
        sizePolicy2.setHeightForWidth(self.cosine_info.sizePolicy().hasHeightForWidth())
        self.cosine_info.setSizePolicy(sizePolicy2)
        self.cosine_info.setMinimumSize(QSize(0, 0))
        self.cosine_info.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_11.addWidget(self.cosine_info)


        self.verticalLayout_7.addWidget(self.TokenFrame)


        self.horizontalLayout_2.addWidget(self.SettingsExpand, 0, Qt.AlignmentFlag.AlignTop)

        self.ContentBox = QFrame(self.CentralWidget)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.ContentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ContentTop = QFrame(self.ContentBox)
        self.ContentTop.setObjectName(u"ContentTop")
        self.ContentTop.setMinimumSize(QSize(0, 60))
        self.ContentTop.setMaximumSize(QSize(16777215, 50))
        self.ContentTop.setFrameShape(QFrame.Shape.NoFrame)
        self.ContentTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.ContentTop)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_title = QLabel(self.ContentTop)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_title.setMargin(5)

        self.horizontalLayout.addWidget(self.lbl_title)

        self.frame = QFrame(self.ContentTop)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.loading_gif = QLabel(self.frame)
        self.loading_gif.setObjectName(u"loading_gif")
        sizePolicy1.setHeightForWidth(self.loading_gif.sizePolicy().hasHeightForWidth())
        self.loading_gif.setSizePolicy(sizePolicy1)
        self.loading_gif.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.loading_gif)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.ContentTop)

        self.ContentBottom = QFrame(self.ContentBox)
        self.ContentBottom.setObjectName(u"ContentBottom")
        self.ContentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.ContentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.PagesContainer = QFrame(self.ContentBottom)
        self.PagesContainer.setObjectName(u"PagesContainer")
        self.PagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.PagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.PagesContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget = QStackedWidget(self.PagesContainer)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.StackedWidget.setMinimumSize(QSize(0, 0))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout = QVBoxLayout(self.Home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GridLayout = QGridLayout()
        self.GridLayout.setSpacing(6)
        self.GridLayout.setObjectName(u"GridLayout")
        self.GridLayout.setContentsMargins(9, 9, 9, 9)
        self.lbl_input = QLabel(self.Home)
        self.lbl_input.setObjectName(u"lbl_input")
        self.lbl_input.setFont(font1)

        self.GridLayout.addWidget(self.lbl_input, 0, 0, 1, 1)

        self.btn_open = QPushButton(self.Home)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QSize(0, 30))
        self.btn_open.setMaximumSize(QSize(150, 30))
        self.btn_open.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.target_language = QLineEdit(self.Home)
        self.target_language.setObjectName(u"target_language")
        self.target_language.setMinimumSize(QSize(0, 30))

        self.GridLayout2.addWidget(self.target_language, 1, 0, 1, 1)

        self.lbl_language = QLabel(self.Home)
        self.lbl_language.setObjectName(u"lbl_language")

        self.GridLayout2.addWidget(self.lbl_language, 0, 0, 1, 1)


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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.prompt_edit.sizePolicy().hasHeightForWidth())
        self.prompt_edit.setSizePolicy(sizePolicy3)
        self.prompt_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.prompt_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.prompt_edit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

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
        icon4.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_next, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.StackedWidget.addWidget(self.Home)
        self.PostProcessing = QWidget()
        self.PostProcessing.setObjectName(u"PostProcessing")
        self.verticalLayout_4 = QVBoxLayout(self.PostProcessing)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ScrollArea = QScrollArea(self.PostProcessing)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollAreaWidgetContents = QWidget()
        self.ScrollAreaWidgetContents.setObjectName(u"ScrollAreaWidgetContents")
        self.ScrollAreaWidgetContents.setGeometry(QRect(0, 0, 1059, 587))
        self.verticalLayout_5 = QVBoxLayout(self.ScrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
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
        self.NavBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.NavBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NavBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_back = QPushButton(self.NavBox)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(0, 30))
        self.btn_back.setMaximumSize(QSize(150, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon6.addFile(u":/icons/images/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_row.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.btn_delete_row)

        self.btn_start = QPushButton(self.NavBox)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 30))
        self.btn_start.setMaximumSize(QSize(150, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon8.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.btn_save)


        self.verticalLayout_4.addWidget(self.NavBox)

        self.StackedWidget.addWidget(self.PostProcessing)

        self.horizontalLayout_4.addWidget(self.StackedWidget)


        self.verticalLayout_6.addWidget(self.PagesContainer)


        self.verticalLayout_2.addWidget(self.ContentBottom)


        self.horizontalLayout_2.addWidget(self.ContentBox)

        self.AboutFrame = QFrame(self.CentralWidget)
        self.AboutFrame.setObjectName(u"AboutFrame")
        sizePolicy.setHeightForWidth(self.AboutFrame.sizePolicy().hasHeightForWidth())
        self.AboutFrame.setSizePolicy(sizePolicy)
        self.AboutFrame.setMinimumSize(QSize(0, 0))
        self.AboutFrame.setMaximumSize(QSize(0, 16777215))
        self.AboutFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AboutFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.AboutFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.about_text = QTextBrowser(self.AboutFrame)
        self.about_text.setObjectName(u"about_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.about_text.sizePolicy().hasHeightForWidth())
        self.about_text.setSizePolicy(sizePolicy4)
        self.about_text.setMinimumSize(QSize(360, 0))

        self.verticalLayout_13.addWidget(self.about_text)


        self.horizontalLayout_2.addWidget(self.AboutFrame)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setFont(font)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.btn_settings.setText("")
        self.btn_info.setText("")
        self.lbl_token.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>API Key:</p></body></html>", None))
        self.api_url_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#a1a1a1;\">You can get the API keys from here:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://platform.openai.com/api-keys\"><span style=\" font-size:10pt; text-decoration: underline; color:#739ef7;\">https://platform.openai.com/api-keys</span></a></p></body></"
                        "html>", None))
        self.max_tokens.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.lbl_max_tokens.setText(QCoreApplication.translate("MainWindow", u"Input Tokens", None))
        self.alignment_box.setText(QCoreApplication.translate("MainWindow", u"Fix Alignment", None))
        self.alignment_fix_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#a1a1a1;\">More tokens can improve translation accuracy; but might cause alignment issues</span></p></body></html>", None))
        self.lbl_model.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Model:</p></body></html>", None))
        self.combo_model.setItemText(0, QCoreApplication.translate("MainWindow", u"GPT 4o", None))
        self.combo_model.setItemText(1, QCoreApplication.translate("MainWindow", u"GPT 4 Turbo", None))
        self.combo_model.setItemText(2, QCoreApplication.translate("MainWindow", u"GPT 4", None))
        self.combo_model.setItemText(3, QCoreApplication.translate("MainWindow", u"GPT 3.5 Turbo", None))

        self.box_cosine.setText(QCoreApplication.translate("MainWindow", u"Cosine Similarty", None))
        self.lbl_threshold.setText(QCoreApplication.translate("MainWindow", u"Threshold:", None))
        self.threshold_edit.setInputMask("")
        self.threshold_edit.setText(QCoreApplication.translate("MainWindow", u"0.6", None))
        self.threshold_edit.setPlaceholderText("")
        self.cosine_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#a1a1a1;\">Compares input-output embeddings to enhance translation accuracy [0, 1] where 1 indicate perfect translation and indicates no similarity between input and output</span></p></body></html>", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">SubGPT</span></p></body></html>", None))
        self.loading_gif.setText("")
        self.lbl_input.setText(QCoreApplication.translate("MainWindow", u"Subtitle Template", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.subtitle_template.setText("")
        self.subtitle_template.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click Open to choose a file", None))
        self.target_language.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Arabic, English, Spanish ... etc", None))
        self.lbl_language.setText(QCoreApplication.translate("MainWindow", u"Target Language", None))
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
        self.about_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">SubGPT</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">v1.1.0</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Provides translations for multiple languages using OpenAI's GPT</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Developers</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">aalramadan</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HusseinAbuRayyash</p></body></html>", None))
        pass
    # retranslateUi

