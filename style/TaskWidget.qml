import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3



RowLayout {
  id: one_task
  height: 40
  // width: 500
  spacing: 0
  Layout.leftMargin:0
  Layout.rightMargin:0
  Layout.maximumWidth: flickable.width - Layout.leftMargin
  Layout.minimumWidth: flickable.width - Layout.rightMargin


  // Layout.fillWidth: true


  MyCircleButton {
    id: btn_a
    text: "A"
    height: 40
  }
  TextArea {
    placeholderText: "Enter new task..."
    color: Style.myColor1
    wrapMode: Text.Wrap
    Layout.fillWidth: true

    background: Rectangle {
      // implicitWidth: 300
      // implicitHeight: 40
      color: Style.myColor5
    }
  }
  MyCircleButton {
    id: btn_b
    text: "B"
    height: 40
  }
  MyCircleButton {
    id: btn_c
    text: "C"
    height: 40
  }

}
