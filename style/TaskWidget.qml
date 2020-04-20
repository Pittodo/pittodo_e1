import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3



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
  MyCircleButton {
    id: abc
    text: "B"}
  MyCircleButton { text: "C"}
}
