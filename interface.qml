import QtQuick 2.0
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ApplicationWindow {
  width: 500
  height: 500
  flags: Qt.Window | Qt.FramelessWindowHint
  visible: true
  title: qsTr("backlight")
  color: "transparent"

  Rectangle {
    width: 200
    height: 200
    radius: 25
    color: "white"
    border.color: "blue"
    border.width: 5
    anchors.fill: parent
    anchors.centerIn: parent

    Image {
      source: "images/logo.png"
      x: 25
      y: 25
    }

    Text {
      text: "Hello world"
      anchors.centerIn: parent

    }
    Image {
      source: "images/cancel_button.png"
      x: parent.width - 25 - sourceSize.width
      y: 25
      MouseArea {
        anchors.fill: parent
        onClicked: console.log("Button exit clicked!")
      }
    }
  }
}
