import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3



ApplicationWindow {
  width: 600
  height: 600
  flags: Qt.Window | Qt.FramelessWindowHint
  visible: true
  title: qsTr("PitToDo")
  color: "transparent"


  Rectangle {
    radius: 15
    color: Style.myColor5
    border.color: Style.myColor1
    border.width: 5
    anchors.fill: parent
    anchors.centerIn: parent

    TaskList {}
    TopBar {}
    Image {
      source: "../images/logo.png"
      x: 25
      y: 25
    }
  }
}
