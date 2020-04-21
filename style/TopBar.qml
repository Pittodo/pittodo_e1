import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file


Rectangle {
  x: 0
  y: 0
  width: parent.width
  height: 40
  radius: parent.radius
  color: "transparent"

  MyCircleButton {
    id: minimize_btn
    text: "-"
    x: root_window.width - 2*height - 30
    y: height
  }
  MyCircleButton {
    id: exit_btn
    text: "X"
    x: root_window.width - 1*height - 15
    y: height
  }
}
