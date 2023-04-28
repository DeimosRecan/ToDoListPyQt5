import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout() # вертикальный layout
        hbox = QHBoxLayout() # горизонтальный layout

        self.taskEntry = QLineEdit() # ввод новой задачи
        self.taskEntry.setPlaceholderText("Add task")
        self.taskEntry.returnPressed.connect(self.add_task)
        self.taskList = QListWidget() # список задач
        deleteButton = QPushButton("Delete") # кнопка для удаления задачи
        deleteButton.clicked.connect(self.delete_task)

        hbox.addWidget(self.taskEntry)
        hbox.addWidget(deleteButton)

        vbox.addWidget(QLabel("To-Do List"))
        vbox.addLayout(hbox)
        vbox.addWidget(self.taskList)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 350)
        self.show()

    def delete_task(self):
        task = self.taskList.currentRow()
        if task == -1:
            QMessageBox.warning(self, "Warning", "Please select a task to delete.")
        else:
            self.taskList.takeItem(task)

    def add_task(self):
        task = self.taskEntry.text()
        if task:
            self.taskList.addItem(task)
            self.taskEntry.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todolist = ToDoList()
    sys.exit(app.exec_())