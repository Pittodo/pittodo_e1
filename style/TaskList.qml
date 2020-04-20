import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3


ColumnLayout {
  id: tasks_list_layout
  x: 25
  y: 100
  width: parent.width - 75
  height:  parent.height - y -25

  MyTaskSeparator {}
  RowLayout {
    height: 40
    width: parent.width
    spacing: 15


    MyCircleButton { text: "A"}
    TextArea {
      Layout.fillWidth: true
      placeholderText: "Enter new task..."
      color: Style.myColor1
      wrapMode: Text.WordWrap

      background: Rectangle {
        color: Style.myColor5
      }
    }
    MyCircleButton { text: "B"}
    MyCircleButton { text: "C"}
  }
  MyTaskSeparator {}
  RowLayout {
    height: 40
    width: parent.width
    spacing: 15


    MyCircleButton { text: "A"}
    TextArea {
      Layout.fillWidth: true
      placeholderText: "Enter new task..."
      color: Style.myColor1
      wrapMode: Text.WordWrap

      background: Rectangle {
        color: Style.myColor5
      }
    }
    MyCircleButton { text: "B"}
    MyCircleButton { text: "C"}
  }
  MyTaskSeparator {}

  Rectangle {
    Layout.alignment: Qt.AlignBottom
    Layout.fillHeight: true
    color: Style.myColor5
    Layout.preferredWidth: parent.width
    Layout.preferredHeight: 40
  }


}
